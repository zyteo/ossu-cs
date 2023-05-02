# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx
# Started 2 May 2023 by zyteo


# In order to solve any recursive problem, we must have at least one base case and a recursive case (or cases). We can think of our base case as the simplest input we could have to this problem (for which determining the solution is trivial and requires no recursion) -- for this approach, our base case is if sequence is a single character (there’s only one way to order a single character). If sequence is longer than one character, we need to identify a simpler version of the problem that, if solved, will help us easily find all permutations for sequence . The pseudocode below gives one approach to recursively solving this problem. Given an input string sequence : ●Base case: ○if sequence is a single character, there’s only one way to order it ■return a singleton list containing sequence ●Recursive case: ○suppose we have a method that can give us a list of all permutations of all but the first character
# in sequence (Hint: think recursion) ○then the permutations of all characters in sequence would be all the different ways we can insert the first character into each permutation of the remaining characters ■example: if our word was ‘bust’, we hold out the character ‘b’ and get the list [‘ust’, ‘sut’, ‘stu’, ‘uts’, ‘tus’, ‘tsu’] ●then ‘ust’ gives us: ‘b ust’, ‘ub st’, ‘us b t’, ‘ust b ’ ●‘sut’ gives us: ‘b sut’, ‘s b ut’, ‘su b t’, ‘sut b ’ ●and so on …
def get_permutations(sequence):
    """
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    """
    # base case -> if single character, just return itself
    # if 2 characters, return itself and reverse
    # subsequent cases -> take first character and hold, and insert into all permutations of remaining characters
    # for the subsequent cases, can use a loop - for each permutation, insert the first character into all possible positions

    # base case
    if len(sequence) == 1:
        return [sequence]
    else:
        # recursive case
        first_char = sequence[0]
        # get all permutations of all but the first character
        permutations = get_permutations(sequence[1:])
        # to store all permutations
        new_permutations = []
        # for loop to insert the first character into all possible positions
        for permutation in permutations:
            # need to +1 to include the last position
            for i in range(len(permutation) + 1):
                new_permutations.append(permutation[:i] + first_char + permutation[i:])
        return new_permutations


if __name__ == "__main__":
    #    #EXAMPLE
    example_input = "abc"
    print("Input:", example_input)
    print("Expected Output:", ["abc", "acb", "bac", "bca", "cab", "cba"])
    print("Actual Output:", get_permutations(example_input))

#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a
#    sequence of length n)

# pass #delete this line and replace with your code here
