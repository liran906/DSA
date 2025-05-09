// https://leetcode.com/problems/maximum-binary-tree/
// m

package main

import "sort"

/*
	不推荐

本方法使用排序 + 原索引映射的方式构造最大二叉树：
1. 对原数组进行升序排序，确保从最大值向下构造；
2. 使用 map 保存原数组中每个值的索引位置，便于判断左右子树归属；
3. 从最大值开始递归构造，每次查找比当前根值小的元素，判断其应归入左子树或右子树；
4. 每个节点最多构造一次左右子树，整体逻辑清晰，但时间复杂度为 O(n^2)。

缺点：比暴力递归更难理解，且和暴力递归差不多效率：每次构造仍需遍历已排序数组
*/
func constructMaximumBinaryTree_na(nums []int) *TreeNode {
	// 1. 构建一个 map，记录每个元素在原数组中的索引位置
	dict := make(map[int]int)
	for i, v := range nums {
		dict[v] = i
	}

	// 2. 复制原数组并升序排序，用于从大到小依次构造最大值节点
	sorted := append([]int(nil), nums...) // 不污染原数组
	sort.Ints(sorted)                     // 升序排序，最大值在最后

	// 3. 构建递归函数：尝试用当前最大值 sorted[index] 构造区间 [left, right) 中的树
	var buildNode func(l, r, index int) *TreeNode
	buildNode = func(left, right, index int) *TreeNode {
		// 边界条件：左边界 >= 右边界时，区间为空，返回 nil
		if left >= right {
			return nil
		}

		// 当前要构建的根节点是 sorted[index]
		rootVal := sorted[index]
		root := &TreeNode{Val: rootVal}
		rootPos := dict[rootVal] // 在原数组中的真实位置

		// 4. 从当前值往更小值倒着查找左右子树
		for i := index - 1; i >= 0; i-- {
			v := sorted[i]
			pos := dict[v] // 当前值在原数组中的索引

			// 尝试构建左子树：必须落在 [left, rootPos)
			if root.Left == nil && pos >= left && pos < rootPos {
				root.Left = buildNode(left, rootPos, i)
			}

			// 尝试构建右子树：必须落在 (rootPos, right)
			if root.Right == nil && pos > rootPos && pos < right {
				root.Right = buildNode(rootPos+1, right, i)
			}

			// 左右子树都构建完了就可以提前退出
			if root.Left != nil && root.Right != nil {
				break
			}
		}
		return root
	}

	// 5. 从最大的数开始构建整棵树（最大值在 sorted 最后一个元素）
	return buildNode(0, len(nums), len(nums)-1)
}

/*
	*正常递归*

1. 每次在区间 [l, r) 内查找最大值作为当前子树的根；
2. 以最大值所在的位置划分为左子树区间和右子树区间；
3. 对左右子区间递归执行相同构建过程；
4. 直到区间为空（l >= r）为止，返回 nil。

- 最坏情况下（数组递减）为 O(n^2)，因为每次找最大值都需线性扫描；
- 平均情况下接近 O(n log n)。

可读性高
*/
func constructMaximumBinaryTree_r(nums []int) *TreeNode {
	// buildRoot 构建 nums[l:r) 区间的最大二叉树
	var buildRoot func(int, int) *TreeNode
	buildRoot = func(l, r int) *TreeNode {
		// 递归终止条件：区间为空
		if l >= r {
			return nil
		}

		// 在 [l, r) 区间内查找最大值的位置
		maxPos := l
		maxVal := nums[maxPos]
		for i := l; i < r; i++ {
			if nums[i] > maxVal {
				maxVal = nums[i]
				maxPos = i
			}
		}

		// 构建根节点
		root := TreeNode{Val: maxVal}

		// 构建左右子树
		root.Left = buildRoot(l, maxPos)
		root.Right = buildRoot(maxPos+1, r)
		return &root
	}

	// 从整个数组开始构建
	return buildRoot(0, len(nums))
}

/*
	***单调递减栈*** O(n)

https://leetcode.cn/problems/maximum-binary-tree/solutions/1762400/zhua-wa-mou-si-by-muse-77-myd7/

核心思想：
1. 利用一个栈维护一组严格递减的节点；
2. 每次遍历到新节点时，将比它小的栈顶元素逐个弹出，作为它的左子树；
3. 如果栈不为空，说明当前节点应是栈顶元素的右子树；
4. 最终栈底的元素即为整棵树的根。

时间复杂度：O(n)
- 每个节点最多入栈出栈一次

空间复杂度：O(n)
- 栈中最多保留 n 个节点

优点：
- 非递归，效率高，结构稳定，非常适合面试进阶使用
*/

func constructMaximumBinaryTree(nums []int) *TreeNode {
	// 使用单调递减栈
	stack := []*TreeNode{}

	// 遍历每个数，构造对应节点
	for i := range nums {
		node := &TreeNode{Val: nums[i]}

		// 如果当前栈顶元素比当前值小，就持续弹出
		// 被弹出的元素将成为当前节点的左子树
		for len(stack) > 0 && stack[len(stack)-1].Val < node.Val {
			popped := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			node.Left = popped
		}

		// 此时栈不为空，说明当前节点应成为栈顶元素的右子树
		if len(stack) > 0 {
			stack[len(stack)-1].Right = node
		}

		// 当前节点入栈，继续维护递减栈
		stack = append(stack, node)
	}

	// 栈底的节点是整棵树的根
	return stack[0]
}
