// https://leetcode.cn/problems/binary-tree-level-order-traversal-ii/
// m

package main

func levelOrderBottom(root *TreeNode) (res [][]int) {
	if root == nil {
		return
	}

	var level []int
	var node *TreeNode
	var levelSize int
	queue := []*TreeNode{root}

	for len(queue) > 0 {
		level = []int{}
		levelSize = len(queue)

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

	// 比 102 多了这一步：反转次序
	for l, r := 0, len(res)-1; l < r; l, r = l+1, r-1 {
		res[l], res[r] = res[r], res[l]
	}

	return
}
