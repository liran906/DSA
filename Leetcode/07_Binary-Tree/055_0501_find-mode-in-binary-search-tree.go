// https://leetcode.cn/problems/find-mode-in-binary-search-tree/description/
// e

package main

// 用字典记录
func findMode_h(root *TreeNode) []int {
	// 因为是 bst，相当于 sort 过了，所以可以用每个元素出现次数 count 当做 key
	var (
		count   int
		prev    *TreeNode
		dict    = make(map[int][]int) // key: 频率，value: 所有值
		inorder func(*TreeNode)
	)

	inorder = func(node *TreeNode) {
		if node == nil {
			return
		}
		// 中序遍历
		inorder(node.Left)

		// 如果是第一个节点
		if prev == nil {
			count = 1
		} else if node.Val == prev.Val {
			count++
		} else {
			// 前一个值结束，记录它
			dict[count] = append(dict[count], prev.Val)
			count = 1
		}
		prev = node // 更新前驱

		inorder(node.Right)
	}

	inorder(root)

	// 最后一个值也需要加入 map
	if prev != nil {
		dict[count] = append(dict[count], prev.Val)
	}

	// 找最大频率的 key
	maxFreq := 0
	for k := range dict {
		if k > maxFreq {
			maxFreq = k
		}
	}
	return dict[maxFreq]
}

// 方法 2：不采用额外的哈希存储频率
func findMode_(root *TreeNode) []int {
	var (
		count, maxCount int             // 当前值的计数器、最大频率
		prev            *TreeNode       // 前驱节点，用于判断值是否变化
		inorder         func(*TreeNode) // 中序遍历函数
		res             []int           // 存放众数结果
	)

	inorder = func(node *TreeNode) {
		if node == nil {
			return
		}

		inorder(node.Left)

		// ====== 中序遍历主逻辑 ======
		if prev == nil {
			// 第一个节点，计数从 1 开始
			count = 1
		} else if node.Val != prev.Val {
			// 遇到不同值时，处理前一个值的计数结果
			if count > maxCount {
				maxCount = count
				res = []int{prev.Val} // 发现新的众数
			} else if count == maxCount {
				res = append(res, prev.Val) // 并列众数
			}
			count = 1 // 当前节点值与前一个不同，计数重置
		} else {
			// 当前值与前一个值相同
			count++
		}
		prev = node

		inorder(node.Right)
	}

	// ====== 执行中序遍历 ======
	inorder(root)

	// ====== 最后处理：别漏了最后一组值 ======
	if prev != nil {
		if count > maxCount {
			res = []int{prev.Val}
		} else if count == maxCount {
			res = append(res, prev.Val)
		}
	}

	return res
}

// **方法 2 改进**：不再单独处理最后一组值

// findMode 返回 BST（二叉搜索树）中所有出现频率最高的元素（众数）
// 利用中序遍历的有序特性，按升序遍历所有节点，并统计每个值的出现次数。
// 由于每个节点在遍历中被实时处理，无需额外处理最后一个节点。

func findMode(root *TreeNode) []int {
	var (
		count, maxCount int             // 当前值频率、当前最大频率
		prev            *TreeNode       // 上一个访问的节点
		res             []int           // 存储所有众数
		inorder         func(*TreeNode) // 中序遍历函数
	)

	inorder = func(node *TreeNode) {
		if node == nil {
			return
		}

		// === 左子树 ===
		inorder(node.Left)

		// === 当前节点 ===
		// 这里也可以加一个 如果 prev==nil 则 count = 1
		// 但其实现在的代码中会并入 else 的逻辑
		if prev != nil && node.Val != prev.Val {
			count = 1 // 新值出现，重置计数
		} else {
			count++ // 相同值，累计计数
		}

		// === 处理频率更新逻辑 ===
		if count > maxCount {
			maxCount = count
			res = []int{node.Val} // 出现了新的众数，重置结果集
		} else if count == maxCount {
			res = append(res, node.Val) // 与当前众数频率相同，追加
		}

		prev = node // 更新前一个节点

		// === 右子树 ===
		inorder(node.Right)
	}

	inorder(root)

	// 说明：不需要遍历后额外处理最后一个节点的频率
	// 因为我们在中序遍历“访问每个节点时”就立即更新频率与结果
	// 所以最后一个节点自然也已经被处理完毕

	return res
}
