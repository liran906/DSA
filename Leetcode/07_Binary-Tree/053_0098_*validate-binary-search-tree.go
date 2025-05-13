// https://leetcode.cn/problems/validate-binary-search-tree/description/
// m

package main

// **两个方法都好**

// 递归，dfs 并记录上下限
// 注意对于 int 指针的使用。
func isValidBST(root *TreeNode) bool {
	// 定义一个递归函数 dfs，用于检查每个节点是否满足 BST 条件
	// 参数 min 和 max 是当前节点允许的取值上下限，使用 *int 类型表示“可选”边界（nil 表示无界）
	var dfs func(nd *TreeNode, min, max *int) bool

	dfs = func(node *TreeNode, min, max *int) bool {
		// 如果当前节点为空，说明是空树或叶子节点的子节点，返回 true
		if node == nil {
			return true
		}

		// 检查当前节点的值是否在 (min, max) 区间内（不允许等于）
		// 如果 max 不为 nil，且 node.Val >= *max，说明不合法
		// 如果 min 不为 nil，且 node.Val <= *min，也不合法
		if (max == nil || node.Val < *max) && (min == nil || node.Val > *min) {
			// 对左子树递归：
			// - 左子树最大值不能 ≥ 当前节点值，因此 max 设为当前 node.Val
			// - 下限 min 保持不变
			// 对右子树递归：
			// - 右子树最小值不能 ≤ 当前节点值，因此 min 设为当前 node.Val
			// - 上限 max 保持不变
			return dfs(node.Left, min, &node.Val) && dfs(node.Right, &node.Val, max)
		}

		// 如果当前节点不满足 BST 的要求，返回 false
		return false
	}

	// 初始时没有上下限
	return dfs(root, nil, nil)
}

// 递归，利用中序遍历递增判断
// 这里也用了 int 指针，现学现用，也可以改为 TreeNode 指针
// 判断一棵二叉树是否是有效的二叉搜索树（BST）
// 核心思想：中序遍历时，所有节点值应该严格递增
func isValidBST_2(root *TreeNode) bool {
	// prev 用于记录上一个访问过的节点的值（中序遍历的“前一个值”）
	// 使用 *int 表示：nil 代表还未赋值，也可以是 *TreeNode
	var prev *int

	// 定义一个递归函数 inorder，用于中序遍历并检查每个节点
	var inorder func(*TreeNode) bool
	inorder = func(node *TreeNode) bool {
		// 空节点合法
		if node == nil {
			return true
		}

		// 左
		if !inorder(node.Left) {
			return false
		}

		// 中
		// 检查当前值是否大于前一个值（必须严格递增）
		if prev != nil && node.Val <= *prev {
			return false
		}
		prev = &node.Val // 更新 prev 为当前节点值（注意取地址）

		// 右
		return inorder(node.Right)
	}
	// 开始中序遍历
	return inorder(root)
}
