# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:
# Started 7 Apr 2023 by zyteo

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

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
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


# 1A) Determine whether the word has been guessed
# is_word_guessed that takes in two parameters a
# string, secret_word , and a list of letters (strings), letters_guessed. This function
# returns a boolean True
# if secret_word has been guessed (i.e., all the letters of
# secret_word are in letters_guessed ), and False otherwise. This function will be
# useful in helping you decide when the hangman game has been successfully
# completed, and becomes an endtest
# for any iterative loop that checks letters against
# the secret word.
def is_word_guessed(secret_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    """
    flag = True
    for letter in secret_word:
        if letter not in letters_guessed:
            flag = False
    return flag


# 1B) Getting the user’s guess
# get_guessed_word that takes in two parameters a
# string, secret_word , and a list of letters, letters_guessed . This function returns a
# string that is comprised of letters and underscores, based on what letters in
# letters_guessed are in secret_word . This shouldn't be too different from
# is_word_guessed !
def get_guessed_word(secret_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    """
    # first make a copy of secret word
    # loop through letters in copy. if letter not in letters_guessed, replace with "_ "
    copy = secret_word
    for letter in copy:
        if letter not in letters_guessed:
            copy = copy.replace(letter, "_ ")
    return copy


# 1C) Getting all available letters
# get_available_letters that takes in one parameter a
# list of letters, letters_guessed . This function returns a string that is comprised of
# lowercase English letters all
# lowercase English letters that are not in
# letters_guessed .
# This function should return the letters in alphabetical order. For this function, you may
# assume that all the letters in letters_guessed are lowercase.
def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    """
    # first get all lowercase letters of the alphabet with string package
    # then replace the letters in letters_guessed with ""
    remaining_letters = string.ascii_lowercase
    for alphabet in letters_guessed:
        remaining_letters = remaining_letters.replace(alphabet, "")
    return remaining_letters


# Game Requirements
# A. Game Architecture:
# 1. The computer must select a word at random from the list of available words
# that was provided in words.txt. The functions for loading the word list and
# selecting a random word have already been provided for you in hangman.py.
# 2. Users start with 6 guesses.
# 3. At the start of the game, let the user know how many letters the computer's
# word contains and how many guesses s/he starts with.
# 4. The computer keeps track of all the letters the user has not guessed so far and
# before each turn shows the user the “remaining letters”

# B. User Computer Interaction:
# The game must be interactive and flow as follows:
# 1. Before each guess, you should display to the user:
# a. Remind the user of how many guesses s/he has left after each guess.
# b. all the letters the user has not yet guessed
# 2. Ask the user to supply one guess at a time. (Look at the user input
# requirements below to see what types of inputs you can expect from the user)
# 3. Immediately after each guess, the user should be told whether the letter is in the computer’s word.
# 4. After each guess, you should also display to the user the computer’s word, with
# guessed letters displayed and unguessed letters replaced with an underscore
# and space (_ )
# 5. At the end of the guess, print some dashes ()
# to help separate individual
# guesses from each other


# C. User Input Requirements:
# 1. You may assume that the user will only guess one character at a time, but the
# user can choose any number, symbol or letter. Your code should accept capital
# and lowercase letters as valid guesses!
# 2. If the user inputs anything besides an alphabet (symbols, numbers), tell the
# user that they can only input an alphabet. Because the user might do this by
# accident, they should get 3 warnings at the beginning of the game. Each time
# they enter an invalid input, or a letter they have already guessed, they should
# lose a warning. If the user has no warnings left and enters an invalid input,
# they should lose a guess.


# D. Game Rules:
# 1. The user starts with 3 warnings.
# 2. If the user inputs anything besides an alphabet (symbols, numbers), tell the
# user that they can only input an alphabet.
# a. If the user has one or more warning left, the user should lose one
# warning. Tell the user the number of remaining warnings.
# b. If the user has no remaining warnings, they should lose one guess.
# 3. If the user inputs a letter that has already been guessed, print a message
# telling the user the letter has already been guessed before.
# a. If the user has one or more warning left, the user should lose one
# warning. Tell the user the number of remaining warnings.
# b. If the user has no warnings, they should lose one guess.
# 4. If the user inputs a letter that hasn’t been guessed before and the letter is in
# the secret word, the user loses no guesses.
# 5. Consonants: If the user inputs a consonant that hasn’t been guessed and the
# consonant is not in the secret word, the user loses one guess if it’s a
# consonant.
# 6. Vowels: If the vowel hasn’t been guessed and the vowel is not in the secret
# word, the user loses two guesses. Vowels are a, e, i , o, and u. y does not
# count as a vowel.


# E. Game Termination:
# 1. The game should end when the user constructs the full word or runs out of
# guesses.
# 2. If the player runs out of guesses before completing the word, tell them they
# lost and reveal the word to the user when the game ends.
# 3. If the user wins, print a congratulatory message and tell the user their score.
# 4. The total score is the number of guesses_remaining once the user has
# guessed the secret_word times the number of unique letters in secret_word .
def hangman(secret_word):
    """
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    """
    guesses_left = 6
    letters_guessed = []
    game_running = True
    user_warning = 3
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")
    print("-" * 13)
    while game_running:
        if guesses_left <= 0:
            print("Sorry, you ran out of guesses. The word was", secret_word)
            game_running = False
            break
        if is_word_guessed(secret_word, letters_guessed):
            print("Congratulations, you won!")
            print(
                "Your total score for this game is:",
                guesses_left * len(set(secret_word)),
            )
            game_running = False
            break
        # get user input, check if valid alphabet
        # if yes, convert to lowercase
        # if no, check user warning.
        # if warning >= 1, minus 1 and continue
        # if warning = 0, minus 1 guess and continue
        print("You have", guesses_left, "guesses left.")
        print("Available letters:", get_available_letters(letters_guessed))
        user_guess = input("Please guess a letter: ")
        check_valid_alphabet = str.isalpha(user_guess)
        if check_valid_alphabet:
            user_guess = user_guess.lower()
            # if user guess is in letters guessed, say already guessed
            if user_guess in letters_guessed:
                if user_warning >= 1:
                    user_warning -= 1
                    print(
                        "Oops! You've already guessed that letter. You have",
                        user_warning,
                        "warnings left:",
                        get_guessed_word(secret_word, letters_guessed),
                    )
                    print("-" * 13)
                    continue
                else:
                    guesses_left -= 1
                    print(
                        "Oops! You've already guessed that letter. You have no warnings left so you lose one guess:",
                        get_guessed_word(secret_word, letters_guessed),
                    )
                    print("-" * 13)
                    continue
            # if user guess is in secret word, say good guess, otherwise say that isn't in the word
            if user_guess in secret_word:
                letters_guessed.append(user_guess)
                print("Good guess:", get_guessed_word(secret_word, letters_guessed))
                print("-" * 13)
            else:
                letters_guessed.append(user_guess)
                print(
                    "Oops! That letter is not in my word:",
                    get_guessed_word(secret_word, letters_guessed),
                )
                print("-" * 13)
                # if user guess is a vowel, minus 2 guesses, otherwise minus 1 guess
                if user_guess in "aeiou":
                    guesses_left -= 2
                else:
                    guesses_left -= 1

        else:
            if user_warning >= 1:
                user_warning -= 1
                print(
                    "Oops! That is not a valid letter. You have",
                    user_warning,
                    "warnings left:",
                    get_guessed_word(secret_word, letters_guessed),
                )
                print("-" * 13)
                continue
            else:
                guesses_left -= 1
                print(
                    "Oops! That is not a valid letter. You have no warnings left so you lose one guess:",
                    get_guessed_word(secret_word, letters_guessed),
                )
                print("-" * 13)
                continue


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
# (hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------
# match_with_gaps takes two parameters: my_word and other_word. my_word is an
# instance of a guessed word, in other words, it may have some _ ’s in places (such as
# ‘t_ _ t’). other_word is a normal English word.
# This function should return True if the guessed letters of my_word match the
# corresponding letters of other_word . It should return False if the two words are not
# of the same length or if a guessed letter in my_word does not match the
# corresponding character in other_word.
# Remember that when a letter is guessed, your code reveals all the positions at which
# that letter occurs in the secret word. Therefore, the hidden letter (_ ) cannot be one
# of the letters in the word that has already been revealed.
def match_with_gaps(my_word, other_word):
    """
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    """
    # first strip my_word of spaces
    # then compare length of my_word and other_word, if not same, return false
    # compare each letter of my_word and other_word, if not same, return false
    my_word = my_word.replace(" ", "")
    alphabets = {}
    underscores = 0
    print(my_word)
    if len(my_word) != len(other_word):
        print("lengths not same", len(my_word), len(other_word))
        return False

    for i in range(len(my_word)):
        print(my_word[i], other_word[i])
        # if both are alphabets and they are not the same, confirm false, so write this part first
        if (my_word[i] != "_") and (my_word[i] != other_word[i]):
            print("not same")
            return False
        # if both are alphabets and they are the same, continue
        elif (my_word[i] != "_") and (my_word[i] == other_word[i]):
            print("same")
            continue
        elif my_word[i] == "_":
            # need to think about this case
            # record the number of underscores and store the alphabet count in a dictionary
            # if the number of underscores is not the same as the total alphabet count, return false
            underscores += 1
            if other_word[i] in alphabets:
                continue
            else:
                for x in other_word:
                    if x == other_word[i]:
                        if other_word[i] not in alphabets:
                            alphabets[other_word[i]] = 1
                        else:
                            alphabets[other_word[i]] += 1
    print(underscores, sum(alphabets.values()))
    if underscores != sum(alphabets.values()):
        return False
    else:
        return True

# show_possible_matches takes a single parameter: my_word which is an instance of a
# guessed word, in other words, it may have some _ ’s in places (such as ‘t_ _ t’).
# This function should print out all words in wordlist (notice where we have defined
# this at the beginning of the file, line 51) that match my_word . It should print “No
# matches found” if there are no matches.
def show_possible_matches(my_word):
    """
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass


def hangman_with_hints(secret_word):
    """
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word.

    Follows the other limitations detailed in the problem write-up.
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    secret_word = choose_word(wordlist)
    hangman(secret_word)
    # hangman("tact")

###############

# To test part 3 re-comment out the above lines and
# uncomment the following two lines.

# secret_word = choose_word(wordlist)
# hangman_with_hints(secret_word)
