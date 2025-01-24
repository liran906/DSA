# Balanced Binary Tree
# https://neetcode.io/problems/balanced-binary-tree
# e

# Brute Force
class Solution:
    def isBalanced(self, root):
        if not root:
            return True
        res = abs(self.height(root.left) - self.height(root.right)) <= 1
        return res and self.isBalanced(root.left) and self.isBalanced(root.right)

    def height(self, root):
        if not root:
            return 0
        left = self.height(root.left)
        right = self.height(root.right)
        return 1 + max(left, right)
    
# Using DFS method again
class Solution:
    def isBalanced(self, root):
        if not root:
            return True
        self.balance = True
        self.height(root)
        return self.balance
    
    def height(self, root):
        if not root:
            return 0
        left = self.height(root.left)
        right = self.height(root.right)

        # still can improve: break when false occurs:
        if abs(left - right) > 1:
            self.balance = False
        
        return 1 + max(left, right)

# Improving
class Solution:
    def isBalanced(self, root):
        return self.banlaced_height(root)[0]
    
    def banlaced_height(self, root):
        if not root:
            return [True, 0]
        left = self.banlaced_height(root.left)
        right = self.banlaced_height(root.right)

        balance = left[0] and right[0] and abs(left[1] - right[1]) <= 1
        return [balance, 1 + max(left[1], right[1])]

# Improved: instant return if subtree is not balanced
class Solution:
    def isBalanced(self, root):
        def check(root):
            if not root:
                return 0  # 空节点高度为 0
            
            # 递归检查子树
            left = check(root.left)
            if left == -1: 
                return -1 # 如果左子树不平衡，直接返回 -1

            right = check(root.right)
            if right == -1: 
                return -1 # 如果右子树不平衡，直接返回 -1 
            
            # 检查当前节点是否平衡
            if abs(left - right) > 1: 
                return -1 # 不平衡，返回 -1
            
            # 返回当前节点的高度
            return 1 + max(left, right)
        
        # 如果 check 返回 -1，则树不平衡
        return check(root) != -1

# 一开始是用 False 代替 None 的，理论上没问题 但 neetcode 上不对。改为 None 之后就没问题了。
class Solution:
    def isBalanced(self, root):
        return self._isBalanced(root) != None

    def _isBalanced(self, root):
        if not root:
            return 0
        
        left = self._isBalanced(root.left)
        if left == None:
            return None
        
        right = self._isBalanced(root.right)
        if right == None:
            return None

        if abs(left - right) > 1:
            return None
        
        return 1 + max(left, right)