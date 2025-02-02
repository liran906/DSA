# Binary Tree Right Side View
# https://neetcode.io/problems/binary-tree-right-side-view
# m

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root):
        if not root:
            return []
        q = [root]
        res = []
        currcount, nextcount = 1, 0
        while q:
            curr = q.pop(0)
            currcount -= 1
            if curr.left:
                nextcount += 1
                q.append(curr.left)
            if curr.right:
                nextcount += 1
                q.append(curr.right)
            
            if currcount == 0:
                res.append(curr.val)
                currcount = nextcount
                nextcount = 0
        return res

class Solution:
    def rightSideView(self, root):
        if not root:
            return []
        q = [root]
        res = []
        while q:
            lenth = len(q)
            for i in range(lenth):
                curr = q.pop(0)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                if i == lenth - 1:
                    res.append(curr.val)
        return res

class Solution:
    def rightSideView(self, root):
        q = [root]
        res = []
        while q:
            lenth = len(q)
            latestRight = None
            for i in range(lenth):
                curr = q.pop(0)
                if curr:
                    latestRight = curr.val
                    q.append(curr.left)
                    q.append(curr.right)
            if latestRight:
                res.append(latestRight)
        return res

# recrusion
class Solution:
    def rightSideView(self, root):
        res = []
        def dfs(node, depth):
            if not node:
                return
            if depth == len(res):
                res.append(node.val)
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)
        dfs(root, 0)
        return res