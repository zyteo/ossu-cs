# my fix: create a copy of L, then clear L and append the elements in reverse order
def rev_list_fix(L):
    """
    input: L, a list
    Modifies L such that its elements are in reverse order
    returns: nothing
    """
    L_copy = L[:]
    for i in range(len(L_copy)):
        L[i] = L_copy[len(L_copy)-i-1]

        
L = [1,2,3,4]
# rev_list(L)
rev_list_fix(L)
print(L)