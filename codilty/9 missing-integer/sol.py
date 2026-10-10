"""
Task description

keyboard_arrow_left
This is a demo task.

Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
"""

def solution(array):
    numsSet = set()
    for num in array:
        numsSet.add(num)

    for num in range(1,1000000):
        if num not in numsSet:
            return num


def solution2(A):
    # MissingInteger / LC 41 First Missing Positive. O(N) time, O(N) space.
    #
    # Why the answer is always in [1, N+1], where N = len(A):
    #   - N elements can cover at most N distinct positives, i.e. at most 1..N.
    #   - If all of 1..N are present -> answer is N+1.
    #       e.g. [1..1000], N=1000 -> 1001
    #   - Otherwise something in 1..N is missing -> answer <= N.
    #       e.g. [1, 3, 6, 4, 1, 2], N=6 -> 5
    #   - An answer of N+2 would need 1..N+1 present = N+1 elements. Impossible.
    #   So values < 1 or > N never affect the answer, and the input range
    #   [-1e6, 1e6] is a distraction; only N matters.
    #
    # Edge cases: all negatives -> 1, duplicates, full 1..N -> N+1.
    s = set(A)
    for i in range(1, len(A) + 2):   # checks 1..N+1 (range end is exclusive)
        if i not in s:
            return i