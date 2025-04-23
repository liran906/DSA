// https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
// m

package main

func connect(root *Node) *Node {
	if root == nil {
		return root
	}

	var pnode *Node // p for previous
	var node *Node
	var lvSize int
	queue := []*Node{root}

	for len(queue) > 0 {
		pnode = nil // 初始化为nil
		lvSize = len(queue)
		for range lvSize {
			node = queue[0]
			queue = queue[1:]

			if pnode != nil {
				pnode.Next = node // 上个节点指向当前节点
			}

			pnode = node // 指针指向当前节点

			if node.Left != nil {
				queue = append(queue, node.Left)
			}
			if node.Right != nil {
				queue = append(queue, node.Right)
			}
		}
	}
	return root
}

// 简略版
func connect_concise(root *Node) *Node {
	if root == nil {
		return root
	}

	var node *Node
	var lvSize int
	queue := []*Node{root}

	for len(queue) > 0 {
		lvSize = len(queue)
		for i := range lvSize {
			// 处理 next 指针
			if i < lvSize-1 {
				queue[i].Next = queue[i+1]
			}

			node = queue[i]
			if node.Left != nil {
				queue = append(queue, node.Left)
				queue = append(queue, node.Right) // 因为是完美二叉树
			}
		}
		// 处理 queue
		queue = queue[lvSize:]
	}
	return root
}

// 递归方法，优雅，实在是优雅~
func connect_Recursive(root *Node) *Node {
	if root == nil || root.Left == nil {
		return root
	}

	// 连接左子树 -> 右子树
	root.Left.Next = root.Right

	// 跨子树连接：右子树 -> 下一棵左子树
	if root.Next != nil {
		root.Right.Next = root.Next.Left
	}

	// 递归左右子树
	connect_Recursive(root.Left)
	connect_Recursive(root.Right)

	return root
}
