// https://leetcode.com/problems/combination-sum/
// m

package backtrack

import "sort"

func combinationSum(candidates []int, target int) (ans [][]int) {
	sort.Ints(candidates) // 先排序，便于剪枝优化
	var path []int        // 存储当前组合路径

	var backtrack func(remaining int, index int)
	backtrack = func(remaining int, index int) {
		if remaining == 0 {
			// 找到一组解，深拷贝 path 保存
			ans = append(ans, append([]int{}, path...))
			return
		}

		for i := index; i < len(candidates); i++ {
			// 剪枝：若当前值已超过目标值，后面的值也不可能满足
			if candidates[i] > remaining {
				return
			}
			// 选择当前数
			path = append(path, candidates[i])
			// 注意这里传 i（不是 i+1）允许重复选当前元素
			backtrack(remaining-candidates[i], i)
			// 回溯
			path = path[:len(path)-1]
		}
	}

	backtrack(target, 0)
	return
}
