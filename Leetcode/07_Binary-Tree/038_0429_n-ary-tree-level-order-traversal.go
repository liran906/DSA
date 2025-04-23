// https://leetcode.cn/problems/n-ary-tree-level-order-traversal/description/
// m

package main

type Node struct {
	Val      int
	Children []*Node
	Left     *Node // 这是为了 038_0116
	Right    *Node // 这是为了 038_0116
	Next     *Node // 这是为了 038_0116
}

func levelOrder_(root *Node) (res [][]int) {
	if root == nil {
		return
	}

	var node *Node
	var lvSize int
	var level []int
	queue := []*Node{root}

	for len(queue) > 0 {
		lvSize = len(queue)
		level = []int{}

		for range lvSize {
			node = queue[0]
			queue = queue[1:]

			if len(node.Children) > 0 {
				queue = append(queue, node.Children...)
			}

			level = append(level, node.Val)
		}
		res = append(res, level)
	}
	return
}

// 递归方法
func levelOrder_Recursive(root *Node) (res [][]int) {
	var dfs func(node *Node, depth int)
	dfs = func(node *Node, depth int) {
		if node == nil {
			return
		}

		// 如果当前层还没添加
		if depth == len(res) {
			res = append(res, []int{})
		}

		// 节点值加入当前层
		res[depth] = append(res[depth], node.Val)

		// 递归子节点
		for i := range len(node.Children) {
			dfs(node.Children[i], depth+1)
		}
	}
	dfs(root, 0)
	return
}
