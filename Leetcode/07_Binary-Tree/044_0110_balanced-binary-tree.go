// https://leetcode.com/problems/balanced-binary-tree/
// e

// O(n^2)
// depth(root.Left) 和 isBalanced(root.Left) 分别会递归一遍左子树，重复遍历了
package main

func isBalanced_(root *TreeNode) bool {
	if root == nil {
		// 空树一定是平衡的
		return true
	}

	// 计算左右子树的高度差
	diff := depth(root.Left) - depth(root.Right)

	// 当前节点平衡 && 左子树平衡 && 右子树平衡
	return diff <= 1 && diff >= -1 && isBalanced_(root.Left) && isBalanced_(root.Right)
}

// 辅助函数：计算从 node 出发的树的最大深度
func depth(node *TreeNode) int {
	if node == nil {
		return 0
	}
	// 深度 = 左右子树最大深度 + 1
	return max(depth(node.Left), depth(node.Right)) + 1
}

// O(n)
// 一次遍历，同时返回深度以及是否平衡
func isBalanced(root *TreeNode) bool {
	res, _ := dfs(root) // 调用辅助函数，返回树是否平衡（忽略深度）
	return res          // 只关心是否平衡
}

// dfs 函数：返回两个结果（当前子树是否平衡，当前子树的最大深度）
func dfs(node *TreeNode) (bool, int) {
	if node == nil {
		// 空树，显然是平衡的，深度为 0
		return true, 0
	}

	// 递归处理左子树，获得左子树是否平衡、左子树最大深度
	leftBalanced, leftDepth := dfs(node.Left)
	// 递归处理右子树，获得右子树是否平衡、右子树最大深度
	rightBalanced, rightDepth := dfs(node.Right)

	// 当前节点是否平衡：
	// 左右子树都平衡 && 左右子树深度差不超过 1
	isBalanced := abs(leftDepth-rightDepth) <= 1 && leftBalanced && rightBalanced

	// 当前节点的深度 = 左右子树最大深度 + 1（加上自己这一层）
	depth := max(leftDepth, rightDepth) + 1

	// 返回当前子树是否平衡，以及当前子树深度
	return isBalanced, depth
}

// 辅助函数：求绝对值
func abs(a int) int {
	if a >= 0 {
		return a
	}
	return -a
}
