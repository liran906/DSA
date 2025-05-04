// https://leetcode.com/problems/sum-of-left-leaves/
// e

package main

// **递归方法 1
func sumOfLeftLeaves(root *TreeNode) int {
	// 定义递归函数：传入当前节点和一个布尔值 isLeft
	// isLeft 表示当前节点是否是其父节点的左子节点
	var dfs func(*TreeNode, bool) int

	dfs = func(node *TreeNode, isLeft bool) int {
		if node == nil {
			return 0 // 空节点，返回 0
		}

		// 如果当前节点是叶子节点
		if node.Left == nil && node.Right == nil {
			if isLeft {
				// 如果是左叶子节点，返回其值
				return node.Val
			}
			return 0 // 如果是右叶子或根，返回 0
		}

		// 递归处理左右子树：
		// - 左子树的 isLeft = true
		// - 右子树的 isLeft = false
		return dfs(node.Left, true) + dfs(node.Right, false)
	}

	// 初始调用：根节点本身不是左子节点
	return dfs(root, false)
}

// 递归方法 2 不再定义一个新函数
func sumOfLeftLeaves_2(root *TreeNode) int {
	if root == nil {
		return 0
	}

	sum := 0
	// 判断左孩子是否是叶子
	if root.Left != nil && root.Left.Left == nil && root.Left.Right == nil {
		sum += root.Left.Val
	}

	// 正常递归左右子树
	sum += sumOfLeftLeaves(root.Left)
	sum += sumOfLeftLeaves(root.Right)
	return sum
}

// 迭代方法
func sumOfLeftLeaves_i(root *TreeNode) (res int) {
	if root == nil {
		return 0
	}

	stack := []*TreeNode{root}
	for len(stack) > 0 {
		node := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		// 如果左不为空
		if node.Left != nil {
			// 且左子节点为叶节点
			if node.Left.Left == nil && node.Left.Right == nil {
				// 那么就加上他的值
				res += node.Left.Val
			} else {
				stack = append(stack, node.Left)
			}
		}
		if node.Right != nil {
			stack = append(stack, node.Right)
		}
	}
	return
}
