# Lowest Common Ancestor in Binary Search Tree
# https://neetcode.io/problems/lowest-common-ancestor-in-binary-search-tree
# m

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode):
        # just find the root whos value lies between the values of p and q
        while root.val < min(p.val, q.val) or root.val > max(p.val, q.val):
            root = root.right if root.val < p.val else root.left
        return root