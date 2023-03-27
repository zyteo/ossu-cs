def rev_list_fix(L):
    """
    input: L, a list
    Modifies L such that its elements are in reverse order
    returns: nothing
    """
    L_copy = L[:]
    L = []
    for i in range(len(L_copy)):
        L.append(L_copy[len(L_copy)-i-1])
    print(L)
        
L = [1,2,3,4]
rev_list_fix(L)
print(L)