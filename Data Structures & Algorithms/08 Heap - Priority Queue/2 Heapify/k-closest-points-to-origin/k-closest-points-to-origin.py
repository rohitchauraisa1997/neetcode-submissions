"""
K Closest Points to Origin (NeetCode)
=====================================

You are given an 2-D array points where points[i] = [xi, yi] represents the
coordinates of a point on an X-Y axis plane. You are also given an integer k.

Return the k closest points to the origin (0, 0).

The distance between two points is defined as the Euclidean distance
(sqrt((x1 - x2)^2 + (y1 - y2)^2)).

You may return the answer in any order.

Example 1:
    Input:  points = [[0,2],[2,2]], k = 1
    Output: [[0,2]]
    Explanation: The distance between (0, 2) and the origin (0, 0) is 2.
    The distance between (2, 2) and the origin is sqrt(2^2 + 2^2) = 2.82842.
    So the closest point to the origin is (0, 2).

Example 2:
    Input:  points = [[0,2],[2,0],[2,2]], k = 2
    Output: [[0,2],[2,0]]
    Explanation: The output [[2,0],[0,2]] would also be accepted.

Constraints:
    1 <= k <= points.length <= 1000
    -100 <= points[i][0], points[i][1] <= 100
"""

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []

        min_heap = []
        for x, y in points:
            # skip sqrt: comparing x²+y² gives the same order as true distance
            dist = (x**2) + (y**2)
            # tuple: heap orders by first element (dist), then x, y for ties
            min_heap.append((dist, x, y))

        # 📌 heapq.heapify(list) → turns list into a min-heap IN-PLACE, O(n)
        heapq.heapify(min_heap)

        while k > 0:
            # 📌 heapq.heappop(heap) → removes & returns smallest, O(log n)
            dist, x, y = heapq.heappop(min_heap)
            res.append([x, y])
            k -= 1

        return res