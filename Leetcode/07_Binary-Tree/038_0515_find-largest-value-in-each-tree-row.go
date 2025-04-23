// https://leetcode.com/problems/find-largest-value-in-each-tree-row/
// m

package main

import "math"

func largestValues(root *TreeNode) (res []int) {
	if root == nil {
		return
	}

	var node *TreeNode
	var lvSize int
	queue := []*TreeNode{root}

	for len(queue) > 0 {
		lvSize = len(queue)
		res = append(res, math.MinInt32) // 先赋予一个最小值

		for range lvSize {
			node = queue[0]
			queue = queue[1:]

			// 比大，因为是 bfs，所以直接和 res 中最后一个元素比
			if res[len(res)-1] < node.Val {
				res[len(res)-1] = node.Val
			}

			if node.Left != nil {
				queue = append(queue, node.Left)
			}
			if node.Right != nil {
				queue = append(queue, node.Right)
			}
		}
	}
	return
}

// 递归方法
func largestValues_Recursive(root *TreeNode) (res []int) {
	var dfs func(*TreeNode, int)
	dfs = func(node *TreeNode, depth int) {
		if node == nil {
			return
		}
		if len(res) == depth {
			res = append(res, math.MinInt32) // 赋予最小值
		}

		res[depth] = max(res[depth], node.Val) // 比大

		dfs(node.Left, depth+1)
		dfs(node.Right, depth+1)
	}

	dfs(root, 0)
	return
}
