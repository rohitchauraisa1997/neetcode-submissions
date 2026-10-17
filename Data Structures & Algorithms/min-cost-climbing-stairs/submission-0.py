class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # bottom up approach but from the END
        # [10,15,20] 0 
        # 0 here represents the cost it would be to reach the roof
        # and since it itself is the roof cost is 0

        cost.append(0) # increases len by 1
        # len(cost)-3 is the 2nd last step of the original array, so we start there:
        # len(cost)-2 (the step just before the roof) is already final, one jump reaches the roof,
        # and len(cost)-1 is the roof itself (cost 0).
        for i in range(len(cost)-3, -1, -1):
            cost[i] = cost[i] + min(cost[i+1], cost[i+2])
        
        return min(cost[0], cost[1])