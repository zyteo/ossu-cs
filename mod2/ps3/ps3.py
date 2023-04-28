# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : <your name>
# Collaborators : <your collaborators>
# Time spent    : <total time>
# Started 24 Apr 2023 by zyteo

import math
import random
import string

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
# account for wildcard
VOWELS += "*"
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    "a": 1,
    "b": 3,
    "c": 3,
    "d": 2,
    "e": 1,
    "f": 4,
    "g": 2,
    "h": 4,
    "i": 1,
    "j": 8,
    "k": 5,
    "l": 1,
    "m": 3,
    "n": 1,
    "o": 1,
    "p": 3,
    "q": 10,
    "r": 1,
    "s": 1,
    "t": 1,
    "u": 1,
    "v": 4,
    "w": 4,
    "x": 8,
    "y": 4,
    "z": 10,
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """

    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, "r")
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """

    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x, 0) + 1
    return freq


# (end of helper code)
# -----------------------------------


#
# Problem #1: Scoring a word
# As a reminder, here are the rules for scoring a word: ●The score for a word is the product of two components:oFirst component: the sum of the points for letters in the word. oSecond component: either [7 * word_length - 3 * ( n- word_length)] or 1,whichever value is greater, where: ▪word_length is the number of letters used in the word ▪n is the number of letters available in the current handYou should use the SCRABBLE_LETTER_VALUES dictionary defined at the top of ps3.py . Do not assume that there are always 7 letters in a hand! The parameter n is the total number of letters in the hand when the word was entered.
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters,
    or the empty string "". You may not assume that the string will only contain
    lowercase letters, so you will have to handle uppercase and mixed case strings
    appropriately.

        The score for a word is the product of two components:

        The first component is the sum of the points for letters in the word.
        The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

        Letters are scored as in Scrabble; A is worth 1, B is
        worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """

    # first calculate the first component
    # convert all to lowercase
    # in a for loop, add up the score
    # second component
    # calculate the formula first. if > 1, return the formula. if < 1, return 1
    # multiply the two components together
    # i will let first component be a and second component be b

    word = word.lower()
    a = 0
    for letter in word:
        a += SCRABBLE_LETTER_VALUES[letter]

    calculation = 7 * len(word) - 3 * (n - len(word))
    if calculation > 1:
        b = calculation
    else:
        b = 1

    return a * b


#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """

    for letter in hand.keys():
        for j in range(hand[letter]):
            print(letter, end=" ")  # print all on the same line
    print()  # print an empty line


#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
# We want to allow hands to contain wildcard letters, which will be denoted by an asterisk (*). Wildcards can only replace vowels. Each hand dealt should initially contain exactly one wildcard as one of its letters. The player does not receive any points for using the wildcard (unlike all the other letters), though it does count as a used or unused letter when scoring. During the game, a player wishing to use a wildcard should enter "*" (without quotes) instead of the intended letter. The word-validation code should not make any assumptions about what the intended vowel should be, but should verify that at least one valid word can be made with the wildcard as a vowel in the desired position.
# Modify the deal_hand function to support always giving one wildcard in each hand. Notethat deal_hand currently ensures that one third of the letters are vowels and the rest areconsonants. Leave the consonant count intact, and replace one of the vowel slots with the wildcard. You will also need to modify one or more of the constants defined at the top of the file to account for wildcards. Then modify the is_valid_word function to support wildcards. Hint: Check to see whatpossible words can be formed by replacing the wildcard with other vowels. You may want to review the documentation
# for string module’s find() function and make note of itsbehavior when a character is not found. The constant VOWELS defined for you at the top ofthe file may be helpful as well.
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """

    hand = {}
    num_vowels = int(math.ceil(n / 3)) - 1

    for i in range(num_vowels):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1

    for i in range(num_vowels, n):
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1

    hand["*"] = 1
    return hand


#
# Problem #2: Update a hand by removing letters
# The player starts with a full hand of n letters. As the player spells out words, letters from the set are used up. For example, the player could start with the following hand: a, q, l, m, u, i, l The player could choose to play the word quail. This would leave the following letters in the player's hand: l, m. You will now write a function that takes a hand and a word as inputs, uses letters from that hand to spell the word, and returns a new hand containing only the remaining letters. Your function should not modify the input hand. For example: >>hand = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1} >>display_hand(hand) a q l l m u i>>new_hand = update_hand(hand, 'quail') >>new_hand{'l': 1, 'm': 1} >>display_hand(new_hand) l m>>display_hand(hand) a q l l m u i
# IMPORTANT: If the player guesses a word that is invalid, either because it is not a real word or because they used letters that they don't actually have in their hand, they still lose the letters from their hand that they did guess as a penalty. Make sure that your implementation accounts for this! Do not assume that the word you are given only uses letters that actually exist in the hand. For example: >>hand = {'j':2, 'o':1, 'l':1, 'w':1, 'n':2} >>display_hand(hand) j j o l w n n>>hand = update_hand(hand, 'jolly') >>hand{'j':1, w':1, 'n':2} >>display_hand(hand) j w n n
def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured).

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    """
    # convert word to lowercase
    # make a copy of hand
    # in a for loop, for each letter in word, minus 1 in the dictionary if have
    # if value is 0, then do not minus 1
    # return new hand
    word = word.lower()
    copy_hand = hand.copy()
    for letter in word:
        if letter in copy_hand.keys():
            if copy_hand[letter] > 0:
                copy_hand[letter] -= 1

    return copy_hand


