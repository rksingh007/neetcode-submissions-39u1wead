class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max_profit = 0

        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         if prices[j] > prices[i]:
        #             max_profit = max(max_profit, prices[j] - prices[i])
        # return (max_profit)
        maxP = 0
        l,r = 0,1
        while r<len(prices):
            if prices[l]<prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP,profit)
            else:
                l=r
            r+=1
        return maxP