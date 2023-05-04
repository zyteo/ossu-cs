# Problem Set 4B
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx
# Started 2 May 2023 by zyteo
# Completed x May 2023

import string

# The idea of the Caesar Cipher is to pick an integer and shift every letter of your message by that integer. In other words, suppose the shift is kth . Then, all instances of the i letter of the alphabet that appear in the plaintext should become the (i + k) th letter of the alphabet in the ciphertext. You will need to be careful with the case in which i + k > 26 (the length of the alphabet).


### HELPER CODE ###
def load_words(file_name):
    """
    file_name (string): the name of the file containing
    the list of words to load

    Returns: a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, "r")
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(" ")])
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def is_word(word_list, word):
    """
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.

    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story


### END HELPER CODE ###

WORDLIST_FILENAME = "words.txt"


# We have provided skeleton code in the Message class for the following functions - your task is to implement them. Please see the docstring comment with each function for more information about the function specification.
# ●__init__(self, text)
# ●The getter methods
# ○get_message_text(self)
# ●Note: This should return an immutable version of the message text we added to this object in init. Luckily, strings are already immutable objects, so we can simply return that string.
# ○get_valid_words(self)
# ●Note: this should return a COPY of self.valid_words to prevent someone from accidentally mutating the original list. ●build_shift_dict(self, shift)
# ●Note: you may find the string module’s ascii_lowercase constant helpful here.
# ●apply_shift(self, shift) ○Hint: use build_shift_dict(self, shift). Remember that spaces and punctuation should not be changed by the cipher.
class Message(object):
    def __init__(self, text):
        """
        Initializes a Message object

        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        """
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    def get_message_text(self):
        """
        Used to safely access self.message_text outside of the class

        Returns: self.message_text
        """
        return self.message_text

    def get_valid_words(self):
        """
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.

        Returns: a COPY of self.valid_words
        """
        return self.valid_words[:]

    def build_shift_dict(self, shift):
        """
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.

        shift (integer): the amount by which to shift every letter of the
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to
                 another letter (string).
        """
        # create 2 lists, one for lowercase and one for uppercase
        # the 2 lists will be in order of the alphabet
        # create 2 new lists, one for lowercase and one for uppercase
        # in a loop, create the dictionary. if index + shift > 26, then just take the modulus (which is the remainder)
        # if less than 26, then just add the shift to the index
        # once done, create the dictionary
        upper = list(string.ascii_uppercase)
        lower = list(string.ascii_lowercase)
        upper_shifted = []
        lower_shifted = []
        letter_map = {}
        for i in range(len(upper)):
            if i + shift > 25:
                upper_shifted.append(upper[(i + shift) % 26])
            else:
                upper_shifted.append(upper[i + shift])
        for i in range(len(lower)):
            if i + shift > 25:
                lower_shifted.append(lower[(i + shift) % 26])
            else:
                lower_shifted.append(lower[i + shift])
        for i in range(len(upper)):
            letter_map[upper[i]] = upper_shifted[i]
        for i in range(len(lower)):
            letter_map[lower[i]] = lower_shifted[i]
        return letter_map

    def apply_shift(self, shift):
        """
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift

        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        """
        # get the letter map with the function above
        # create a new string based on the letter map
        # if the string is not a letter, then just add the character to the new string
        map_for_shift = self.build_shift_dict(shift)
        new_string = ""
        for char in self.message_text:
            if char in map_for_shift:
                new_string += map_for_shift[char]
            else:
                new_string += char
        return new_string


# The methods you should fill in are:
# ●__init__(self, text, shift) ○Use the parent class constructor to make your code more concise. Take a look at Style Guide #7 if you are confused.
# ●The getter methods ○get_shift(self)
# ○get_encryption_dict(self) ■Note: this should return a COPY of self.encryption_dict to prevent someone from mutating the original dictionary. ○get_message_text_encrypted(self)
# ●change_shift(self, shift) ○Hint: think about what other methods you can use to make this easier. It shouldn’t take more than a couple lines of code
class PlaintextMessage(Message):
    def __init__(self, text, shift):
        """
        Initializes a PlaintextMessage object

        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        """
        # use parent class constructor to make code more concise
        Message.__init__(self, text)
        # only need to define 3 new attributes
        self.shift = shift
        self.encryption_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)

    def get_shift(self):
        """
        Used to safely access self.shift outside of the class

        Returns: self.shift
        """
        return self.shift

    def get_encryption_dict(self):
        """
        Used to safely access a copy self.encryption_dict outside of the class

        Returns: a COPY of self.encryption_dict
        """
        return self.encryption_dict.copy()

    def get_message_text_encrypted(self):
        """
        Used to safely access self.message_text_encrypted outside of the class

        Returns: self.message_text_encrypted
        """
        return self.message_text_encrypted

    def change_shift(self, shift):
        """
        Changes self.shift of the PlaintextMessage and updates other
        attributes determined by shift.

        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        """
        # change the shift
        self.shift = shift
        # change the encryption dictionary
        self.encryption_dict = self.build_shift_dict(shift)
        # change the message text encrypted
        self.message_text_encrypted = self.apply_shift(shift)


