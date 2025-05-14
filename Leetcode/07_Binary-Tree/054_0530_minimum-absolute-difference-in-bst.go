// https://leetcode.cn/problems/minimum-absolute-difference-in-bst/description/
// e
package main

import "math"

// 这是错误的方法
// 第一遍只考虑相邻节点的最小值，没有考虑左子树的右子节点和当前节点最小的情况
func getMinimumDifference_na(root *TreeNode) int {
	if root.Left == nil && root.Right == nil {
		return math.MaxInt
	} else if root.Left != nil && root.Right != nil {
		return min(
			abs(root.Val-root.Left.Val), getMinimumDifference_na(root.Left),
			abs(root.Val-root.Right.Val), getMinimumDifference_na(root.Right),
		)
	} else if root.Left != nil {
		return min(abs(root.Val-root.Left.Val), getMinimumDifference_na(root.Left))
	} else {
		return min(abs(root.Val-root.Right.Val), getMinimumDifference_na(root.Right))
	}
}

// **中序遍历 递归**
// 利用中序遍历是按从小到大的顺序遍历 BST 的特点，求最小值。
func getMinimumDifference(root *TreeNode) int {
	var (
		res     int       = math.MaxInt // 记录最小差值，初始设为最大整数
		prev    *TreeNode               // 记录中序遍历过程中的“上一个节点”
		inorder func(*TreeNode)
	)

	// 中序遍历函数（左-根-右）
	inorder = func(node *TreeNode) {
		if node == nil {
			return
		}
		// 递归左子树
		inorder(node.Left)

		// 处理当前节点
		// 中序遍历的值是有序的，因此当前节点和上一个节点的差就是候选答案
		if prev != nil {
			res = min(res, node.Val-prev.Val) // 这里也不需要 abs 了
		}
		prev = node // 更新 prev，指向当前节点

		// 递归右子树
		inorder(node.Right)
	}
	// 从根节点开始中序遍历
	inorder(root)
	return res
}

// *迭代法*
// 用栈中序遍历 看：inorderTraversal_i(root)
func getMinimumDifference_i(root *TreeNode) int {
	stack := []*TreeNode{} // 显式栈用于模拟递归中的栈行为
	cur := root            // 当前访问节点
	res := math.MaxInt     // 初始化为最大值，用于记录最小差值
	var prev *TreeNode     // prev 用于记录中序遍历的前一个节点

	// 开始中序遍历：左 -> 根 -> 右
	for len(stack) > 0 || cur != nil {
		if cur != nil {
			// 一路向左，压栈
			stack = append(stack, cur)
			cur = cur.Left
		} else {
			// 到达最左边，开始回退处理节点
			cur = stack[len(stack)-1]
			stack = stack[:len(stack)-1]

			// 比较当前值与前一个节点值，更新最小差值
			if prev != nil {
				res = min(res, cur.Val-prev.Val)
			}
			prev = cur // 更新 prev 为当前节点

			// 转向右子树
			cur = cur.Right
		}
	}
	return res
}
