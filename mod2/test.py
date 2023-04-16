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
                # check if every alphabet in my_word is same as word for non underscore portions
                # any part that is not similar, move on to next word. if same, move on to next process
                # make use of match_with_gaps function. if true, add word to list. if false, move on to next word

                # technically this part below is not needed. but i think it would be faster to do this
                for i in range(len(my_word)):
                    if my_word[i] != "_":
                        if my_word[i] != word[i]:
                            break

                if match_with_gaps(my_word, word):
                    match_word_holder.append(word)
                else:
                    continue
    if len(match_word_holder) == 0:
        print("No matches found")
    else:
        print(" ".join(match_word_holder))


show_possible_matches("t_ _ t")
show_possible_matches("abbb _")
show_possible_matches("a_ pl_ ")
