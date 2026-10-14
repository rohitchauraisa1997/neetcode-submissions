"""
A non-empty array A consisting of N integers is given. A pair of integers (P, Q), such that 0 ≤ P < Q < N, is called a slice of array A (notice that the slice contains at least two elements). The average of a slice (P, Q) is the sum of A[P] + A[P + 1] + ... + A[Q] divided by the length of the slice. To be precise, the average equals (A[P] + A[P + 1] + ... + A[Q]) / (Q − P + 1).

For example, array A such that:

    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8
contains the following example slices:

slice (1, 2), whose average is (2 + 2) / 2 = 2;
slice (3, 4), whose average is (5 + 1) / 2 = 3;
slice (1, 4), whose average is (2 + 2 + 5 + 1) / 4 = 2.5.
The goal is to find the starting position of a slice whose average is minimal.

Write a function:

def solution(A)

that, given a non-empty array A consisting of N integers, returns the starting position of the slice with the minimal average. If there is more than one slice with a minimal average, you should return the smallest starting position of such a slice.

For example, given array A such that:

    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8
the function should return 1, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [2..100,000];
each element of array A is an integer within the range [−10,000..10,000].
"""

def solutionBrute(arr):
    min_sum_avg = float('inf')
    min_sum_start = 0

    for l in range(0, len(arr)):
        for r in range(l+1, len(arr)):
            new_avg = sum(arr[l:r+1])/(r-l+1)
            if new_avg < min_sum_avg:
                min_sum_start = l
                min_sum_avg = new_avg
    
    return min_sum_start

def solution(A):
    # KEY MATH FACT: the min-average slice always has length 2 or 3.
    # Why: a slice of length >= 4 can be split into smaller slices, each of length >= 2.
    #   The average of a whole is never less than the smallest average of its parts.
    #   (If you split into parts with averages a and b, the whole lies between a and b.)
    #   So a part's average is <= the whole's. Keep splitting and you end up at length 2 or 3.
    #   Length 3 can't be split into slices of length >= 2, so it has to be checked too.
    n = len(A)
    min_avg = (A[0] + A[1]) / 2
    min_start = 0

    for i in range(n - 1):
        # Length-2 slice starting at i
        avg2 = (A[i] + A[i + 1]) / 2
        if avg2 < min_avg:
            min_avg = avg2
            min_start = i

        # Length-3 slice starting at i
        # ⚠️ Bounds check: a 3-slice needs i+2 < n
        if i + 2 < n:
            avg3 = (A[i] + A[i + 1] + A[i + 2]) / 3
            if avg3 < min_avg:
                min_avg = avg3
                min_start = i

    # ⚠️ Strict < plus a left-to-right scan returns the smallest start on ties
    return min_start

# Time: O(N), Space: O(1)

