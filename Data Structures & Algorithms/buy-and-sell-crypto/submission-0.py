class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0
        j = 0

        for i in range(1, len(prices)):
            if prices[i] < prices[j]:
                j += 1
            profit = prices[i] - prices[j]
            if profit > max:
                max = profit
        
        return max
