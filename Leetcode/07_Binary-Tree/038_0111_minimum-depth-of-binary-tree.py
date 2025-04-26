# 递归
class Solution(object):
    def minDepth(self, root):
        if not root:
            return 0
        if not root.left:
            return 1 + self.minDepth(root.right)
        if not root.right:
            return 1 + self.minDepth(root.left)
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

# 迭代
class Solution(object):
    def minDepth(self, root):
        depth = 0
        if root:
            q = [root]
            # bfs
            while q:
                depth += 1
                size = len(q)
                for _ in range(size):
                    cur = q.pop(0)
                    if not cur.left and not cur.right:
                        return depth # 第一个叶子节点，就是最小深度
                    if cur.left:
                        q.append(cur.left)
                    if cur.right:
                        q.append(cur.right)
        return depth