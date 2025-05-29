// https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/
// e
package main

// sortedArrayToBST 将有序数组 nums 转换为高度平衡的二叉搜索树
func sortedArrayToBST(nums []int) *TreeNode {
	// 如果数组为空，返回 nil
	if len(nums) == 0 {
		return nil
	}

	// 取中间位置作为当前根节点的值（为了尽量平衡）
	n := len(nums) / 2
	root := &TreeNode{Val: nums[n]}

	// 递归构建左子树，左子树使用 nums 的左半部分
	root.Left = sortedArrayToBST(nums[:n])

	// 递归构建右子树，右子树使用 nums 的右半部分
	root.Right = sortedArrayToBST(nums[n+1:])

	// 返回当前根节点
	return root
}
