# Best Time to Buy and Sell Stock
# https://neetcode.io/problems/buy-and-sell-crypto
# e

class Solution:
    def maxProfit(self, prices):
        minvalues = []
        maxvalues = []
        for i in range(len(prices)):
            if minvalues == []:
                minvalues.append(prices[i])
            else:
                if prices[i] < minvalues[-1]:
                    minvalues.append(prices[i])
                else:
                    minvalues.append(minvalues[-1])
        for i in reversed(range(len(prices))):
            if maxvalues == []:
                maxvalues.append(prices[i])
            else:
                if prices[i] > maxvalues[-1]:
                    maxvalues.append(prices[i])
                else:
                    maxvalues.append(maxvalues[-1])
        maxvalues = maxvalues[::-1]
        maxProfit = 0
        for i in range(len(prices)):
            profit = maxvalues[i] - minvalues[i]
            if profit > maxProfit:
                maxProfit = profit
        return maxProfit
# too complicated in space complexity: O(n)

class Solution:
    def maxProfit(self, prices):
        maxProfit = 0
        minPrice = prices[0]
        for price in prices:
            minPrice = min(minPrice, price)
            maxProfit = max(maxProfit, price - minPrice)
        return maxProfit