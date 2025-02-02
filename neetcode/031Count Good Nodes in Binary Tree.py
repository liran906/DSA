# Count Good Nodes in Binary Tree
# https://neetcode.io/problems/count-good-nodes-in-binary-tree
# m

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root):
        def dfs(node, maxVal=None):
            if not node:
                return 0
            res = 0
            if maxVal == None or node.val >= maxVal:
                res += 1
                maxVal = node.val
            return res + dfs(node.left, maxVal) + dfs(node.right, maxVal)
        return dfs(root)
