# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value

class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        # Common bug: forgetting `return` here, so the caller gets None.
        return self.mergeSortHelper(pairs, 0, len(pairs) - 1)

    def mergeSortHelper(self, arr, start, end):
        # `end` is inclusive. Base case: 0 or 1 element is already sorted.
        # Without it the recursion never stops.
        if end - start + 1 <= 1:
            return arr

        # Python ints can't overflow. In Go, Java or C++ write start + (end-start)//2.
        mid = (start + end) // 2

        # Split as [start..mid] and [mid+1..end].
        # Splitting as [start..mid-1] and [mid..end] recurses forever on 2 elements.
        self.mergeSortHelper(arr, start, mid)
        self.mergeSortHelper(arr, mid + 1, end)

        self.merge(arr, start, end)
        return arr

    def merge(self, arr, start, end):
        # `mid` must be calculated exactly as in mergeSortHelper, or the halves won't line up.
        # Passing mid in as an argument is safer.
        mid = (start + end) // 2

        # Copy both halves first. Merging back into arr would otherwise overwrite
        # values not yet compared. Slice ends are exclusive, hence the +1s.
        left = arr[start:mid + 1]
        right = arr[mid + 1:end + 1]

        i = j = 0
        k = start  # Common bug: starting k at 0 overwrites the wrong part of arr.

        while i < len(left) and j < len(right):
            # Use <=, not <. On equal keys it takes from the left half first,
            # which keeps equal keys in their original order (a stable sort).
            if left[i].key <= right[j].key:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # Copy whatever is left. Only one of these loops will run.
        # Common bug: reading arr[i] instead of left[i]. i and j are positions in
        # left and right, not in arr.
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

        return arr

# Time: O(n log n) in every case. Space: O(n) for the copied halves,
# plus O(log n) for the recursion stack.