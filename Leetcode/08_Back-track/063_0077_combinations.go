// https://leetcode.cn/problems/combinations/
// m

package backtrack

func combine(n int, k int) (ans [][]int) {
	var path []int // 用于存储当前组合的临时路径

	// 回溯函数：从 startIndex 开始枚举选择数值
	var backtrack func(int)
	backtrack = func(startIndex int) {
		// 终止条件：当前路径长度等于目标长度 k，说明找到一个合法组合
		if len(path) == k {
			// 注意要复制一份 path，避免之后 path 改变影响结果
			comb := append([]int{}, path...)
			ans = append(ans, comb)
			return
		}

		// 剪枝优化：
		// 如果还需要 (k - len(path)) 个数，则最大起始点是 n - (k - len(path)) + 1
		// 否则后面就不够元素凑成 k 个了
		for i := startIndex; i <= n-(k-len(path))+1; i++ {
			// 选择当前数 i，加入路径
			path = append(path, i)

			// 递归：从 i+1 开始选择下一个数，确保组合中数值递增、无重复
			backtrack(i + 1)

			// 回溯：撤销选择，准备尝试下一个 i
			path = path[:len(path)-1]
		}
	}

	// 从 1 开始尝试构造所有组合
	backtrack(1)

	return // 返回最终结果集
}
