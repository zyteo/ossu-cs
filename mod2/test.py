import string
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


secret_word = "apple"
letters_guessed = ["e", "i", "k", "p", "r", "s"]
print(get_available_letters(letters_guessed))
