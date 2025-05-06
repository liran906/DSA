// https://leetcode.cn/problems/path-sum/
// e

package main

// 递归 1
func hasPathSum_o(root *TreeNode, targetSum int) bool {
	var dfs func(*TreeNode, int, int) bool
	dfs = func(node *TreeNode, target, cur int) bool {
		if node == nil {
			return false
		}
		if node.Left == nil && node.Right == nil && cur+node.Val == target {
			return true
		}
		return dfs(node.Left, target, cur+node.Val) || dfs(node.Right, target, cur+node.Val)
	}
	return dfs(root, targetSum, 0)
}

// ** 递归 2
func hasPathSum(root *TreeNode, targetSum int) bool {
	if root == nil {
		return false
	}
	if root.Left == nil && root.Right == nil {
		return root.Val == targetSum
	}
	return hasPathSum(root.Left, targetSum-root.Val) ||
		hasPathSum(root.Right, targetSum-root.Val)
}

// 单栈+结构体
type nodeSum struct {
	node *TreeNode
	sum  int
}

func hasPathSum_i(root *TreeNode, targetSum int) bool {
	if root == nil {
		return false
	}

	stack := []nodeSum{{root, root.Val}}

	for len(stack) > 0 {
		top := stack[len(stack)-1]
		stack = stack[:len(stack)-1]

		node, sum := top.node, top.sum

		if node.Left == nil && node.Right == nil && sum == targetSum {
			return true
		}
		if node.Left != nil {
			stack = append(stack, nodeSum{node.Left, sum + node.Left.Val})
		}
		if node.Right != nil {
			stack = append(stack, nodeSum{node.Right, sum + node.Right.Val})
		}
	}
	return false
}

// 两个并行栈
func hasPathSum_i2(root *TreeNode, targetSum int) bool {
	if root == nil {
		return false
	}
	stack := []*TreeNode{root}
	cur := []int{0}
	for len(stack) > 0 {
		node := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		sum := cur[len(cur)-1]
		cur = cur[:len(cur)-1]
		if node.Left == nil && node.Right == nil && sum+node.Val == targetSum {
			return true
		}
		if node.Left != nil {
			stack = append(stack, node.Left)
			cur = append(cur, sum+node.Val)
		}
		if node.Right != nil {
			stack = append(stack, node.Right)
			cur = append(cur, sum+node.Val)
		}
	}
	return false
}
