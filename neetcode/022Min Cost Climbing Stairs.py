# Min Cost Climbing Stairs
# https://neetcode.io/problems/min-cost-climbing-stairs
# e

# Dynamic Programming (Bottom-Up) time: O(n), space: O(n)
class Solution:
    def minCostClimbingStairs(self, cost):
        mincost = [0] * (len(cost) + 1)
        for i in range(2, len(cost) + 1):
            mincost[i] = min(mincost[i-1] + cost[i-1], mincost[i-2] + cost[i-2])
        return mincost[len(cost)]

# Dynamic Programming (optimize space) (Bottom-Up) time: O(n), space: O(1)
class Solution:
    def minCostClimbingStairs(self, cost):
        currMincost = prevMincost = 0
        for i in range(2, len(cost) + 1):
            temp = currMincost
            currMincost = min(currMincost + cost[i-1], prevMincost + cost[i-2])
            prevMincost = temp
        return currMincost