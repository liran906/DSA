// https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
// m

package main

// 先看 106 吧，我是从 106 过来的，原理基本一样，但这里我故意做了点变化
// 就是 left 和 right 的取值，106 是左闭右闭，这里是左闭右开
func buildTree_pre(preorder []int, inorder []int) *TreeNode {
	// 1. 构建哈希表，用于在中序数组中快速定位某个节点的位置
	inorderMap := make(map[int]int)
	for i, v := range inorder {
		inorderMap[v] = i
	}

	// 2. 初始化一个索引，表示当前正在处理的 preorder 根节点位置（从左到右）
	rootIndex := 0

	// 3. 定义递归函数，参数是当前 inorder 子树的左右边界 [left, right)
	var buildRoot func(int, int) *TreeNode
	buildRoot = func(left, right int) *TreeNode {
		// 边界条件：当区间为空时，说明该子树为 nil（注意是左闭右开区间）
		if left >= right {
			return nil
		}

		// 3.1 取当前 preorder[rootIndex] 作为根节点的值
		rootVal := preorder[rootIndex]
		rootIndex++ // 前序遍历是 根 → 左 → 右，递增索引

		// 3.2 在 inorder 中找到根节点的位置，以划分左右子树
		index := inorderMap[rootVal]

		// 3.3 构建当前根节点
		root := TreeNode{Val: rootVal}

		// 3.4 递归构建子树：这里和 106 区别就是先从左子树开始递归
		root.Left = buildRoot(left, index)
		root.Right = buildRoot(index+1, right)

		return &root
	}

	// 4. 从整个 inorder 区间构造整棵树（左闭右开）
	return buildRoot(0, len(inorder))
}
