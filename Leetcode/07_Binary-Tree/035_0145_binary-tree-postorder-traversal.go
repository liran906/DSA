// https://leetcode.cn/problems/binary-tree-postorder-traversal/description/
// e
package main

// type TreeNode struct {
// 	Val   int
// 	Left  *TreeNode
// 	Right *TreeNode
// }

func postorderTraversal(root *TreeNode) []int {
	if root == nil {
		return []int{}
	}

	res := postorderTraversal(root.Left)
	res = append(res, postorderTraversal(root.Right)...)
	res = append(res, root.Val)

	return res
}

func postorderTraversal_2(root *TreeNode) []int {
	var res []int

	var dfs func(node *TreeNode)
	dfs = func(node *TreeNode) {
		if node != nil {
			dfs(node.Left)
			dfs(node.Right)
			res = append(res, node.Val)
		}
	}

	dfs(root)
	return res
}

func postorderTraversal_c(root *TreeNode) []int {
	if root == nil {
		return []int{}
	}
	return append(postorderTraversal_c(root.Left), append(postorderTraversal_c(root.Right), root.Val)...)
}
