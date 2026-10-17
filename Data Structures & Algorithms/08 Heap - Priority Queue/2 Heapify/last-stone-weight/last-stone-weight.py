"""
Last Stone Weight (NeetCode)
============================

You are given an array of integers stones where stones[i] represents the weight
of the ith stone.

We want to run a simulation on the stones as follows:
    - At each step we choose the two heaviest stones, with weight x and y and
      smash them together.
    - If x == y, both stones are destroyed.
    - If x < y, the stone of weight x is destroyed, and the stone of weight y
      has new weight y - x.

Continue the simulation until there is no more than one stone remaining.

Return the weight of the last remaining stone or return 0 if none remain.

Example 1:
    Input:  stones = [2,3,6,2,4]
    Output: 1
    Explanation:
    We smash 6 and 4 and are left with a 2, so the array becomes [2,3,2,2].
    We smash 3 and 2 and are left with a 1, so the array becomes [1,2,2].
    We smash 2 and 2, so the array becomes [1].

Example 2:
    Input:  stones = [1,2]
    Output: 1

Constraints:
    1 <= stones.length <= 20
    1 <= stones[i] <= 100

Max heap in Python: store -weight in heapq's min heap. Keep EVERY value in the
heap negative: negate what you push back too, or the heap mixes signs and pops
the wrong stones (passes the examples, fails ~45% of random inputs).
"""

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Python only has a MIN heap: store every weight as -weight,
        # so the heaviest stone (most negative) is at the root
        for i in range(len(stones)):
            stones[i] = -1 * stones[i]

        maxHeap = stones
        heapq.heapify(maxHeap)          # in place, O(n)

        while len(maxHeap)>1:
            # take the two heaviest (flip the sign back to get real weights)
            firstWeight = -1* heapq.heappop(maxHeap)    # heaviest
            secondWeight = -1* heapq.heappop(maxHeap)   # second heaviest

            # equal stones destroy each other: nothing goes back
            if firstWeight != secondWeight:
                weightAfterCollision = firstWeight-secondWeight
                # ⚠️ negate again before pushing, like every other stone in the heap
                heapq.heappush(maxHeap, -1 * weightAfterCollision)

        # ⚠️ flip the sign back; all stones destroyed -> 0
        return -1 * maxHeap[0] if maxHeap else 0

# Time: O(n log n), each collision is a pop/pop/push of O(log n). Space: O(1) extra (heap is the input list)