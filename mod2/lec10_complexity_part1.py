# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 11:27:54 2016

@author: ericgrimson
"""


def linear_search(L, e):
    """
    function takes in a list L and an element e
    returns True if e is in L and False otherwise
    """
    found = False
    for i in range(len(L)):
        if e == L[i]:
            found = True
    return found


testList = [1, 3, 4, 5, 9, 18, 27]
print(linear_search(testList, 9))
print(linear_search(testList, 100))


def search(L, e):
    """
    assume L is a list and the elements of L are in ascending order
    returns True if e is in L and False otherwise
    as long as L[i] > e, we know e is not in L
    """
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False


print(search(testList, 9))
print(search(testList, 100))


def isSubset(L1, L2):
    """
    takes in 2 list L1 and L2 and check if L1 is a subset of L2
    """
    for e1 in L1:
        matched = False
        for e2 in L2:
            if e1 == e2:
                matched = True
                break
        # as long as e1 is not in L2, matched will be False, so return False
        if not matched:
            return False
    # if all elements in L1 are in L2, return True
    return True


testSet = [1, 2, 3, 4, 5]
testSet1 = [1, 5, 3]
testSet2 = [1, 6]
testSet3 = [1, 6, 1]

print(isSubset(testSet1, testSet))
print(isSubset(testSet2, testSet))


def intersect(L1, L2):
    """
    takes in 2 list L1 and L2 and returns a list of elements that are in both L1 and L2
    """
    tmp = []
    for e1 in L1:
        for e2 in L2:
            if e1 == e2:
                tmp.append(e1)
    # the above process might include duplicate elements, so we need to remove them
    res = []
    for e in tmp:
        if not (e in res):
            res.append(e)
    return res


print(intersect(testSet1, testSet2))
print(intersect(testSet1, testSet))
print(intersect(testSet3, testSet))
