// https://leetcode.com/problems/minimum-depth-of-binary-tree/
// e
package main

import "math"

func minDepth(root *TreeNode) int {
	if root == nil {
		return 0
	}
	size := 0
	count := 0
	queue := []*TreeNode{root}
	for len(queue) > 0 {
		count++
		size = len(queue)
		for range size {
			node := queue[0]
			queue = queue[1:]
			if node.Left == nil && node.Right == nil {
				return count
			}
			if node.Left != nil {
				queue = append(queue, node.Left)
			}
			if node.Right != nil {
				queue = append(queue, node.Right)
			}
		}
	}
	return count // 不会到这步的，不过为了编译加上
}

// recursive
func minDepth_Recursive(root *TreeNode) int {
	if root == nil {
		return 0
	}
	var dfs func(*TreeNode, int) int
	dfs = func(node *TreeNode, depth int) int {
		if node == nil {
			return math.MaxInt32 // 这里用一个最大数，规避只有一边空的情况
		}
		if node.Left == nil && node.Right == nil {
			return depth
		}
		return min(dfs(node.Left, depth+1), dfs(node.Right, depth+1))
	}
	return dfs(root, 1)
}

// 更优雅的递归
func minDepth_RecursiveII(root *TreeNode) int {
	if root == nil {
		return 0
	}

	// 如果左子树为空，只走右边
	if root.Left == nil {
		return minDepth(root.Right) + 1
	}

	// 如果右子树为空，只走左边
	if root.Right == nil {
		return minDepth(root.Left) + 1
	}

	// 两边都有，取最小
	return min(minDepth(root.Left), minDepth(root.Right)) + 1
}

// 或者逻辑反过来
func minDepth_RecursiveIII(root *TreeNode) int {
	if root == nil {
		return 0
	}
	if root.Left != nil && root.Right != nil {
		return min(minDepth(root.Left), minDepth(root.Right)) + 1
	}
	if root.Left != nil {
		return minDepth(root.Left) + 1
	}
	// root.Right != nil
	return minDepth(root.Right) + 1
}
