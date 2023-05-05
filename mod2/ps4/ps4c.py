# Problem Set 4C
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx
# Started 5 May 2023 by zyteo
# Completed x May 2023

import string
from ps4a import get_permutations

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
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
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
    def __init__(self, text):
        '''
        Initializes a SubMessage object
                
        text (string): the message's text

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
    
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]
                
    def build_transpose_dict(self, vowels_permutation):
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)
        
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled 
        according to vowels_permutation. The first letter in vowels_permutation 
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52 
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        # first create a dictionary with all the letters
        # then using the vowels permutation, change the vowels
        # add the consonants to the dictionary
        # return the dictionary
        transpose_dict = {}
        for i in range(len(VOWELS_LOWER)):
            transpose_dict[VOWELS_LOWER[i]] = vowels_permutation[i]
            transpose_dict[VOWELS_UPPER[i]] = vowels_permutation[i].upper()
        for i in range(len(CONSONANTS_LOWER)):
            transpose_dict[CONSONANTS_LOWER[i]] = CONSONANTS_LOWER[i]
            transpose_dict[CONSONANTS_UPPER[i]] = CONSONANTS_UPPER[i]

        return transpose_dict
        
    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary
        
        Returns: an encrypted version of the message text, based 
        on the dictionary
        '''
        # create a new string
        # for each letter in the message text, convert it to the new letter
        # return the new string
        transposed_text = ''
        for letter in self.message_text:
            if letter in string.punctuation or letter == ' ':
                transposed_text += letter
            else:
                transposed_text += transpose_dict[letter]
        return transposed_text


class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        SubMessage.__init__(self, text)

    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message 
        
        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.
        
        If no good permutations are found (i.e. no permutations result in 
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message    
        
        Hint: use your function from Part 4A
        '''
        # first get the list of permutations
        # create a dictionary that maps each permutation to the number of valid words
        # for each permutation, apply the transpose and check how many valid words, then add to the dictionary
        # once done, check which permutation has the most valid words
        # return the decrypted message
        permutations = get_permutations(VOWELS_LOWER)
        valid_words_dict = {}
        for permutation in permutations:
            transpose_dict = self.build_transpose_dict(permutation)
            decrypted_message = self.apply_transpose(transpose_dict)
            valid_words = 0
            for word in decrypted_message.split():
                if is_word(self.valid_words, word):
                    valid_words += 1
            valid_words_dict[permutation] = valid_words
        
        max_valid_words = 0
        best_permutation = ''
        for permutation in permutations:
            if valid_words_dict[permutation] > max_valid_words:
                max_valid_words = valid_words_dict[permutation]
                best_permutation = permutation

        if max_valid_words == 0:
            return self.message_text
        else:
            transpose_dict = self.build_transpose_dict(best_permutation)
            decrypted_message = self.apply_transpose(transpose_dict)
            return decrypted_message   

if __name__ == '__main__':

    # Example test case
    message = SubMessage("Hello World!")
    permutation = "eaiuo"
    # aeiou
    # eaiuo
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Hallu Wurld!")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())
     
    #TODO: WRITE YOUR TEST CASES HERE
    #     Write two test cases for SubMessage and two test cases for 
    # EncryptedSubMessage in comments under if __name__ == ‘__main__’ . 
    # Each test case should contain the input, expected output, function call used, 
    # and actual output. 
    # First test case
    message1 = SubMessage("This is A VERY bIg cAT!")
    permutation1 = "iouae"
    # aeiou
    # iouae
    encoded_dict1 = message1.build_transpose_dict(permutation1)
    print("Original message:", message1.get_message_text(), "Permutation:", permutation1)
    print("Expected encryption:", "Thus us I VORY bUg cIT!")
    print("Actual encryption:", message1.apply_transpose(encoded_dict1))
    encoded_message1 = EncryptedSubMessage(message1.apply_transpose(encoded_dict1))
    print("Decrypted message:", encoded_message1.decrypt_message())

    # Second test case
    message2 = SubMessage("The MESSAGE has been ENCRYPTED!")
    permutation2 = "iuoea"
    # aeiou
    # iuoea
    encoded_dict2 = message2.build_transpose_dict(permutation2)
    print("Original message:", message2.get_message_text(), "Permutation:", permutation2)
    print("Expected encryption:", "Thu MUSSIGU his buun UNCRYPTUD!")
    print("Actual encryption:", message2.apply_transpose(encoded_dict2))
    encoded_message2 = EncryptedSubMessage(message2.apply_transpose(encoded_dict2))
    print("Decrypted message:", encoded_message2.decrypt_message())