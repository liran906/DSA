# https://leetcode.cn/problems/symmetric-tree/description/
# e

# 双栈迭代 逻辑有点复杂，不好
class Solution(object):
    def isSymmetric(self, root):
        # 空树 或 只有一个根节点 ⇒ 对称
        if not root:
            return True
        if not root.left and not root.right:
            return True
        
        # 一边为空，另一边不为空 ⇒ 不对称
        if not root.left or not root.right:
            return False

        # 使用两个栈分别同时遍历左右子树
        leftstack = [root.left]
        rightstack = [root.right]

        # 同步 DFS 遍历左右子树
        while leftstack and rightstack:
            leftcur = leftstack.pop()
            rightcur = rightstack.pop()

            # 当前两个节点值不等 ⇒ 不对称
            if leftcur.val != rightcur.val:
                return False

            # 比较外侧节点：left.left vs right.right
            if leftcur.left and rightcur.right:
                leftstack.append(leftcur.left)
                rightstack.append(rightcur.right)
            elif leftcur.left or rightcur.right:
                # 一边为空另一边不为空 ⇒ 不对称
                return False

            # 比较内侧节点：left.right vs right.left
            if leftcur.right and rightcur.left:
                leftstack.append(leftcur.right)
                rightstack.append(rightcur.left)
            elif leftcur.right or rightcur.left:
                return False

        # 最终两个栈都应为空 ⇒ 所有节点对称遍历完毕
        return not leftstack and not rightstack

# 单栈迭代
class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return True
        
        stack = [(root.left, root.right)]  # 栈中存储一对对称节点

        while stack:
            left, right = stack.pop()

            # 都为 None ⇒ 合法
            if not left and not right:
                continue
            # 只有一个为 None ⇒ 不对称
            if not left or not right:
                return False
            # 值不等 ⇒ 不对称
            if left.val != right.val:
                return False

            # 入栈顺序很关键：外侧在一起，内侧在一起
            stack.append((left.left, right.right))   # 外侧对称
            stack.append((left.right, right.left))   # 内侧对称
        return True
    
# 双栈简单写法（和单栈一个逻辑）
class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return True
        lstack = [root.left]
        rstack = [root.right]

        while lstack: # or rstack
            left = lstack.pop()
            right = rstack.pop()

            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            
            lstack.append(left.left)
            rstack.append(right.right)
            lstack.append(left.right)
            rstack.append(right.left)
        return True

# 递归
class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return True  # 空树是对称的
        
        def dfs(left, right):
            # 两个子节点都为空 ⇒ 对称
            if not left and not right:
                return True
            # 只有一个为空 ⇒ 不对称
            if not left or not right:
                return False
            # 当前值相等，且子树分别对称
            return left.val == right.val and dfs(left.left, right.right) and dfs(left.right, right.left)
                
        return dfs(root.left, root.right)