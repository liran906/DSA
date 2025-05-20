// https://leetcode.cn/problems/insert-into-a-binary-search-tree/description/
// m
package main

func insertIntoBST_(root *TreeNode, val int) *TreeNode {
	if root == nil {
		return &TreeNode{Val: val}
	}
	if root.Val > val {
		if root.Left == nil {
			root.Left = &TreeNode{Val: val}
		} else {
			insertIntoBST_(root.Left, val)
		}
	}
	if root.Val < val {
		if root.Right == nil {
			root.Right = &TreeNode{Val: val}
		} else {
			insertIntoBST_(root.Right, val)
		}
	}
	return root
}

// **递归：简洁写法**
func insertIntoBST(root *TreeNode, val int) *TreeNode {
	if root == nil {
		return &TreeNode{Val: val}
	}
	if root.Val > val {
		root.Left = insertIntoBST(root.Left, val)
	} else {
		root.Right = insertIntoBST(root.Right, val)
	}
	return root
}
