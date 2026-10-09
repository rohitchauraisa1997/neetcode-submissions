class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = [0]*3

        for num in nums:
            counter[num] += 1

        index = 0
        for i in range(3):
            while counter[i]>0:
                nums[index] = i 
                index += 1
                counter[i] -= 1