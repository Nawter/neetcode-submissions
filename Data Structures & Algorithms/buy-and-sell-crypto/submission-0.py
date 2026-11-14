class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        n = len(prices)
        for l in range(n):
            for r in range(l+1,n):
                profit = prices[r] - prices[l]
                best = max(best, profit)
           

        return best 
        