# Kth Smallest Integer in BST
# https://neetcode.io/problems/kth-smallest-integer-in-bst
# m

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Inorder Traversal
class Solution:
    def kthSmallest(self, root, k):
        res = []
        def dfs(node):
            if node.left:
                dfs(node.left)
            res.append(node.val)
            if node.right:
                dfs(node.right)
        dfs(root)
        return res[k-1]

# Recursive DFS (Optimal)
class Solution:
    def kthSmallest(self, root, k):
        count = k
        res = root.val

        def dfs(node):
            nonlocal count, res
            if not node:
                return
            
            dfs(node.left)
            if res == root.val: # if !=, then the value is found
                count -= 1
                if count == 0:
                    res = node.val
                    return # stops once found
                dfs(node.right)
        
        dfs(root)
        return res