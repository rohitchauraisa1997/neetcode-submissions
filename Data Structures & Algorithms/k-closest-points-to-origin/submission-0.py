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