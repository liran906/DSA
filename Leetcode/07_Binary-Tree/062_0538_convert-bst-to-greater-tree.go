// https://leetcode.cn/problems/convert-bst-to-greater-tree/
// m
package main

// convertBST 将 BST 转换为累加树（Greater Tree）
// 每个节点的值变为大于等于它的所有节点值之和
func convertBST(root *TreeNode) *TreeNode {
	sum := 0 // 全局累加和（从大到小遍历累加）

	var dfs func(*TreeNode)
	dfs = func(node *TreeNode) {
		if node == nil {
			return
		}

		// 1. 先访问右子树（因为 BST 中右子树的值比当前节点大）
		dfs(node.Right)

		// 2. 更新当前节点
		sum += node.Val // 累加当前节点值
		node.Val = sum  // 更新当前节点为累加和

		// 3. 再访问左子树（左子树的值比当前节点小）
		dfs(node.Left)
	}

	dfs(root)
	return root
}
