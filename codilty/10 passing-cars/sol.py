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
    # BRUTE FORCE: O(N²) time, O(pairs) space. Correct, but TLEs on large N.
    #
    # My thinking:
    #   A passing pair is (P, Q) with P < Q, arr[P] == 0 (east), arr[Q] == 1 (west).
    #   So for every 0 at index l, scan everything to its right and
    #   record each 1 as a pair (l, r). The answer is the number of pairs.
    res = []

    for l in range(len(arr)):
        if arr[l] == 0:
            # Eastbound car: pair it with every westbound car to its right
            for r in range(l + 1, len(arr)):  # l+1 enforces P < Q
                if arr[r] == 1:
                    res.append((l, r))
        else:
            # Intent: "this is a 1, it can't start a pair, so skip it and move on".
            # ⚠️ USELESS LINE. `for l in range(...)` rebinds l to the next value at
            #    the start of every iteration, so this increment is overwritten
            #    immediately. Changing the loop variable doesn't affect range().
            #    (In Go's `for l := 0; l < n; l++`, l++ inside WOULD skip an index.)
            # Why the code still works: skipping a 1 and moving to the next index
            # is exactly what the for loop does anyway. The else branch could be
            # deleted with no change in behavior.
            l += 1

    # ⚠️ Storing every pair is wasteful. Only the count is needed, so `count += 1` would do.
    # ⚠️ Missing requirement: return -1 if the count exceeds 1,000,000,000.
    return len(res)

# Why it TLEs: in the worst case (half 0s followed by half 1s) that's ~N²/4 checks.
#    N = 100,000 → ~2.5 billion operations.
#
# Optimal O(N) idea (see the other version): flip the view. Instead of each 0
# looking right for 1s, each 1 looks LEFT. It pairs with every 0 seen so far,
# so keep a running `east` count and do `pairs += east` whenever you hit a 1.

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