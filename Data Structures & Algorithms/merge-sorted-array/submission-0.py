class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Fill from the back. The end of nums1 is empty space, so nothing gets overwritten.
        # Common bug: merging from the front overwrites nums1 values not yet compared.
        last_index = m + n - 1

        # m and n are counts, so subtract 1 to get the last valid index in each list.
        m -= 1
        n -= 1

        while m >= 0 and n >= 0:
            # The larger of the two goes into the current last slot.
            # On equal values nums2 goes first. That's fine for ints;
            # for objects that must stay in order (stable), use >=.
            if nums1[m] > nums2[n]:
                nums1[last_index] = nums1[m]
                m -= 1
            else:
                nums1[last_index] = nums2[n]
                n -= 1
            last_index -= 1

        # Copy whatever is left in nums2. This also covers m == 0 (nums1 started empty).
        # No loop is needed for nums1: any values left there are already in the right place.
        # Common bug: adding that loop anyway, or forgetting this one.
        while n >= 0:
            nums1[last_index] = nums2[n]
            last_index -= 1
            n -= 1

        # Common bug: returning nums1 or building a new list. The task wants nums1 changed in place.

# Time: O(m + n). Space: O(1).