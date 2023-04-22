# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 12:13:13 2016

@author: ericgrimson
"""


def bisect_search2(L, e):
    """
    Takes a sorted list L and an element e
    Returns True if e is in L and False otherwise
    """

    def bisect_search_helper(L, e, low, high):
        """
        Takes in 4 arguments, a sorted list L, an element e, and low/high which are indexes
        Returns True if e is in L and False otherwise
        """
        # so for visualisation, the process is:
        # first case low1 ============================== guess1 ================================ high1
        # if mid > e, low1 ============guess2============ high2 = guess1 ========================= high1
        # if mid < e, low1 ======================== low2 = guess1 =============guess2============ high1
        # rinse and repeat...

        print("low: " + str(low) + "; high: " + str(high))  # added to visualize
        if high == low:
            # this will return True if L[low] == e and False otherwise
            return L[low] == e
        # if high != low, then there is more than one element in the list, so calculate the midpoint
        mid = (low + high) // 2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid:  # nothing left to search
                return False
            else:
                # this is case where mid > e
                return bisect_search_helper(L, e, low, mid - 1)
        else:
            # this is case where mid < e
            return bisect_search_helper(L, e, mid + 1, high)

    if len(L) == 0:
        return False
    else:
        return bisect_search_helper(L, e, 0, len(L) - 1)


testList = []
for i in range(100):
    testList.append(i)

print(bisect_search2(testList, 76))


def genSubsets(L):
    """
    Generates the power set of L, a list. Assumes L is a list of unique sorted elements.
    """
    if len(L) == 0:
        return [[]]  # list of empty list
    smaller = genSubsets(L[:-1])  # all subsets without last element
    extra = L[-1:]  # create a list of just last element
    new = []
    for small in smaller:
        new.append(
            small + extra
        )  # for all smaller solutions, add one with last element
    return smaller + new  # combine those with last element and those without


testSet = [1, 2, 3, 4]
print(genSubsets(testSet))
print(genSubsets([1, 2]))
