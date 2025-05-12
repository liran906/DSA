package main

import (
	"fmt"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func main() {
	t1 := &TreeNode{Val: 5}
	t2 := &TreeNode{Val: 4, Right: t1}
	t3 := &TreeNode{Val: 3}
	t4 := &TreeNode{Val: 2, Left: t2, Right: t3}
	t5 := &TreeNode{Val: 1}
	t6 := &TreeNode{Val: 0, Left: t4, Right: t5} // Tree 1

	t7 := &TreeNode{Val: 9}
	t8 := &TreeNode{Val: 8, Left: t7}
	t9 := &TreeNode{Val: 7}
	t10 := &TreeNode{Val: 6, Right: t9}
	t11 := &TreeNode{Val: 10, Left: t8, Right: t10} // Tree 2

	merged := mergeTrees(t6, t11)
	fmt.Println(merged)
}

type TreeNodes struct {
	tn  *TreeNode
	tn1 *TreeNode
	tn2 *TreeNode
}

func mergeTrees(root1 *TreeNode, root2 *TreeNode) *TreeNode {
	if root1 == nil {
		return root2
	}
	if root2 == nil {
		return root1
	}

	root := &TreeNode{Val: root1.Val + root2.Val}
	queue := []TreeNodes{
		{tn: root, tn1: root1, tn2: root2},
	}
	for len(queue) > 0 {
		top := queue[0]
		queue = queue[1:]

		node, node1, node2 := top.tn, top.tn1, top.tn2

		node.Left = nodeSum(node1.Left, node2.Left)
		if node.Left != nil {
			queue = append(queue, TreeNodes{
				tn: node.Left, tn1: node1.Left, tn2: node2.Left,
			})
		}

		node.Right = nodeSum(node1.Right, node2.Right)
		if node.Right != nil {
			queue = append(queue, TreeNodes{
				tn: node.Right, tn1: node1.Right, tn2: node2.Right,
			})
		}
	}
	return root
}

func nodeSum(node1, node2 *TreeNode) *TreeNode {
	if node1 != nil && node2 != nil {
		return &TreeNode{Val: node1.Val + node2.Val}
	}
	if node1 != nil {
		return &TreeNode{Val: node1.Val}
	}
	if node2 != nil {
		return &TreeNode{Val: node2.Val}
	}
	return nil
}
