class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0            # buy day (lowest price seen so far)
        r = 1            # sell day (scans forward)
        max_profit = 0   # 0 if no profitable trade exists

        while r < len(prices):
            if prices[l] < prices[r]:
                # profitable: check if this sell beats the best so far
                profit = prices[r] - prices[l]
                max_profit = max(profit, max_profit)
            else:
                # found a cheaper (or equal) buy price → move buy day here
                # safe to jump: any future sell is better off buying at r than at l
                l = r
            r += 1       # always advance sell day

        return max_profit