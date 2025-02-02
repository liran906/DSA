# Valid Binary Search Tree
# https://neetcode.io/problems/valid-binary-search-tree
# m

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Actually should be OK to be EQUAL on one side of the bst.
class Solution:
    def isValidBST(self, root, minVal=None, maxVal=None):
        if not root:
            return True
        if ((root.left and root.left.val >= root.val) 
            or (root.right and root.right.val <= root.val)
            or (maxVal is not None and root.val >= maxVal) 
            or (minVal is not None and root.val <= minVal)):
            return False
        return (self.isValidBST(root.left, minVal, root.val) 
            and self.isValidBST(root.right, root.val, maxVal))