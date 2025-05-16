// https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/
// m

package main

// lowestCommonAncestor 在普通二叉树中查找两个节点 p 和 q 的最近公共祖先。
// 要找的情况是：
// p 和 q 不位于同一子树上（分别位于左右子树或者某一个为根节点）
func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
	// 情况 1：如果当前节点是 nil，说明到叶子节点了，返回 nil
	if root == nil {
		return nil
	}
	// 情况 2：如果当前节点是 p 或 q，说明找到了目标节点之一，返回自己
	if root == p || root == q {
		return root
	}

	// 递归查找左子树和右子树
	left := lowestCommonAncestor(root.Left, p, q)
	right := lowestCommonAncestor(root.Right, p, q)

	// 情况 3：左右子树都不为空，说明 p 和 q 分别出现在左右子树中，当前 root 就是最近公共祖先
	if left != nil && right != nil {
		return root
	}

	// 情况 4：只有一边不为空，说明公共祖先在非空那一边
	if left != nil {
		return left
	}
	return right
}
