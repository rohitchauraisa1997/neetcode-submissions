class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # traverse right-to-left,
        # tracking the max of everything seen so far

        max_right = -1

        for i in range(len(arr)-1, -1, -1):
            # stage the next max BEFORE overwriting arr[i],
            # otherwise we lose arr[i]'s original value
            new_max = max(max_right, arr[i])
            arr[i] = max_right
            max_right = new_max

        return arr