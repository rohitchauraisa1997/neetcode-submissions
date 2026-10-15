"""
Quick Sort (NeetCode)
=====================

Implement Quick Sort.

Quick Sort is a divide-and-conquer algorithm. It picks a pivot element,
partitions the list so that elements smaller than the pivot are on its left and
the rest are on its right, then recursively sorts both sides.

Objective:
    Given a list of key-value pairs, sort the list by key using Quick Sort.
    Use the right-most element as the pivot. Return the sorted list.

Input:
    pairs - a list of key-value pairs, where each key-value has an integer key
    and a string value. (0 <= pairs.length <= 100).

Example 1:
    Input:  pairs = [(5, "apple"), (2, "banana"), (9, "cherry"), (1, "date"),
                     (9, "elderberry")]
    Output: [(1, "date"), (2, "banana"), (5, "apple"), (9, "elderberry"),
             (9, "cherry")]

Example 2:
    Input:  pairs = [(3, "cat"), (2, "dog"), (3, "bird")]
    Output: [(2, "dog"), (3, "bird"), (3, "cat")]

    Note: Quick Sort is NOT stable. Equal keys can swap order (cherry and
    elderberry above, cat and bird here). Merge Sort keeps them in order.

Explanation (one partition of keys [5, 2, 9, 1, 6], pivot = 6):

    left = 0, scan i = 0..3, swap arr[i] into arr[left] when arr[i] < pivot

      i=0: 5 < 6  swap(0,0), left=1    [5, 2, 9, 1, 6]
      i=1: 2 < 6  swap(1,1), left=2    [5, 2, 9, 1, 6]
      i=2: 9      skip                 [5, 2, 9, 1, 6]
      i=3: 1 < 6  swap(3,2), left=3    [5, 2, 1, 9, 6]

    put pivot at left:                 [5, 2, 1, 6, 9]
                                                 ^ final position
    recurse on [5, 2, 1] and [9]

Time: O(n log n) average, O(n^2) worst (already sorted input + right-most
pivot: every partition only peels off one element). Space: O(log n) average
recursion, O(n) worst.
"""

# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value

class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.quickSortHelper(pairs, 0, len(pairs) - 1)
        return pairs  # sorted in-place

    def quickSortHelper(self, arr, start, end):
        # base case: 0 or 1 element
        if end - start + 1 <= 1:
            return

        pivot = arr[end]  # pivot = rightmost
        left = start      # next slot for an element < pivot

        # move everything < pivot to the left side
        for i in range(start, end):  # excludes end (the pivot)
            if arr[i].key < pivot.key:  # strict < keeps equal keys in order (but QS still isn't stable overall)
                temp = arr[i]
                arr[i] = arr[left]
                arr[left] = temp
                left += 1

        # put pivot in its final position
        arr[end] = arr[left]
        arr[left] = pivot

        # recurse on both sides, skipping pivot (already placed)
        self.quickSortHelper(arr, start, left - 1)
        self.quickSortHelper(arr, left + 1, end)