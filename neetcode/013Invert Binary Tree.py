# Invert Binary Tree
# https://neetcode.io/problems/invert-a-binary-tree
# e

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root):
        if not root or (not root.left and not root.right):
            return root
        elif root.left and root.right:
            left = self.invertTree(root.right)
            right = self.invertTree(root.left)
            root.left, root.right = left, right
        elif root.right:
            root.left = self.invertTree(root.right)
            root.right = None
        else:
            root.right = self.invertTree(root.left)
            root.left = None
        return root

# More concise
class Solution:
    def invertTree(self, root):
        if root:
            root.left, root.right = root.right, root.left
            self.invertTree(root.right)
            self.invertTree(root.left)
        return root