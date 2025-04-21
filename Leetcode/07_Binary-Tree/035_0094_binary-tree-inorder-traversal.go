// https://leetcode.cn/problems/binary-tree-inorder-traversal/description/
// e
package main

func inorderTraversal(root *TreeNode) []int {
	if root == nil {
		return []int{}
	}
	res := inorderTraversal(root.Left)
	res = append(res, root.Val)
	res = append(res, inorderTraversal(root.Right)...)
	return res
}

func inorderTraversal_2(root *TreeNode) (res []int) {
	var dfs func(node *TreeNode)
	dfs = func(node *TreeNode) {
		if node == nil {
			return
		}
		dfs(node.Left)
		res = append(res, node.Val)
		dfs(node.Right)
	}

	dfs(root)
	return
}

func inorderTraversal_c(root *TreeNode) []int {
	if root == nil {
		return []int{}
	}
	return append(inorderTraversal_c(root.Left), append([]int{root.Val}, inorderTraversal_c(root.Right)...)...)
}
