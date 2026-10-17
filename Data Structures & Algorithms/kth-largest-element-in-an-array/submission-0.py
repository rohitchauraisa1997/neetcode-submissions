class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Python only has a MIN heap: negate every number so the
        # largest one becomes the smallest and sits at the root (a max heap)
        for i in range(len(nums)):
            nums[i] = -1*nums[i]

        minHeap = nums                  # holds negatives, so it behaves as a MAX heap
        heapq.heapify(minHeap)          # in place, O(n)

        # pop the k-1 largest; whatever is at the root next is the kth largest
        while k>1:
            heapq.heappop(minHeap)
            k -= 1

        # flip the sign back to get the real number
        return -1*heapq.heappop(minHeap)

# Time: O(n + k log n): heapify O(n), then k pops of O(log n). Space: O(1) extra (heap is the input list)