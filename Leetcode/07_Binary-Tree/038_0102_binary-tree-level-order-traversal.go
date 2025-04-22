// https://leetcode.cn/problems/binary-tree-level-order-traversal
// m
package main

// 采用两个 counter 计数判定层次边界
func levelOrder(root *TreeNode) (res [][]int) {
	if root == nil {
		return
	}

	queue := []*TreeNode{root}
	var cur *TreeNode
	remainCount := 1
	nodeCount := 0
	level := []int{}

	for len(queue) > 0 {
		cur = queue[0]
		queue = queue[1:]
		remainCount--

		level = append(level, cur.Val)

		if cur.Left != nil {
			queue = append(queue, cur.Left)
			nodeCount++
		}
		if cur.Right != nil {
			queue = append(queue, cur.Right)
			nodeCount++
		}

		if remainCount == 0 {
			remainCount = nodeCount
			nodeCount = 0
			res = append(res, level)
			level = []int{}
		}
	}
	return
}

// 更简单，每一层记录一次 size 然后进入循环
func levelOrder_2(root *TreeNode) (res [][]int) {
	if root == nil {
		return
	}

	queue := []*TreeNode{root}
	var node *TreeNode
	var level []int
	var levelSize int

	for len(queue) > 0 {
		levelSize = len(queue)
		level = []int{}
		for range levelSize {
			node = queue[0]
			queue = queue[1:]
			level = append(level, node.Val)

			if node.Left != nil {
				queue = append(queue, node.Left)
			}
			if node.Right != nil {
				queue = append(queue, node.Right)
			}
		}
		res = append(res, level)
	}
	return
}