#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.

    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """

    # create another function to check for possible word
    def check_possible_word(word, hand, word_list):
        word = word.lower()
        copy_hand = hand.copy()

        if word not in word_list:
            return False
        else:
            for letter in word:
                if letter not in copy_hand:
                    return False
                else:
                    copy_hand[letter] -= 1
                    if copy_hand[letter] < 0:
                        return False
        return True

    # first check if word is in word_list. if false, return false
    # if true, continue
    # in a loop, check if each letter in word is in hand. if false, return false
    # when checking, need to make sure that hand has sufficient number of letters to make word. i will make a copy of hand and remove letters as i check them
    word = word.lower()
    copy_hand = hand.copy()
    possible_words = []
    # now split into 2 cases - one if word contains *, the the other if not containing *
    if "*" in word:
        # now check if word is valid by replacing * with each vowel and checking if the word is in word_list
        # check every vowel except for *
        index_of_asterisk = word.find("*")
        for vowel in VOWELS and vowel != "*":
            new_word = word[:index_of_asterisk] + vowel + word[index_of_asterisk + 1 :]
            # now check if new_word is in word_list. if yes, then add to possible_words
            if new_word in word_list:
                possible_words.append(new_word)
        # now check if possible_words is empty. if yes, then return false
        if len(possible_words) == 0:
            return False
        else:
            # now check if any one of the possible_words can be made from hand
            # at first the below else statement was the previous version of is_valid_word, but i made into a function instead since i need to use twice
            for possible_word in possible_words:
                if check_possible_word(possible_word, copy_hand, word_list):
                    return True
            # if none of the possible_words can be made from hand, return false
            return False

    else:
        return check_possible_word(word, hand, word_list)


#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """
    Returns the length (number of letters) in the current hand.

    hand: dictionary (string-> int)
    returns: integer
    """
    # use a loop to add up all the values in hand
    # return the sum
    sum_length = 0
    for key in hand:
        sum_length += hand[key]
    return sum_length


def play_hand(hand, word_list):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.

    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand

    """

    # BEGIN PSEUDOCODE <-- Remove this comment when you implement this function
    # Keep track of the total score

    # As long as there are still letters left in the hand:

    # Display the hand

    # Ask user for input

    # If the input is two exclamation points:

    # End the game (break out of the loop)

    # Otherwise (the input is not two exclamation points):

    # If the word is valid:

    # Tell the user how many points the word earned,
    # and the updated total score

    # Otherwise (the word is not valid):
    # Reject invalid word (print a message)

    # update the user's hand by removing the letters of their inputted word

    # Game is over (user entered '!!' or ran out of letters),
    # so tell user the total score

    # Return the total score as result of function


#
# Problem #6: Playing a game
#


#
# procedure you will use to substitute a letter in a hand
#


def substitute_hand(hand, letter):
    """
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.

    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """

    pass  # TO DO... Remove this line when you implement this function


def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the
      entire series

    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep
      the better of the two scores for that hand.  This can only be done once
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.

    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """

    print(
        "play_game not implemented."
    )  # TO DO... Remove this line when you implement this function


#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == "__main__":
    word_list = load_words()
    play_game(word_list)
