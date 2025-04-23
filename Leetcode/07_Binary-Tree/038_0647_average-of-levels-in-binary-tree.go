// https://leetcode.cn/problems/average-of-levels-in-binary-tree/description/
// e
package main

func averageOfLevels(root *TreeNode) (res []float64) {
	if root == nil {
		return
	}

	var node *TreeNode
	var lvSum int
	var lvSize int
	queue := []*TreeNode{root}

	for len(queue) > 0 {
		lvSize = len(queue)
		for range lvSize {
			node = queue[0]
			queue = queue[1:]
			if node.Left != nil {
				queue = append(queue, node.Left)
			}
			if node.Right != nil {
				queue = append(queue, node.Right)
			}
			lvSum += node.Val
		}
		res = append(res, float64(lvSum)/float64(lvSize))
		lvSum = 0
	}
	return
}
