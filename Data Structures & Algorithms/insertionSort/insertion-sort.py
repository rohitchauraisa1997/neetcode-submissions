"""
Insertion Sort (NeetCode)
=========================

Implement Insertion Sort.

Insertion Sort is a simple sorting algorithm that builds the sorted list one
element at a time, from left to right. It works by repeatedly taking an element
from the unsorted portion and inserting it into its correct position in the
sorted portion of the list.

Objective:
    Given a list of key-value pairs, sort the list by key using Insertion Sort.
    Return a list of lists showing the state of the array after each insertion.
    If two key-value pairs have the same key, maintain their relative order in
    the sorted list.

Input:
    pairs - a list of key-value pairs, where each key-value has an integer key
    and a string value. (0 <= pairs.length <= 100).

Example 1:
    Input:  pairs = [(5, "apple"), (2, "banana"), (9, "cherry")]
    Output: [[(5, "apple"), (2, "banana"), (9, "cherry")],
             [(2, "banana"), (5, "apple"), (9, "cherry")],
             [(2, "banana"), (5, "apple"), (9, "cherry")]]
    Note: The state of the array after the first insertion (index 0) is the
    original list.

Example 2:
    Input:  pairs = [(3, "cat"), (3, "bird"), (2, "dog")]
    Output: [[(3, "cat"), (3, "bird"), (2, "dog")],
             [(3, "cat"), (3, "bird"), (2, "dog")],
             [(2, "dog"), (3, "cat"), (3, "bird")]]
"""

# PROBLEM: Insertion Sort (NeetCode) - sort pairs by key, return list state after each insertion.
# e.g. [(5,a),(2,b),(9,c)] -> [[5a,2b,9c], [2b,5a,9c], [2b,5a,9c]]
# IDEA: pairs[0..i-1] stays sorted; swap pairs[i] left until it's in place.

class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        n = len(pairs)
        res = []

        for i in range(n):
            j = i-1

            # strict '>' keeps equal keys in order -> stable
            # j>=0 to make sure we dont get index out of range error
            while j>=0 and pairs[j].key > pairs[j+1].key:
                temp = pairs[j+1]
                pairs[j+1] = pairs[j]
                pairs[j] = temp
                j -= 1

            res.append(pairs[:])    # copy; appending `pairs` stores the same list n times
        return res

# Time: O(n^2) worst, O(n) if already sorted | Space: O(1) in-place