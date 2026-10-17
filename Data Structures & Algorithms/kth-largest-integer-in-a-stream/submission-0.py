class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # min heap with K largest elements
        # this way the root of heap(smallest among them)
        # will always have kth largest element
        self.k = k
        self.minHeap = nums # self.minHeap = heapq.heapify(nums) WRONGGGGG
        # ⚠️ heapify works IN PLACE and returns None: don't assign its result
        # print(dir(heapq))
        heapq.heapify(self.minHeap)

        # keep only the k largest: pop the smallest until k remain
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)

        # one too many: drop the smallest, it can't be in the top k
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        # root = smallest of the k largest = kth largest
        return self.minHeap[0]

# Time: __init__ O(n log n) worst (heapify O(n) + up to n pops),
#       add O(log k). Space: O(k)