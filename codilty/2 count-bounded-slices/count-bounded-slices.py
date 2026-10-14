"""
CountBoundedSlices (Codility)
=============================

An integer K and a non-empty array A consisting of N integers are given.

A pair of integers (P, Q), such that 0 <= P <= Q < N, is called a slice of
array A.

A bounded slice is a slice in which the difference between the maximum and
minimum values in the slice is less than or equal to K. More precisely it is a
slice, such that max(A[P], A[P + 1], ..., A[Q]) - min(A[P], A[P + 1], ..., A[Q])
<= K.

The goal is to calculate the number of bounded slices.

For example, consider K = 2 and array A such that:

    A[0] = 3
    A[1] = 5
    A[2] = 7
    A[3] = 6
    A[4] = 3

There are exactly nine bounded slices: (0, 0), (0, 1), (1, 1), (1, 2), (1, 3),
(2, 2), (2, 3), (3, 3), (4, 4).

Write a function:

def solution(K, A)

that, given an integer K and a non-empty array A of N integers, returns the
number of bounded slices of array A.

If the number of bounded slices is greater than 1,000,000,000, the function
should return 1,000,000,000.

For example, given K = 2 and array A as above, the function should return 9,
as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
K is an integer within the range [0..1,000,000,000];
each element of array A is an integer within the range
[-1,000,000,000..1,000,000,000].
"""

# ***** PERFORMANCE FAILS ****

def solution(K, arr):
    arr_len = len(arr)
    count = 0
    # max_val = arr[0]
    # min_val = arr[0]

    for i in range(arr_len):
        max_val = arr[i]
        min_val = arr[i]

        for j in range(i, arr_len):
            max_val = max(max_val, arr[j])
            min_val = min(min_val, arr[j])
            
            diff = max_val-min_val
            if diff <= K:
                count += 1
            else: 
              break

    return count
