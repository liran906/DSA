# Serialize and Deserialize Binary Tree
# https://neetcode.io/problems/serialize-and-deserialize-binary-tree
# h

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root):
        queue = [root]
        res = []
        while queue:
            current = queue.pop(0)
            if current:
                queue.append(current.left)
                queue.append(current.right)
                res.append(current.val)
            else:
                res.append(current)

        while res[-1] == None:
            res.pop()
        
        return str(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data):
        data = eval(data)
        queue = []
        if data:
            root = TreeNode(data.pop(0))
            queue.append(root)
        while queue and data:
            current = queue.pop(0)
            pop1 = data.pop(0)
            pop2 = data.pop(0) if data else None
            
            if pop1:
                current.left = TreeNode(pop1)
                queue.append(current.left)
            if pop2:
                current.right = TreeNode(pop2)
                queue.append(current.right)
            
            


t = TreeNode(5)
t.left = TreeNode(1)
t.right = TreeNode(2)
t.right.left = TreeNode(3)
t.right.right = TreeNode(4)
t.right.left.left = TreeNode(6)

s = Codec()
print(s.serialize(t))