// https://leetcode.cn/problems/merge-two-binary-trees/
// e

package main

// 递归方法（第一次写的版本）
func mergeTrees_r1(root1 *TreeNode, root2 *TreeNode) *TreeNode {
	// ✅ 若两棵树都为空，直接返回 nil
	if root1 == nil && root2 == nil {
		return nil
	}

	// ✅ 初始化新节点。这里也可以不是指针，后面 return 指针
	var root *TreeNode = &TreeNode{}

	// ✅ 如果两棵树当前节点都不为空
	if root1 != nil && root2 != nil {
		root.Val = root1.Val + root2.Val                  // 值相加
		root.Left = mergeTrees(root1.Left, root2.Left)    // 递归合并左子树
		root.Right = mergeTrees(root1.Right, root2.Right) // 递归合并右子树
		return root
	}

	// ✅ 只有 root1 不为空，拷贝 root1 的整个结构（深拷贝）
	if root1 != nil {
		root.Val = root1.Val
		root.Left = mergeTrees(root1.Left, nil)
		root.Right = mergeTrees(root1.Right, nil)
		return root
	}

	// ✅ 只有 root2 不为空，拷贝 root2 的整个结构（深拷贝）
	root.Val = root2.Val
	root.Left = mergeTrees(nil, root2.Left)
	root.Right = mergeTrees(nil, root2.Right)
	return root
}

// ** 递归（复制节点的写法）**
//
// - 如果两个节点都存在，值相加，继续递归左右子树
// - 如果其中一个为 nil，直接返回另一个子树（保持原结构）
// - 最终构建出一棵新的合并树
func mergeTrees(root1 *TreeNode, root2 *TreeNode) *TreeNode {
	// 情况 1：两个节点都为空，返回 nil
	if root1 == nil && root2 == nil {
		return nil
	}

	// 情况 2：只有 root1 为空，复制 root2 节点（保留其左右子树）
	if root1 == nil {
		return &TreeNode{Val: root2.Val, Left: root2.Left, Right: root2.Right}
	}

	// 情况 3：只有 root2 为空，复制 root1 节点（保留其左右子树）
	if root2 == nil {
		return &TreeNode{Val: root1.Val, Left: root1.Left, Right: root1.Right}
	}

	// 情况 4：两个节点都不为空，合并当前节点值并递归合并左右子树
	root := &TreeNode{Val: root1.Val + root2.Val}
	root.Left = mergeTrees(root1.Left, root2.Left)
	root.Right = mergeTrees(root1.Right, root2.Right)

	return root
}

// ** 递归 **
// 对比不复制直接引用的方法
//
// - 只在两棵树都非空时创建新节点
// - 如果一棵树为 nil，则直接返回另一棵子树（复用原结构）
// ⚠️ 注意：该方法会复用原始输入树中的节点，可能导致副作用
func mergeTrees_r(root1 *TreeNode, root2 *TreeNode) *TreeNode {
	// 如果其中一棵树为空，直接返回另一棵（复用原节点）
	if root1 == nil {
		return root2
	}
	if root2 == nil {
		return root1
	}

	// 两棵树都不为空，创建新节点并递归合并左右子树
	root := &TreeNode{Val: root1.Val + root2.Val}
	root.Left = mergeTrees_r(root1.Left, root2.Left)
	root.Right = mergeTrees_r(root1.Right, root2.Right)

	return root
}

// 迭代方法（不推荐，判断逻辑相对复杂）
//
// TreeNodes 结构体：用于队列中存储对应的三个节点位置：
// tn  是当前结果树中的节点
// tn1 是原树1中的对应位置节点
// tn2 是原树2中的对应位置节点
type TreeNodes struct {
	tn  *TreeNode
	tn1 *TreeNode
	tn2 *TreeNode
}

// mergeTrees：使用 BFS 迭代方式合并两棵二叉树（Leetcode 617）
// - 对应位置节点值相加
// - 若某棵树为空，则以另一棵树为准
// - 最终返回一棵合并后的新树
func mergeTrees_i(root1 *TreeNode, root2 *TreeNode) *TreeNode {
	if root1 == nil {
		return root2
	}
	if root2 == nil {
		return root1
	}

	// 创建新根节点，值为两棵树根节点之和
	root := &TreeNode{Val: root1.Val + root2.Val}

	// 队列初始化，保存根节点三元组
	queue := []TreeNodes{
		{tn: root, tn1: root1, tn2: root2},
	}

	// BFS
	for len(queue) > 0 {
		top := queue[0]
		queue = queue[1:]

		node, node1, node2 := top.tn, top.tn1, top.tn2

		// 为了安全访问，先判断 node1/node2 是否为 nil
		var left1, left2, right1, right2 *TreeNode
		if node1 != nil {
			left1, right1 = node1.Left, node1.Right
		}
		if node2 != nil {
			left2, right2 = node2.Left, node2.Right
		}

		// 合并左子树
		node.Left = nodeSum1(left1, left2)
		// 加入到 queue
		if node.Left != nil {
			queue = append(queue, TreeNodes{
				tn: node.Left, tn1: left1, tn2: left2,
			})
		}

		// 合并右子树
		node.Right = nodeSum1(right1, right2)
		// 加入到 queue
		if node.Right != nil {
			queue = append(queue, TreeNodes{
				tn: node.Right, tn1: right1, tn2: right2,
			})
		}
	}

	return root
}

// nodeSum：用于合并两个节点，返回一个新节点
func nodeSum1(node1, node2 *TreeNode) *TreeNode {
	// 两个节点都存在：返回值相加的新节点
	if node1 != nil && node2 != nil {
		return &TreeNode{Val: node1.Val + node2.Val}
	}
	// 其中之一存在：直接复制值
	if node1 != nil {
		return &TreeNode{Val: node1.Val}
	}
	if node2 != nil {
		return &TreeNode{Val: node2.Val}
	}
	// 都不存在：返回 nil
	return nil
}
