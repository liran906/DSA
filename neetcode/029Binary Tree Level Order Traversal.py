# Binary Tree Level Order Traversal
# https://neetcode.io/problems/level-order-traversal-of-binary-tree
# m

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        myqueue = [root]
        res = [[]]
        currchild = 1
        nextchild = 0
        
        while myqueue:
            curr = myqueue.pop(0)
            currchild -= 1
            if curr.left:
                myqueue.append(curr.left)
                nextchild += 1
            if curr.right:
                myqueue.append(curr.right)
                nextchild += 1
            
            res[-1].append(curr.val)
            
            if currchild == 0 and myqueue:
                currchild = nextchild
                nextchild = 0
                res.append([])
        
        return res

# DFS solution
class Solution:
    def levelOrder(self, root):
        res = []

        def dfs(node, depth):
            if not node:
                return None
            if len(res) == depth:
                res.append([])
            
            res[depth].append(node.val)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        
        dfs(root, 0)
        return res