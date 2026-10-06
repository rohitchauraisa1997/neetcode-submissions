# PROBLEM: Insertion Sort (NeetCode) - sort pairs by key, return list state after each insertion.
# e.g. [(5,a),(2,b),(9,c)] -> [[5a,2b,9c], [2b,5a,9c], [2b,5a,9c]]
# IDEA: pairs[0..i-1] stays sorted; swap pairs[i] left until it's in place.

class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        n = len(pairs)
        res = []

        for i in range(n):
            j = i-1

            # strict '>' keeps equal keys in order -> stable
            # j>=0 to make sure we dont get index out of range error
            while j>=0 and pairs[j].key > pairs[j+1].key:
                temp = pairs[j+1]
                pairs[j+1] = pairs[j]
                pairs[j] = temp
                j -= 1

            res.append(pairs[:])    # copy; appending `pairs` stores the same list n times
        return res

# Time: O(n^2) worst, O(n) if already sorted | Space: O(1) in-place