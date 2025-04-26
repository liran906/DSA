# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 递归
class Solution(object):
    def maxDepth(self, root):
        def dfs(node, depth):
            if not node:
                return depth
            return max(dfs(node.left, depth+1), dfs(node.right, depth+1))
        return dfs(root, 0)

# 迭代
class Solution(object):
    def maxDepth(self, root):
        depth = 0
        if root:
            queue = [root]
            while queue:
                size = len(queue)
                depth += 1
                for _ in range(size):
                    cur = queue.pop(0)
                    if cur.left:
                        queue.append(cur.left)
                    if cur.right:
                        queue.append(cur.right)
        return depth