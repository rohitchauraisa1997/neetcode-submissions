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