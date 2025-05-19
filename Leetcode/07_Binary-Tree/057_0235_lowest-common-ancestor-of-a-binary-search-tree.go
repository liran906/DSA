// https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-search-tree/description/
// m
package main

// lowestCommonAncestor 返回二叉搜索树中两个节点的最近公共祖先
// 利用 BST 的性质：左 < 根 < 右
func lowestCommonAncestor_bst(root, p, q *TreeNode) *TreeNode {
	// 确保 p.Val >= q.Val，简化后续逻辑（可选）
	if p.Val < q.Val {
		p, q = q, p
	}

	// 当前节点值大于 p 和 q，说明它们都在左子树中
	if root.Val > p.Val {
		return lowestCommonAncestor(root.Left, p, q)
	}

	// 当前节点值小于 p 和 q，说明它们都在右子树中
	if root.Val < q.Val {
		return lowestCommonAncestor(root.Right, p, q)
	}

	// 否则说明 p 和 q 分别在左右子树，或其中一个就是 root
	return root
}
