# Maximum Depth of Binary Tree
# https://neetcode.io/problems/depth-of-binary-tree
# e

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        leftD = self.maxDepth(root.left) if root.left else 0
        rightD = self.maxDepth(root.right) if root.right else 0
        return max(leftD, rightD) + 1     