"""
MaxCounters (Codility)

You are given N counters, initially set to 0, and you have two possible
operations on them:

    increase(X) - counter X is increased by 1,
    max counter - all counters are set to the maximum value of any counter.

A non-empty array A of M integers is given. This array represents consecutive
operations:

    if A[K] = X, such that 1 <= X <= N, then operation K is increase(X),
    if A[K] = N + 1 then operation K is max counter.

For example, given integer N = 5 and array A such that:

    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4
the values of the counters after each consecutive operation will be:

    (0, 0, 1, 0, 0)
    (0, 0, 1, 1, 0)
    (0, 0, 1, 2, 0)
    (2, 2, 2, 2, 2)
    (3, 2, 2, 2, 2)
    (3, 2, 2, 3, 2)
    (3, 2, 2, 4, 2)
The goal is to calculate the value of every counter after all operations.

Write a function:

def solution(N, A)

that, given an integer N and a non-empty array A consisting of M integers, returns a sequence of integers representing the values of the counters.

Result array should be returned as an array of integers.

For example, given:

    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4
the function should return [3, 2, 2, 4, 2], as explained above.

Write an efficient algorithm for the following assumptions:

N and M are integers within the range [1..100,000];
each element of array A is an integer within the range [1..N + 1].
"""

# ****PERFORMANCE FAILS (77%)****
def solution(counter, array):
    # 1-indexed counters (ops use values 1..N), slot 0 unused
    counter_array = [0] * (counter + 1)
    max_counter_now = 0  # running max across all counters

    for counter_array_index in array:
        if counter_array_index == counter + 1:
            # "max counter" op: set ALL counters to current max
            # ⚠️ O(N) rebuild every time → O(N·M) worst case → TLE
            counter_array = [max_counter_now] * (counter + 1)
        else:
            # "increase" op: bump that one counter
            counter_array[counter_array_index] += 1
            # track max so the next "max counter" op knows what to set
            max_counter_now = max(max_counter_now, counter_array[counter_array_index])

    return counter_array[1:]  # drop unused slot 0


def solution(N, A):
    MAX_COUNTER_OP = N + 1

    counters = [0] * (N + 1)   # 1-indexed; counters[0] unused
    current_max = 0            # highest value any counter has reached
    pending_min = 0            # every counter is at least this (set by last max-counter op, applied lazily)

    for op in A:
        if op == MAX_COUNTER_OP:
            # Don't rebuild the array (O(N)); just record the new minimum (O(1))
            pending_min = current_max
            continue

        # op is the counter to increment:
        # first catch it up to pending_min (if it missed a max op), then +1
        counters[op] = max(counters[op], pending_min) + 1
        current_max = max(current_max, counters[op])

    # Final cleanup: counters not touched since the last max op still hold stale values
    # e.g. stored [3, 0, 1, 4, 0] with pending_min=2 → [3, 2, 2, 4, 2]
    result = []
    for value in counters[1:]:   # skip unused slot 0
        result.append(max(value, pending_min))
    return result