// https://leetcode.cn/problems/binary-tree-right-side-view/
// m

package main

// 采用两个 counter 计数判定层次边界
func rightSideView(root *TreeNode) (res []int) {
	if root == nil {
		return
	}

	queue := []*TreeNode{root}
	remainCount := 1
	nodeCount := 0
	var node *TreeNode

	for len(queue) > 0 {
		node = queue[0]
		queue = queue[1:]

		if node.Left != nil {
			queue = append(queue, node.Left)
			nodeCount++
		}
		if node.Right != nil {
			queue = append(queue, node.Right)
			nodeCount++
		}

		remainCount--
		if remainCount == 0 {
			res = append(res, node.Val)
			remainCount = nodeCount
			nodeCount = 0
		}
	}
	return
}

// 每一层记录一次 size 然后进入循环
func rightSideView_2(root *TreeNode) (res []int) {
	if root == nil {
		return
	}
	queue := []*TreeNode{root}
	var node *TreeNode
	var levelSize int

	for len(queue) > 0 {
		levelSize = len(queue)
		for i := range levelSize {
			node = queue[0]
			queue = queue[1:]
			if i == levelSize-1 {
				res = append(res, node.Val)
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
