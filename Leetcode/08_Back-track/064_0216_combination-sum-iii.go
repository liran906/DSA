// https://leetcode.cn/problems/combination-sum-iii/description/
// m

package backtrack

func combinationSum3(k int, n int) (ans [][]int) {
	var path []int
	var sum int

	var bt func(int)
	bt = func(start int) {
		if len(path) == k {
			if sum == n {
				comb := append([]int{}, path...) // 拷贝当前组合
				ans = append(ans, comb)
			}
			return // 不管是否满足和为 n，递归终止
		}

		for i := start; i <= 9; i++ {
			// 剪枝优化：如果当前和加上 i 已经大于 n，提前结束循环
			if sum+i > n {
				break
			}

			path = append(path, i) // 做选择
			sum += i

			bt(i + 1) // 递归进入下一层，数字不能重复，所以 start+1

			// 回溯
			path = path[:len(path)-1]
			sum -= i
		}
	}

	bt(1)
	return
}
