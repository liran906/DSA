// https://leetcode.cn/problems/binary-tree-preorder-traversal/
// e
package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// 正常写法
func preorderTraversal(root *TreeNode) []int {
	if root == nil {
		return []int{}
	}
	res := []int{root.Val}
	res = append(res, preorderTraversal(root.Left)...)
	res = append(res, preorderTraversal(root.Right)...)
	return res
}

// 匿名函数（闭包）递归写法
func preorderTraversal_2(root *TreeNode) []int {
	var res []int

	var dfs func(node *TreeNode)
	dfs = func(node *TreeNode) {
		if node == nil {
			return
		}
		res = append(res, node.Val)
		dfs(node.Left)
		dfs(node.Right)
	}
	dfs(root)
	return res
}

// 简洁写法 preorderTraversal_c, c for concise
func preorderTraversal_c(root *TreeNode) []int {
	if root == nil {
		return []int{}
	}
	return append([]int{root.Val}, append(preorderTraversal_c(root.Left), preorderTraversal_c(root.Right)...)...)
}
