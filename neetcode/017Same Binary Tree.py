# Same Binary Tree
# https://neetcode.io/problems/same-binary-tree
# e

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p, q):
        for ptn, qtn in zip(self.preorder(p), self.preorder(q)):
            if ptn != qtn:
                return False
        return True
    
    def preorder(self,t):
        if t:
            yield t.val
            yield from self.preorder(t.left)
            yield from self.preorder(t.right)
        else:
            yield None

# Recursive method
class Solution:
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        elif p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False