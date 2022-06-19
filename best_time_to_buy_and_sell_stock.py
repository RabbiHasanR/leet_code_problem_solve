class Solution:
    def maxProfit(self, prices):
        l,r = 0,1 # l=buy price index, r=sell price index
        maxP = 0
        
        while r < len(prices):
            # profitable ?
            if prices[l] < prices [r]:
                profit = prices[r] - prices[l]
                # maximum profit
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP

s = Solution()
prices = [7,1,5,3,6,4]
print(s.maxProfit(prices))