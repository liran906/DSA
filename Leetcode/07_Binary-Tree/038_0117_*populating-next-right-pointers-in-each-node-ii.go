// https://leetcode.cn/problems/populating-next-right-pointers-in-each-node-ii/
// m

package main

// 递归方法
func connect_ii_R(root *Node) *Node {
	// 如果 root 为空或者 root 是叶节点
	if root == nil || (root.Left == nil && root.Right == nil) {
		return root
	}

	// 第一步：链接子节点，并找出当前节点的子节点中最右边一个
	var node *Node
	// root 同时有左右子树
	if root.Left != nil && root.Right != nil {
		root.Left.Next = root.Right
		node = root.Right
		// root 只有左子树
	} else if root.Left != nil {
		node = root.Left
		// root 只有右子树
	} else {
		node = root.Right
	}

	// 第二步：找出右侧节点中，最左子节点
	// 加入一个当前指针
	cur := root.Next
	// cur 不为空
	for cur != nil {
		// cur 有左子树
		if cur.Left != nil {
			node.Next = cur.Left
			break
			// cur 只有右子树
		} else if cur.Right != nil {
			node.Next = cur.Right
			break
			// cur 没有子树
		} else {
			cur = cur.Next
		}
	}

	// 递归调用，一定要先从右边开始
	// 因为我们在连接 Left -> ? 时可能需要借助右边一连串的结构（root.Next），
	// 而这些结构还未被递归构建，必须先递归右边才能确保 root.Next.Left 之类的指针已就绪。
	connect_ii_R(root.Right)
	connect_ii_R(root.Left)
	// 返回根节点
	return root
}

// 更优雅的递归
func connect_ii_RR(root *Node) *Node {
	if root == nil {
		return nil
	}

	// 定义一个 dummy 节点，用于构造下一层链表
	dummy := &Node{}
	// tail 用来遍历，而 dummy 就是虚拟头节点
	tail := dummy

	// 遍历当前层
	for cur := root; cur != nil; cur = cur.Next {
		if cur.Left != nil {
			tail.Next = cur.Left
			tail = tail.Next
		}
		if cur.Right != nil {
			tail.Next = cur.Right
			tail = tail.Next
		}
	}

	// 递归处理下一层
	connect_ii_RR(dummy.Next)
	return root
}

// 迭代
func connect_ii(root *Node) *Node {
	// cur 指向当前正在处理的这一层的头节点
	cur := root

	// 当当前层不为空时，继续处理
	for cur != nil {
		// dummy 是“下一层链表”的虚拟头节点（不会被返回，只作为辅助）
		dummy := &Node{}
		// tail 是我们在构建下一层链表时的游标，用来动态追加 .Next
		tail := dummy

		// 遍历当前层，利用每个节点的 .Next 指针横向移动
		for ; cur != nil; cur = cur.Next {
			// 如果当前节点有左子节点，挂到 tail 后面，并更新 tail
			if cur.Left != nil {
				tail.Next = cur.Left
				tail = tail.Next
			}
			// 如果当前节点有右子节点，同样挂到 tail 后面，并更新 tail
			if cur.Right != nil {
				tail.Next = cur.Right
				tail = tail.Next
			}
		}

		// 当前层遍历完后，cur 移动到下一层的起始位置（即 dummy.Next）
		cur = dummy.Next
	}

	// 返回原始根节点
	return root
}
