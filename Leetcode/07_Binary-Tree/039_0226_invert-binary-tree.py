# https://leetcode.cn/problems/invert-binary-tree/description/
# e

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 递归
class Solution:
    def invertTree(self, root):
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

# 迭代
class Solution:
    def invertTree(self, root):
        if root:
            queue = [root]
            while queue:
                size = len(queue)
                for _ in range(size):
                    cur = queue.pop(0)
                    cur.left, cur.right = cur.right, cur.left
                    if cur.left:
                        queue.append(cur.left)
                    if cur.right:
                        queue.append(cur.right)
        return root