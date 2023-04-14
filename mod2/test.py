def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open("./ps2/words.txt", "r")
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


wordlist = load_words()


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
    # replace "_ " with "_"
    my_word = my_word.replace("_ ", "_")
    match_word_holder = []
    # in a for loop, iterate through the wordlist, first check the length of the word
    # if length not same, move on. if same, compare first alphabet
    # if first alphabet not same, move on.
    # if same, more task to process
    for word in wordlist:
        if len(word) != len(my_word):
            continue
        else:
            if word[0] != my_word[0]:
                continue
            else:
                # first alphabet same. now check the rest of the word
                # similar to previous function. loop through the word, for every underscore portion, check for corresponding alphabet and add to dictionary
                # at the end of loop, if underscore sum is not same as dictionary value sum, do not add word to list
                alphabets = {}
                underscore = 0
                for i in range(len(my_word)):
                    if my_word[i] != "_":
                        # check if alphabet is the same. if not same, break
                        if my_word[i] != word[i]:
                            break
                    else:
                        underscore += 1
                        if word[i] in alphabets:
                            continue
                        else:
                            for x in word:
                                if x == word[i]:
                                    if word[i] not in alphabets:
                                        alphabets[word[i]] = 1
                                    else:
                                        alphabets[word[i]] += 1
                if underscore != sum(alphabets.values()):
                    continue
                else:
                    match_word_holder.append(word)

    if len(match_word_holder) == 0:
        print("No matches found")
    else:
        print(" ".join(match_word_holder))


show_possible_matches("t_ _ t")
