# Subtree of Another Tree
# https://neetcode.io/problems/subtree-of-a-binary-tree
# e

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# O(n*m)
class Solution:
    def isSubtree(self, root, subRoot):
        if not subRoot:
            return True
        if not root:
            return False
        if self.isSame(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSame(self, p, q):
        if not p and not q:
            return True
        elif p and q and p.val == q.val:
            return self.isSame(p.left, q.left) and self.isSame(p.right, q.right)
        else:
            return False

# serialize method (slightly different from the one provided in neetcode), O(n+m)
class Solution:
    def serialize(self, root):
        if root is None:
            return "$#"
        return "$" + str(root.val) + self.serialize(root.left) + self.serialize(root.right)

    def isSubtree(self, root, subRoot):
        serialized_root = self.serialize(root)
        serialized_subRoot = self.serialize(subRoot)
        return serialized_subRoot in serialized_root