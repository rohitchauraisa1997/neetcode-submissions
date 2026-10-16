"""
Task description

keyboard_arrow_left
An integer M and a non-empty array A consisting of N non-negative integers are given. All integers in array A are less than or equal to M.

A pair of integers (P, Q), such that 0 ≤ P ≤ Q < N, is called a slice of array A. The slice consists of the elements A[P], A[P + 1], ..., A[Q]. A distinct slice is a slice consisting of only unique numbers. That is, no individual number occurs more than once in the slice.

For example, consider integer M = 6 and array A such that:

    A[0] = 3
    A[1] = 4
    A[2] = 5
    A[3] = 5
    A[4] = 2
There are exactly nine distinct slices: (0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2), (3, 3), (3, 4) and (4, 4).

The goal is to calculate the number of distinct slices.

Write a function:

def solution(M, A)

that, given an integer M and a non-empty array A consisting of N integers, returns the number of distinct slices.

If the number of distinct slices is greater than 1,000,000,000, the function should return 1,000,000,000.

For example, given integer M = 6 and array A such that:

    A[0] = 3
    A[1] = 4
    A[2] = 5
    A[3] = 5
    A[4] = 2
the function should return 9, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
M is an integer within the range [0..100,000];
each element of array A is an integer within the range [0..M].
"""

def solution(max_val, arr):
    # Brute force: for each start l, extend r until a duplicate appears.
    # O(N^2) is correct but fails perf; use a sliding window for O(N).
    res = []

    for l in range(len(arr)):
        new_set = set()            # values in the current slice arr[l..r]
        new_set.add(arr[l])
        res.append((l,l))          # a single element is always a valid slice
        for r in range(l+1, len(arr)):
            if arr[r] not in new_set:
                new_set.add(arr[r])
                res.append((l,r))  # record EVERY valid extension, not only at a dup
            else:
                break              # dup found: every longer slice from l is invalid too

    # print(res)
    return len(res)                # missing the 1e9 cap from the spec


def solution(M, array):
    # Sliding window: keep array[l..r] all-distinct. O(N).
    l = 0
    r = 0                   # redundant: the for loop sets r
    res = 0
    numSet = set()          # values in the current window

    for r in range(len(array)):          # r drives the loop; l only moves in the while
        while array[r] in numSet:        # check the NEW element (r), not array[l]
            numSet.remove(array[l])      # shrink from the left until the dup is gone
            l += 1
        numSet.add(array[r])

        # window [l..r] is distinct, so every slice ending at r is distinct:
        # starts l, l+1, ..., r  ->  r - l + 1 slices
        # (each slice is counted once, by its end index)
        res = res + r - l + 1

        if res > 1000000000:             # spec: cap at 1e9
            return 1000000000

    return res