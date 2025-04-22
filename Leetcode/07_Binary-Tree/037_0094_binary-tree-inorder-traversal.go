// https://leetcode.cn/problems/binary-tree-inorder-traversal/description/
// e
package main

// https://www.bilibili.com/video/BV1Zf4y1a77g

// inorderTraversal_i 实现二叉树的中序遍历（左 → 根 → 右）
// 使用迭代方式 + 切片作为栈，无需额外库
func inorderTraversal_i(root *TreeNode) (res []int) {
	// 初始化栈（用切片模拟）
	stack := []*TreeNode{}
	cur := root

	// 当还有节点可访问（栈不空或当前节点不为空）
	for len(stack) > 0 || cur != nil {
		if cur != nil {
			// 1. 一直向左走，把所有左子节点压栈
			stack = append(stack, cur)
			cur = cur.Left
		} else {
			// 2. 到达最左侧后，回退一层，访问当前节点
			cur = stack[len(stack)-1]    // 取栈顶节点
			stack = stack[:len(stack)-1] // 出栈

			res = append(res, cur.Val) // 记录

			cur = cur.Right // 3. 然后转向右子树
		}
	}
	return
}

// 复习前中后序 迭代遍历二叉树
func inorderTraversal_ii(root *TreeNode) (res []int) {
	if root == nil {
		return
	}

	stack := []*TreeNode{}
	cur := root

	for len(stack) > 0 || cur != nil {
		if cur != nil {
			stack = append(stack, cur)
			cur = cur.Left
		} else {
			cur = stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			res = append(res, cur.Val)
			cur = cur.Right
		}
	}
	return
}

func preorderTraversal_ii(root *TreeNode) (res []int) {
	if root == nil {
		return
	}

	stack := []*TreeNode{root}
	var cur *TreeNode

	for len(stack) > 0 {
		cur = stack[len(stack)-1]
		stack = stack[:len(stack)-1]

		res = append(res, cur.Val)

		if cur.Right != nil {
			stack = append(stack, cur.Right)
		}
		if cur.Left != nil {
			stack = append(stack, cur.Left)
		}
	}
	return
}

func postorderTraversal_ii(root *TreeNode) (res []int) {
	if root == nil {
		return
	}

	stack := []*TreeNode{root}
	var cur *TreeNode

	for len(stack) > 0 {
		cur = stack[len(stack)-1]
		stack = stack[:len(stack)-1]

		res = append(res, cur.Val)
		if cur.Left != nil {
			stack = append(stack, cur.Left)
		}
		if cur.Right != nil {
			stack = append(stack, cur.Right)
		}
	}

	for l, r := 0, len(res)-1; l < r; l, r = l+1, r-1 {
		res[l], res[r] = res[r], res[l]
	}
	return
}
