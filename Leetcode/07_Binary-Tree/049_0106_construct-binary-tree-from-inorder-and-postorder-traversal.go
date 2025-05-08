// https://leetcode.cn/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
// m
package main

// 普通递归 O(n^2)
func buildTree_(inorder []int, postorder []int) *TreeNode {
	// 如果中序遍历数组为空，说明没有节点可构造，返回 nil
	if len(inorder) == 0 {
		return nil
	}

	// 后序遍历的最后一个元素是当前子树的根节点
	root := TreeNode{Val: postorder[len(postorder)-1]}

	// 在中序遍历中找到根节点的位置，用于划分左右子树
	index := -1
	for i, v := range inorder {
		if v == root.Val {
			index = i
			break
		}
	}

	// 划分中序遍历数组：左子树和右子树
	leftSubTree_io := inorder[:index]
	rightSubTree_io := inorder[index+1:]

	// 划分后序遍历数组：
	// 左子树的后序序列长度等于左中序的长度（index），右子树是剩下的部分（除去最后一个根节点）
	leftSubTree_po := postorder[:index]
	rightSubTree_po := postorder[index : len(postorder)-1]

	// 递归构建左右子树
	root.Left = buildTree_(leftSubTree_io, leftSubTree_po)
	root.Right = buildTree_(rightSubTree_io, rightSubTree_po)

	// 返回构建好的树的根节点指针
	return &root
}

// 递归+散列表 O(n)
// 注意：这个方法只是为了展示思路，不保证能正确运行
// 原因在于：它使用切片的方式递归传递 inorder 和 postorder，
// 但索引（index）是基于原始 inorder 的索引映射（dict），
// 与当前子切片起始点不一致，会导致切片越界或逻辑错误。

func buildTree_na(inorder []int, postorder []int) *TreeNode {
	// 构建值到中序索引的映射，加快查找根节点位置
	dict := make(map[int]int)
	for i, v := range inorder {
		dict[v] = i
	}

	// 定义递归函数，参数为当前的中序和后序子数组
	var helper func([]int, []int) *TreeNode
	helper = func(io, po []int) *TreeNode {
		// 递归终止条件：如果中序为空，返回 nil
		if len(io) == 0 {
			return nil
		}

		// 当前子树的根节点是 postorder 最后一个元素
		root := TreeNode{Val: po[len(po)-1]}

		// 从原始 dict 中找出根节点在 inorder 中的索引位置
		index := dict[root.Val]

		// 尝试用 index 分割中序和后序子数组（⚠️这里会出错）
		leftSubTree_io := io[:index]             // 左子树的 inorder 子数组
		leftSubTree_po := po[:index]             // 左子树的 postorder 子数组
		rightSubTree_io := io[index+1:]          // 右子树的 inorder 子数组
		rightSubTree_po := po[index : len(po)-1] // 右子树的 postorder 子数组（去掉根）

		// 递归构建左右子树
		root.Left = helper(leftSubTree_io, leftSubTree_po)
		root.Right = helper(rightSubTree_io, rightSubTree_po)

		// 返回当前子树根节点指针
		return &root
	}

	// 从整个数组开始递归构造
	return helper(inorder, postorder)
}

// ***散列+递归 O(n)
func buildTree(inorder []int, postorder []int) *TreeNode {
	// 1. 构建一个哈希表，记录中序遍历中每个值的位置（用于在 inorder 中 O(1) 查找根节点位置）
	inorderMap := make(map[int]int)
	for i, v := range inorder {
		inorderMap[v] = i
	}

	// 2. 初始化一个全局索引，指向 postorder 中的最后一个元素（即当前树的根）
	rootIndex := len(postorder) - 1

	// 3. 定义一个递归函数 buildRoot，参数是当前 inorder 遍历的左右边界
	var buildRoot func(int, int) *TreeNode
	buildRoot = func(left, right int) *TreeNode {
		// 边界：左闭，右闭；当左>右时，子树为空
		if left > right {
			return nil
		}

		// 3.1 取 postorder[rootIndex] 作为当前子树的根节点值
		rootVal := postorder[rootIndex]
		rootIndex-- // 指向下一个子树的根

		// 3.2 在 inorder 中定位这个根节点的位置
		index := inorderMap[rootVal]

		// 3.3 创建根节点
		root := TreeNode{Val: rootVal}

		// 3.4 注意：先构建右子树，再构建左子树（因为 postorder 是从右往左处理的）
		root.Right = buildRoot(index+1, right)
		root.Left = buildRoot(left, index-1)

		return &root
	}

	// 4. 从整个中序区间开始构造（注意：这里是 inorder 的索引范围）
	return buildRoot(0, len(inorder)-1)
}
