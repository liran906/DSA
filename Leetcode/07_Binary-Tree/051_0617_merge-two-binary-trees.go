// https://leetcode.cn/problems/merge-two-binary-trees/
// e

package main

// 递归方法
func mergeTrees(root1 *TreeNode, root2 *TreeNode) *TreeNode {
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
