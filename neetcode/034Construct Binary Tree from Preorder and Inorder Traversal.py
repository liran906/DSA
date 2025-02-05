# Construct Binary Tree from Preorder and Inorder Traversal
# https://neetcode.io/problems/binary-tree-from-preorder-and-inorder-traversal
# m

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# class Solution:
#     def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
#         count = 0
#         inorder = [] # xxx
#         root = curr = TreeNode(preorder[0])
#         idx = inorder.index(preorder[0])
#         ltree = inorder[:idx]
#         rtree = inorder[idx+1:]
#         for i in range(1, len(preorder)):
#             val = preorder[i]
#             node = TreeNode(val)
#             if val in ltree:
#                 curr.left = node
#             else:
#                 curr.right = node
#             curr = node

#             idx = inorder.index(val)
#             ltree = inorder[:idx]
#             rtree = inorder[idx+1:]

class Solution:
    def buildTree(self, preorder, inorder):
        if preorder == []:
            return None
        root = TreeNode(preorder[0])
        idx = inorder.index(preorder[0])
        ltree = inorder[:idx]
        rtree = inorder[idx+1:]
        root.left = self.buildTree(preorder[1:idx+1], ltree)
        root.right = self.buildTree(preorder[idx+1:], rtree)
        return root