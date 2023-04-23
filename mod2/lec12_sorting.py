# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 09:21:39 2016

@author: ericgrimson
"""


def bubble_sort(L):
    """
    sorts a given list L using bubble sort
    compare 2 adjacent elements and swap if necessary
    """
    swap = False
    # this will run for a maximum of len(L) times
    while not swap:
        print("bubble sort: " + str(L))
        swap = True
        # compare 2 elements so range will just limit to len(L)-1
        # alternative would be range(0, len(L)-1)
        for j in range(1, len(L)):
            if L[j - 1] > L[j]:
                swap = False
                # swap elements
                temp = L[j]
                L[j] = L[j - 1]
                L[j - 1] = temp


testList = [1, 3, 5, 7, 2, 6, 25, 18, 13]

print("")
print(bubble_sort(testList))
print(testList)


def selection_sort(L):
    """
    sorts a given list L using selection sort
    find the smallest element and swap it with the first element
    """
    # start of the suffix
    suffixSt = 0
    # this will run for a maximum of len(L) times
    while suffixSt != len(L):
        print("selection sort: " + str(L))
        # the range will get smaller over each iteration
        for i in range(suffixSt, len(L)):
            if L[i] < L[suffixSt]:
                # swap the elements
                L[suffixSt], L[i] = L[i], L[suffixSt]
        suffixSt += 1


testList = [1, 3, 5, 7, 2, 6, 25, 18, 13]

print("")
print(selection_sort(testList))
print(testList)


def merge(left, right):
    """
    takes 2 sorted lists and
    merges the lists into a single sorted list
    """
    result = []
    i, j = 0, 0
    # i and j are the index of the left and right lists respectively
    while i < len(left) and j < len(right):
        # compare the elements of the left and right lists, append the smaller element
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # the remaining while loops is for when one list is empty, so just append the remaining elements
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    print("merge: " + str(left) + "&" + str(right) + " to " + str(result))
    return result


def merge_sort(L):
    """
    sorts a given list L using merge sort"""
    print("merge sort: " + str(L))
    if len(L) < 2:
        # base case - list is already sorted
        return L[:]
    else:
        # recursive case - split the list into 2 halves and merge sort each half
        middle = len(L) // 2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)


testList = [1, 3, 5, 7, 2, 6, 25, 18, 13]

print("")
print(merge_sort(testList))
