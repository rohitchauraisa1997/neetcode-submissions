class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # BOTTOM-UP DP, filled from the START
        # dp[i] = cheapest total to REACH step i (step n = the top)
        # you reach step i from i-1 (paying cost[i-1]) or from i-2 (paying cost[i-2])
        #   dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        n = len(cost)
        dp = [0]*(n+1)          # ⚠️ (n+1): one extra slot for the top; [0]*n+1 is an error
                                # dp[0] = dp[1] = 0: you may START on step 0 or 1 for free

        for i in range(2,n+1):  # ⚠️ n+1: the loop must fill dp[n], the top
            dp[i] = min((dp[i-1]+cost[i-1]),
                        (dp[i-2]+cost[i-2]))

        return dp[n]

    # DRY RUN: cost = [10, 15, 20], n = 3
    #   index : 0    1    2    3 (top)
    #   cost  : 10   15   20
    #   dp    : 0    0    .    .
    #   i=2: min(dp[1]+cost[1], dp[0]+cost[0]) = min(0+15, 0+10) = 10
    #   i=3: min(dp[2]+cost[2], dp[1]+cost[1]) = min(10+20, 0+15) = 15
    #   dp    : 0    0    10   15   -> 15 (start on step 1, pay 15, jump 2 to the top)
    #
    # DRY RUN: cost = [1, 2, 1, 2, 1, 1, 1], n = 7
    #   index : 0  1  2  3  4  5  6  7 (top)
    #   cost  : 1  2  1  2  1  1  1
    #   i=2: min(0+2, 0+1) = 1
    #   i=3: min(1+1, 0+2) = 2
    #   i=4: min(2+2, 1+1) = 2
    #   i=5: min(2+1, 2+2) = 3
    #   i=6: min(3+1, 2+1) = 3
    #   i=7: min(3+1, 3+1) = 4
    #   dp    : 0  0  1  2  2  3  3  4   -> 4
    #
    # Time: O(n), Space: O(n)

    def minCostClimbingStairs2(self, cost: List[int]) -> int:
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