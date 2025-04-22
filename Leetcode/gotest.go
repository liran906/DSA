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
	t6 := &TreeNode{Val: 0, Left: t4, Right: t5}

	fmt.Println(levelOrder_2(t6))
}

func levelOrder_2(root *TreeNode) (res [][]int) {
	if root == nil {
		return
	}

	queue := []*TreeNode{root}
	var node *TreeNode
	var level []int

	for len(queue) > 0 {
		levelSize := len(queue)
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
