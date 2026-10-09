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