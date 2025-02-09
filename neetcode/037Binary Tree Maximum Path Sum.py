# Binary Tree Maximum Path Sum
# https://neetcode.io/problems/binary-tree-maximum-path-sum
# h

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root):
        self.tmax = -float('inf')
        def fmax(node):
            lmax = fmax(node.left) if node.left else 0 # max of left subT
            rmax = fmax(node.right) if node.right else 0 # max of right subT
            lmax = max(lmax, 0) # if negetive, no need to add
            rmax = max(rmax, 0)

            # max value going to parent node
            # (node + left subT) or (node + right subT)
            cmax = max(node.val+lmax, node.val+rmax)

            # max value NOT going to parent node:
            # node alone or leftT + node + rightT
            self.tmax = max(self.tmax, node.val + lmax + rmax, node.val)
            return cmax # pass the current max to parent
        
        # pick the largest:
        return max(fmax(root), self.tmax)