// https://leetcode.cn/problems/path-sum-ii/
// m

package main

// 递归方法
func pathSum(root *TreeNode, targetSum int) (res [][]int) {
	var dfs func(*TreeNode, int, []int)
	dfs = func(node *TreeNode, tarSum int, path []int) {
		if node == nil {
			return
		}
		path = append(path, node.Val)
		// 到达叶子节点 且路径和满足条件
		if node.Left == nil && node.Right == nil && node.Val == tarSum {
			// 将 path 的一个拷贝（不是引用）加入结果集 res 中，
			// 确保即使之后 path 发生变化，res 中保存的路径不受影响
			res = append(res, append([]int{}, path...))
			return
		}
		// 递归左右子树
		dfs(node.Left, tarSum-node.Val, path)
		dfs(node.Right, tarSum-node.Val, path)
	}
	dfs(root, targetSum, []int{})
	return
}

// 单栈迭代方法
type nodeSum_ struct {
	node *TreeNode // 当前节点
	sum  int       // 当前剩余目标和（targetSum 减去前面节点之和）
	path []int     // 当前路径上的节点值
}

func pathSum_i(root *TreeNode, targetSum int) (res [][]int) {
	if root == nil {
		return
	}

	// 初始化栈，起点是根节点，初始 path 是空
	stack := []nodeSum_{{root, targetSum, []int{}}}

	for len(stack) > 0 {
		// 出栈一个元素
		top := stack[len(stack)-1]
		stack = stack[:len(stack)-1]

		// 解析出当前节点、剩余目标和、当前路径（追加当前节点值）
		node := top.node
		sum := top.sum - node.Val          // 直接减去当前节点的值，后面判断是否等于 0
		path := append(top.path, node.Val) // 注意这里必须 append 后复制出新路径

		// 如果是叶子节点，且恰好符合 targetSum，记录结果
		if node.Left == nil && node.Right == nil && sum == 0 {
			res = append(res, append([]int{}, path...)) // 拷贝 path，避免后续修改影响
		}

		// 压入右子节点
		if node.Right != nil {
			stack = append(stack, nodeSum_{node.Right, sum, path})
		}
		// 压入左子节点
		if node.Left != nil {
			stack = append(stack, nodeSum_{node.Left, sum, path})
		}
	}
	return
}
