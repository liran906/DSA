// https://leetcode.com/problems/binary-tree-paths/
// e

package main

import (
	"strconv"
	"strings"
)

func binaryTreePaths(root *TreeNode) (res []string) {
	// 定义一个 dfs 函数变量，接受当前节点和当前路径
	var dfs func(node *TreeNode, path []string)

	// 实现 dfs 函数
	dfs = func(node *TreeNode, path []string) {
		if node == nil {
			return // 空节点直接返回
		}

		// 当前节点值加入路径
		path = append(path, strconv.Itoa(node.Val))

		// 如果是叶子节点，说明路径到头，拼接路径加入结果
		if node.Left == nil && node.Right == nil {
			res = append(res, strings.Join(path, "->"))
			return
		}

		// 递归访问左右子树
		dfs(node.Left, path)
		dfs(node.Right, path)

		// ❗这里不需要手动回溯（即 path = path[:len(path)-1]）
		// 因为：
		// Go 的切片是引用类型，但 append(path, ...) 返回的是新切片，
		// 每次递归传入的 path 是当前路径的拷贝，
		// 后续对 path 的更改不会影响上层路径，
		// 所以每次递归天然“隔离”，无需手动回溯。
	}

	// 从根节点开始 DFS，初始路径为空切片
	dfs(root, []string{})
	return
}
