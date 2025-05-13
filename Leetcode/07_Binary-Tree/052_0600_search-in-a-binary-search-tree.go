// https://leetcode.cn/problems/search-in-a-binary-search-tree/description/
// e
package main

func searchBST(root *TreeNode, val int) *TreeNode {
	if root == nil {
		return nil
	}
	if root.Val < val {
		return searchBST(root.Right, val)
	}
	if root.Val > val {
		return searchBST(root.Left, val)
	}
	return root
}

func searchBST_i(root *TreeNode, val int) *TreeNode {
	if root == nil {
		return nil
	}
	node := root
	for node != nil && node.Val != val {
		if node.Val > val {
			node = node.Left
		} else {
			node = node.Right
		}
	}
	return node // node == nil or node.Val == val, either way, return node
}
