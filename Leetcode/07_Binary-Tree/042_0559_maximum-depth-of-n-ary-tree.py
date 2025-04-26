# https://leetcode.cn/problems/maximum-depth-of-n-ary-tree/
# e

# 递归 1
class Solution(object):
    def maxDepth(self, root):
        def dfs(node, depth):
            maxd = depth
            for c in node.children:
                maxd = max(maxd, dfs(c, depth+1))
            return maxd
        
        if not root:
            return 0
        return dfs(root, 1)

# 递归 2
class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        if not root.children:
            return 1
        
        return 1 + max(self.maxDepth(c) for c in root.children)

# 迭代
class Solution(object):
    def maxDepth(self, root):
        depth = 0
        if root:
            queue = [root]
            # bfs
            while queue:
                size = len(queue)
                depth += 1
                for _ in range(size):
                    cur = queue.pop(0)
                    queue.extend(cur.children)
        return depth