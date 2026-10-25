class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        j = 0

        for i in range(1, len(prices)):
            if prices[j] > prices[i]:
                j = i
            else:
                 res = max(res, prices[i] - prices[j])
        return res