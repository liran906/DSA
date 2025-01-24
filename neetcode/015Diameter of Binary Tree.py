# Diameter of Binary Tree
# https://neetcode.io/problems/binary-tree-diameter
# m

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Brute Force
class Solution:
    def diameterOfBinaryTree(self, root):
        htable = {}
        if not root:
            return 0
        left = self._height(root.left, htable) if root.left else 0
        right = self._height(root.right, htable) if root.right else 0
        return max(left + right, self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
    
    def _height(self, root, htable):
        if not root:
            return 0
        
        if root in htable:
            return htable[root]
        
        if root.left in htable:
            leftH = htable[root.left]
        else:
            leftH = self._height(root.left, htable) if root.left else 0
            htable[root.left] = leftH
        
        if root.right in htable:
            rightH = htable[root.right]
        else:
            rightH = self._height(root.right, htable) if root.right else 0
            htable[root.right] = rightH
        
        htable[root] = max(leftH, rightH) + 1
        return htable[root]

# DFS METHOD: computing the height and the diameter at the same time.
class Solution:
    def diameterOfBinaryTree(self, root):
        self.result = 0
        
        # Returns the height, not diameter
        def height(root):
            if not root:
                return 0
            
            left = height(root.left)
            right = height(root.right)

            # Compares for the largest diameter everytime
            self.result = max(self.result, left + right)

            return max(left, right) + 1
        
        height(root)

        return self.result


# Another way of coding dfs
class Solution:
    def diameterOfBinaryTree(self, root):
        self.result = 0
        self.height(root)
        return self.result
    
    # Returns the height, not diameter
    def height(self, root):
        if not root:
            return 0
        
        left = self.height(root.left)
        right = self.height(root.right)

        # Compares for the largest diameter everytime
        self.result = max(self.result, left + right)

        return max(left, right) + 1