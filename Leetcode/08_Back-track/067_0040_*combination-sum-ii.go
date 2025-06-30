// https://leetcode.cn/problems/combination-sum-ii/description/
// m

package backtrack

import "sort"

func combinationSum2(candidates []int, target int) [][]int {
	var res [][]int
	var path []int

	// 先排序，让重复的元素相邻，方便去重处理
	sort.Ints(candidates)

	// 回溯函数：从 index 开始，尝试组合
	var backtrack func(start int, remaining int)
	backtrack = func(start int, remaining int) {
		if remaining == 0 {
			// 找到一个合法组合，复制当前 path 加入结果
			comb := append([]int{}, path...)
			res = append(res, comb)
			return
		}

		for i := start; i < len(candidates); i++ {
			// 剪枝1：同层中，如果当前元素和前一个相同，跳过（避免重复组合）
			// 比如示例 1 中，如果没有这一行，会出现 2 个 1 2 5 和 1 7 （因为有 2 个 1）
			// 所以要跳过同一层递归栈中的相同元素
			if i > start && candidates[i] == candidates[i-1] {
				continue
			}

			// 剪枝2：已经超出目标，直接 break（因为是升序的）
			if candidates[i] > remaining {
				return
			}

			// 选择当前元素
			path = append(path, candidates[i])

			// 递归：注意 i+1，表示“下一个位置开始”，避免重复使用当前数字
			backtrack(i+1, remaining-candidates[i])

			// 回溯：撤销选择
			path = path[:len(path)-1]
		}
	}

	// 3️⃣ 从下标 0 开始回溯
	backtrack(0, target)

	return res
}
