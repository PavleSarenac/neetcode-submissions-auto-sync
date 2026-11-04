class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        leftWindowEdge = 0
        maxProfit = 0
        for rightWindowEdge in range(1, len(prices)):
            if prices[rightWindowEdge] < prices[leftWindowEdge]:
                leftWindowEdge = rightWindowEdge
                continue
            profit = prices[rightWindowEdge] - prices[leftWindowEdge]
            maxProfit = max(maxProfit, profit)
        return maxProfit