# The methods you should fill in are:
# ●__init__(self, text) ○Hint: use the parent class constructor to make your code more concise. Take a look at Style Guide #7 if you are confused.
# ●decrypt_message(self) ○Hint: you may find the helper function is_word(wordlist, word) and the string method split useful ( https://docs.python.org/3/library/stdtypes.html#str.split
# , or alternatively help(str.split) in your console) ○Note: is_word will ignore punctuation and other special characters when considering whether a word is valid.
class CiphertextMessage(Message):
    def __init__(self, text):
        """
        Initializes a CiphertextMessage object

        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        """
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    def decrypt_message(self):
        """
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create
        the maximum number of valid words, you may choose any of those shifts
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        """
        # first create a dictionary of all possible shifts and the number of valid words
        # then search the highest number of valid words and create the tuple to return
        shift_dict = {}
        for shift in range(26):
            new_message = self.apply_shift(shift)
            words = new_message.split(" ")
            valid_words = 0
            for word in words:
                if is_word(self.valid_words, word):
                    valid_words += 1
            shift_dict[shift] = valid_words
        # search the highest number of valid words and create the tuple to return
        best_shift = max(shift_dict, key=shift_dict.get)
        return best_shift, self.apply_shift(best_shift)


if __name__ == "__main__":
    # test message
    message = Message("Abc, !")
    print(message.get_message_text())
    print(message.build_shift_dict(2))
    print(message.apply_shift(2))

    # Example test case (PlaintextMessage)
    plaintext = PlaintextMessage("hello", 2)
    print("Expected Output: jgnnq")
    print("Actual Output:", plaintext.get_message_text_encrypted())
    #
    # Example test case (CiphertextMessage)
    ciphertext = CiphertextMessage("jgnnq")
    print("Expected Output:", (24, "hello"))
    print("Actual Output:", ciphertext.decrypt_message())

    # TODO: WRITE YOUR TEST CASES HERE
    # Write two test cases for PlaintextMessage and two test cases for
    # CiphertextMessage in comments under if name == ‘__main__’ . Each
    # test case should display the input, expected output, and actual output. An
    # example can be found in ps4b.py. Then, decode the file story.txt and write
    # the best shift value used to decrypt the story, and unencrypted story in a
    # comment underneath your test cases.
    plaintext_test1 = PlaintextMessage("this is a test", 5)
    print("Expected Output: ymnx nx f yjxy")
    print("Actual Output:", plaintext_test1.get_message_text_encrypted())

    plaintext_test2 = PlaintextMessage("WHAT did the cat SAY?!?", 10)
    print("Expected Output: GRKD nsn dro mkd CKI?!?")
    print("Actual Output:", plaintext_test2.get_message_text_encrypted())

    ciphertext_test1 = CiphertextMessage("ymnx nx f yjxy")
    print("Expected Output:", (21, "this is a test"))
    print("Actual Output:", ciphertext_test1.decrypt_message())

    ciphertext_test2 = CiphertextMessage("GRKD nsn dro mkd CKI?!?")
    print("Expected Output:", (16, "WHAT did the cat SAY?!?"))
    print("Actual Output:", ciphertext_test2.decrypt_message())

    # Hint: The skeleton code contains a helper function get_story_string that returns
    # the encrypted version of the story as a string. Create a CiphertextMessage object
    # using the story string and use decrypt_message to return the appropriate shift
    # value and unencrypted story.
    # TODO: best shift value and unencrypted story
    # read the file story.txt
    # find the best shift value
    # decrypt the story
    # print the best shift value and the unencrypted story
    story = get_story_string()
    ciphertext_story = CiphertextMessage(story)
    print("Best shift value:", ciphertext_story.decrypt_message()[0])
    print("Unencrypted story:", ciphertext_story.decrypt_message()[1])
