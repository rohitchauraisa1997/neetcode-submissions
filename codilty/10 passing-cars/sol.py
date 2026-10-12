"""
A non-empty array A consisting of N integers is given. The consecutive elements of array A represent consecutive cars on a road.

Array A contains only 0s and/or 1s:

0 represents a car traveling east,
1 represents a car traveling west.
The goal is to count passing cars. We say that a pair of cars (P, Q), where 0 ≤ P < Q < N, is passing when P is traveling to the east and Q is traveling to the west.

For example, consider array A such that:

  A[0] = 0
  A[1] = 1
  A[2] = 0
  A[3] = 1
  A[4] = 1
We have five pairs of passing cars: (0, 1), (0, 3), (0, 4), (2, 3), (2, 4).

Write a function:

def solution(A)

that, given a non-empty array A of N integers, returns the number of pairs of passing cars.

The function should return −1 if the number of pairs of passing cars exceeds 1,000,000,000.

For example, given:

  A[0] = 0
  A[1] = 1
  A[2] = 0
  A[3] = 1
  A[4] = 1
the function should return 5, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer that can have one of the following values: 0, 1.
"""

def solution(arr):
    res = []
    for l in range(len(arr)):
        if arr[l] == 0:
            for r in range(l+1,len(arr)):
                if arr[r] == 1:
                    res.append((l,r))
        else:
            l += 1
    return len(res)


def solution(A):
    # Number of eastbound cars (0s) seen so far.
    # Every one of them is behind (to the left of) the current position,
    # so any westbound car we meet from here on will pass all of them.
    east = 0

    # Total number of passing pairs found so far.
    pairs = 0

    for car in A:
        if car == 0:
            # Eastbound car: it can't pass anything to its left (pairs need P < Q
            # with P going east), but it WILL pass every westbound car to its right.
            # Record it so future 1s can count it.
            east += 1
        else:
            # Westbound car: it forms a pair with every eastbound car before it.
            # That's exactly `east` new pairs, no need to look back at them individually.
            pairs += east

            # Problem requires -1 once the count exceeds 1e9.
            # Checking here lets us stop early instead of finishing the loop.
            if pairs > 1_000_000_000:
                return -1

    return pairs