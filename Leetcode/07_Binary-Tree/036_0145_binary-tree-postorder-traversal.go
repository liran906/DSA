// https://leetcode.cn/problems/binary-tree-postorder-traversal/description/
// e
package main

func postorderTraversal_i(root *TreeNode) (res []int) {
	if root == nil {
		return
	}

	var cur *TreeNode

	for stack := []*TreeNode{root}; len(stack) > 0; {
		cur = stack[len(stack)-1]
		stack = stack[:len(stack)-1]

		res = append(res, cur.Val) // 注意这里的 res 会按照中右左的顺序（反序）写入，所以后面要反转次序

		if cur.Left != nil {
			stack = append(stack, cur.Left)
		}
		if cur.Right != nil {
			stack = append(stack, cur.Right)
		}
	}

	// 反转次序
	for l, r := 0, len(res)-1; l < r; l, r = l+1, r-1 {
		res[l], res[r] = res[r], res[l]
	}

	return res
}
