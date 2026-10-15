# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value

class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.quickSortHelper(pairs, 0, len(pairs) - 1)
        return pairs  # sorted in-place

    def quickSortHelper(self, arr, start, end):
        # base case: 0 or 1 element
        if end - start + 1 <= 1:
            return

        pivot = arr[end]  # pivot = rightmost
        left = start      # next slot for an element < pivot

        # move everything < pivot to the left side
        for i in range(start, end):  # excludes end (the pivot)
            if arr[i].key < pivot.key:  # strict < keeps equal keys in order (but QS still isn't stable overall)
                temp = arr[i]
                arr[i] = arr[left]
                arr[left] = temp
                left += 1

        # put pivot in its final position
        arr[end] = arr[left]
        arr[left] = pivot

        # recurse on both sides, skipping pivot (already placed)
        self.quickSortHelper(arr, start, left - 1)
        self.quickSortHelper(arr, left + 1, end)