class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Counting sort: values are only 0, 1, 2 → count each
        counter = [0] * 3   # counter[v] = how many times v appears

        # Pass 1: count occurrences
        for num in nums:
            counter[num] += 1   # value doubles as index

        # Pass 2: overwrite nums in order 0s → 1s → 2s
        index = 0               # next write position in nums
        for i in range(3):
            while counter[i] > 0:
                nums[index] = i
                index += 1
                counter[i] -= 1