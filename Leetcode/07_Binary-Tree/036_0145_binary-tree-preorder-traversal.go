// https://leetcode.cn/problems/binary-tree-postorder-traversal/
// e
package main

// type TreeNode struct {
// 	Val int
// 	Left *TreeNode
// 	Right *TreeNode
// }

// 迭代写法
func preorderTraversal_i(root *TreeNode) (res []int) {
	if root == nil {
		return
	}

	var stack []*TreeNode
	var cur *TreeNode

	// dfs
	stack = []*TreeNode{root}
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
