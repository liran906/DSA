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

// 递归方法
func levelOrderRecursive(root *TreeNode) (res [][]int) {
	var dfs func(node *TreeNode, depth int) // 先声明出来，才能递归调用
	dfs = func(node *TreeNode, depth int) {
		if node == nil {
			return
		}

		// 如果当前层还没添加
		if depth == len(res) {
			res = append(res, []int{})
		}

		// 加入当前层
		res[depth] = append(res[depth], node.Val)

		// 递归左右子树
		dfs(node.Left, depth+1)
		dfs(node.Right, depth+1)
	}

	dfs(root, 0)
	return res
}
