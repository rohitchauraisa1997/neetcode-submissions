"""
Koko Eating Bananas (NeetCode)
==============================

You are given an integer array piles where piles[i] is the number of bananas in
the ith pile. You are also given an integer h, which represents the number of
hours you have to eat all the bananas.

You may decide your bananas-per-hour eating rate of k. Each hour, you may
choose a pile of bananas and eat k bananas from that pile. If the pile has
less than k bananas, you may finish eating the pile but you can not eat from
another pile in the same hour.

Return the minimum integer k such that you can eat all the bananas within h
hours.

Example 1:
    Input:  piles = [1,4,3,2], h = 9
    Output: 2
    Explanation: With an eating rate of 2, you can eat the bananas in 6 hours.
    With an eating rate of 1, you would need 10 hours to eat all the bananas
    (which exceeds h=9), thus the minimum eating rate is 2.

Example 2:
    Input:  piles = [25,10,23,4], h = 4
    Output: 25

Constraints:
    1 <= piles.length <= 1,000
    piles.length <= h <= 1,000,000
    1 <= piles[i] <= 1,000,000,000
"""

class Solution:
    def minEatingSpeed(self, piles: List[int], hoursToFinishIn: int) -> int:
        # Binary search on the ANSWER (eating speed), not on the array
        leftSpeed = 1               # slowest possible speed
        rightSpeed = max(piles)     # fastest needed: every pile done in 1 hour
        result = rightSpeed            # max(piles) always works, so it's a safe default

        while leftSpeed <= rightSpeed:
            midSpeed = (leftSpeed + rightSpeed) // 2   # candidate speed

            # hours needed at this speed (one pile per hour, leftovers don't carry over)
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / midSpeed)   # partial pile still costs a full hour

            if hours <= hoursToFinishIn:
                # midSpeed works → record it, then try slower
                result = min(result, midSpeed)
                rightSpeed = midSpeed - 1
            else:
                # too slow → need a faster speed
                leftSpeed = midSpeed + 1

        return result