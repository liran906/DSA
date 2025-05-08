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
	// t1 := &TreeNode{Val: 5}
	// t2 := &TreeNode{Val: 4, Right: t1}
	// t3 := &TreeNode{Val: 3}
	// t4 := &TreeNode{Val: 2, Left: t2, Right: t3}
	// t5 := &TreeNode{Val: 1}
	// t6 := &TreeNode{Val: 0, Left: t4, Right: t5}
	inorder := []int{4, 2, 1, 7, 5, 3, 8, 6, 9}
	postorder := []int{4, 2, 7, 5, 8, 9, 6, 3, 1}

	root := buildTree(inorder, postorder)
	preorder(root)
}

func buildTree(inorder []int, postorder []int) *TreeNode {
	dict := make(map[int]int)
	for i, v := range inorder {
		dict[v] = i
	}
	var helper func(int, int) *TreeNode
	helper = func(l, r int) *TreeNode {
		if l > r {
			return nil
		}
		rootVal := postorder[r]
		rootIndex := dict[rootVal]
		root := &TreeNode{Val: rootVal}

		root.Left = helper(l, rootIndex-1)
		root.Right = helper(rootIndex, r-1)

		return root
	}
	return helper(0, len(postorder)-1)
}

func preorder(root *TreeNode) {
	if root == nil {
		return
	}
	fmt.Println(root.Val)
	preorder(root.Left)
	preorder(root.Right)
}
