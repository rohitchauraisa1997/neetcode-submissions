"""
An array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.
Your goal is to find that missing element.
Write a function:
def solution(A)
that, given an array A, returns the value of the missing element.
For example, given array A such that:
  A[0] = 2
  A[1] = 3
  A[2] = 1
  A[3] = 5
the function should return 4, as it is the missing element.
Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
the elements of A are all distinct;
each element of array A is an integer within the range [1..(N + 1)].
"""

def solution(arr):
    n = len(arr)
    element_dict = {}

    # n+2, not n+1: range is 1..N+1 inclusive (N+1 values)
    for i in range(1, n+2):
        element_dict[i] = False

    # mark seen
    for element in arr:
        element_dict[element] = True

    # the one still False is missing; N=0 -> {1: False} -> returns 1
    for key, value in element_dict.items():
        if value == False:          # `not value` is more idiomatic
            return key
