# https://leetcode.cn/problems/count-complete-tree-nodes/
# e

# 常规方法 O(n)
class Solution(object):
    def countNodes(self, root):
        if not root:
            return 0
        queue = [root]
        lv = 0
        while queue:
            lv += 1
            for i in range(len(queue)):
                cur = queue.pop(0)
                if cur.left:
                    queue.append(cur.left)
                else:
                    return (2 * i) + (2 ** lv - 1)
                if cur.right:
                    queue.append(cur.right)
                else:
                    return (2 * i + 1) + (2 ** lv - 1)

# 二分查找 O(logn)
# 分别计算左右子树高度：
# 左子树右子树高度相同——左子树满二叉（公式计算），右子树递归计算
# 左子树右子树高度不同——右子树满二叉（公式计算），左子树递归计算
class Solution(object):
    def countNodes(self, root):
        if not root:
            return 0
        ld, rd = self.depth(root.left), self.depth(root.right)
        if ld == rd:
            # 递归求右子树节点数 + 左子树节点数 + 1（当前根节点）
            return self.countNodes(root.right) + 2**ld - 1 + 1
        else:
            # 递归求左子树节点数 + 右子树节点数 + 1（当前根节点）
            return self.countNodes(root.left) + 2**rd - 1 + 1

    # 完全二叉树的高度就是其左子树的高度+1
    def depth(self, node):
        if not node: return 0
        return self.depth(node.left) + 1 if node.left else 1