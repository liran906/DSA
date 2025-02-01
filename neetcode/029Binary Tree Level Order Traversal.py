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