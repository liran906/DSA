// https://leetcode.cn/problems/maximum-depth-of-binary-tree
// e

package main

func maxDepth(root *TreeNode) int {
	if root == nil {
		return 0
	}
	var size int
	queue := []*TreeNode{root}
	count := 0

	for len(queue) > 0 {
		count++
		size = len(queue)
		for range size {
			node := queue[0]
			queue = queue[1:]

			if node.Left != nil {
				queue = append(queue, node.Left)
			}
			if node.Right != nil {
				queue = append(queue, node.Right)
			}
		}
	}
	return count
}

// recursive
func maxDepth_Recursive(root *TreeNode) int {
	var dfs func(*TreeNode, int) int
	dfs = func(node *TreeNode, depth int) int {
		if node == nil { // 到叶节点的子节点才会返回，所以深度会+1，正好符合题目要求
			return depth
		}
		return max(dfs(node.Left, depth+1), dfs(node.Right, depth+1))
	}
	return dfs(root, 0)
}

func maxDepth_RecursiveII(root *TreeNode) int {
	if root == nil {
		return 0
	}
	// 左为空，走右
	if root.Left == nil {
		return maxDepth(root.Right) + 1
	}
	// 右为空，走左
	if root.Right == nil {
		return maxDepth(root.Left) + 1
	}
	// 都不空，取最大
	return max(maxDepth(root.Left), maxDepth(root.Right)) + 1
}
