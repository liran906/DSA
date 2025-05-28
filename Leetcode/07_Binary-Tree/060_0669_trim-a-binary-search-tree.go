// https://leetcode.cn/problems/trim-a-binary-search-tree/description/
// m
package main

// 遇到这种二叉树，优先递归
func trimBST(root *TreeNode, low int, high int) *TreeNode {
	if root == nil {
		return nil
	}

	if root.Val < low {
		// 当前节点太小，丢弃左子树，只保留右子树
		return trimBST(root.Right, low, high)
	}
	if root.Val > high {
		// 当前节点太大，丢弃右子树，只保留左子树
		return trimBST(root.Left, low, high)
	}

	// 节点在范围内，递归处理左右子树
	root.Left = trimBST(root.Left, low, high)
	root.Right = trimBST(root.Right, low, high)
	return root
}

// 下面我放个试图迭代的方法，毫不意外的无法通过
func trimBST_na(root *TreeNode, low int, high int) *TreeNode {
	if root == nil {
		return nil
	}

	node := root
	parent := &TreeNode{Left: root}

	// 修剪小于 low 的部分
	for node != nil && node.Val > low || (node.Right != nil && node.Right.Val > low) {
		for node != nil && node.Val > low {
			parent = node
			node = node.Left
		}
		if node != nil && node.Right != nil && node.Right.Val > low {
			parent.Left = node.Right
			node = parent.Left
		} else {
			parent.Left = nil
		}
	}

	// 修剪大于 high 的部分
	node = root
	parent = &TreeNode{Right: root}

	for node != nil && node.Val < high || (node.Left != nil && node.Left.Val < high) {
		for node != nil && node.Val < high {
			parent = node
			node = node.Right
		}
		if node != nil && node.Left != nil && node.Left.Val < high {
			parent.Right = node.Left
			node = parent.Right
		} else {
			parent.Right = nil
		}
	}

	return root
}
