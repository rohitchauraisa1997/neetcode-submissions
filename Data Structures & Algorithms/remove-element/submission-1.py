class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0

        # using two pointers
        # i iterates through the array
        # k keeps track of where to place the "non-value" 
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[k] = nums[i]
                k+=1
        return k