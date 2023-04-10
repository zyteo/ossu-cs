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
    print(my_word)
    if len(my_word) != len(other_word):
        print("lengths not same", len(my_word), len(other_word))
        return False
    else:
        for i in range(len(my_word)):
            print(my_word[i], other_word[i])


match_with_gaps("t__t", "tact")
