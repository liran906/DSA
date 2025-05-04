// https://leetcode.com/problems/find-bottom-left-tree-value
// m

package main

// 迭代法，层序遍历，最直观
func findBottomLeftValue(root *TreeNode) (res int) {
	queue := []*TreeNode{root}
	for len(queue) > 0 {
		size := len(queue)
		for i := range size {
			node := queue[0]
			queue = queue[1:]
			// 每一层只记录第一个节点
			if i == 0 {
				res = node.Val
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

// 递归，dfs 遍历，用闭包
func findBottomLeftValue_r(root *TreeNode) int {
	var (
		maxDepth int
		maxValue int
		dfs      func(*TreeNode, int)
	)

	// 闭包 Closure
	dfs = func(node *TreeNode, depth int) {
		if node == nil {
			return
		}

		// 只在更深一层第一次访问时更新
		if depth > maxDepth {
			maxDepth = depth
			maxValue = node.Val // 记录当前 node 的值
		}

		// 先左后右，确保最左边的节点先被访问
		dfs(node.Left, depth+1)
		dfs(node.Right, depth+1)
	}

	dfs(root, 1)
	return maxValue
}
