class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # nums_len = len(nums)
        # new_nums = [0]*2*nums_len

        # for i in range(nums_len):
        #     # first copy
        #     new_nums[i] = nums[i]
        #     # second copy, offset by nums_len
        #     new_nums[i+nums_len] = nums[i]
        
        # return new_nums


        # NEETCODE easier soln
        ans = []
        for _ in range(2):
            for i in range(len(nums)):
                ans.append(nums[i])
        
        return ans