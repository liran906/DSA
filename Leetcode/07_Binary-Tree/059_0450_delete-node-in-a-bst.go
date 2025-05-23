// https://leetcode.cn/problems/delete-node-in-a-bst/
// m

package main

// 这个写法思路、复杂度都没啥问题，就是不太优雅
func deleteNode_(root *TreeNode, key int) *TreeNode {
	// 创建一个 dummy 节点作为 root 的父节点，方便处理删除 root 的情况
	dummy := &TreeNode{Val: 999999, Left: root}

	var dfs func(node, parent *TreeNode, key int)
	dfs = func(node, parent *TreeNode, key int) {
		if node == nil {
			return
		}

		// 向左递归查找
		if node.Val > key {
			dfs(node.Left, node, key)
			return
		}

		// 向右递归查找
		if node.Val < key {
			dfs(node.Right, node, key)
			return
		}

		// 找到目标节点，开始删除
		if node.Val == key {
			if node.Left != nil && node.Right != nil {
				// 情况1：左右子树都不为空
				// 选择右子树最左节点接上左子树
				sub := node.Right
				// 把父节点的指针改为当前右子树
				if parent.Val > key {
					parent.Left = node.Right
				} else {
					parent.Right = node.Right
				}
				// 找到右子树最左节点（中序后继）
				for sub.Left != nil {
					sub = sub.Left
				}
				sub.Left = node.Left

			} else if node.Left != nil {
				// 情况2：只有左子树
				if parent.Val > key {
					parent.Left = node.Left
				} else {
					parent.Right = node.Left
				}
			} else if node.Right != nil {
				// 情况3：只有右子树
				if parent.Val > key {
					parent.Left = node.Right
				} else {
					parent.Right = node.Right
				}
			} else {
				// 情况4：是叶子节点
				if parent.Val > key {
					parent.Left = nil
				} else {
					parent.Right = nil
				}
			}
			return
		}
	}

	dfs(root, dummy, key)
	return dummy.Left
}

// **递归**
func deleteNode(root *TreeNode, key int) *TreeNode {
	// 空树直接返回 nil
	if root == nil {
		return nil
	}

	// 当前节点值大于 key，去左子树中删除
	if root.Val > key {
		root.Left = deleteNode(root.Left, key)
		// 当前节点值小于 key，去右子树中删除
	} else if root.Val < key {
		root.Right = deleteNode(root.Right, key)
		// 找到了要删除的节点
	} else {
		// 情况 1：左子树为空，直接返回右子树
		if root.Left == nil {
			return root.Right
			// 情况 2：右子树为空，直接返回左子树
		} else if root.Right == nil {
			return root.Left
			// 情况 3：左右子树都不为空
		} else {
			// 找到右子树中的最左节点（中序后继）
			successor := root.Right
			for successor.Left != nil {
				successor = successor.Left
			}
			// 将原左子树挂到 successor 的左侧
			successor.Left = root.Left

			// 返回右子树作为新的子树根节点，相当于删除当前节点
			root = root.Right
		}
	}
	// 返回更新后的当前节点（或者新的子树根）
	return root
}
