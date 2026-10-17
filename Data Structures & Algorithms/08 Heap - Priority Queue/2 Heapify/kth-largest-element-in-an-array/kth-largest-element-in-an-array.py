"""
Kth Largest Element in an Array (NeetCode)
==========================================

Given an unsorted array of integers nums and an integer k, return the kth
largest element in the array.

By kth largest element, we mean the kth largest element in the sorted order,
not the kth distinct element.

Follow-up: Can you solve it without sorting?

Example 1:
    Input:  nums = [2,3,1,5,4], k = 2
    Output: 4

Example 2:
    Input:  nums = [2,3,1,1,5,5,4], k = 3
    Output: 4

Constraints:
    1 <= k <= nums.length <= 10000
    -1000 <= nums[i] <= 1000

Two heap approaches:
    - max heap of everything (below): negate, heapify, pop k-1 times.
      O(n + k log n) time, the whole array in the heap.
    - min heap of only the k largest (like Kth Largest in a Stream):
      root = answer. O(n log k) time, O(k) space:
          minHeap = nums[:k]; heapq.heapify(minHeap)
          for num in nums[k:]:
              if num > minHeap[0]: heapq.heapreplace(minHeap, num)
          return minHeap[0]
"""

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