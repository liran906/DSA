// https://leetcode.cn/problems/letter-combinations-of-a-phone-number/
// m

package backtrack

import "strings"

func letterCombinations(digits string) (res []string) {
	if digits == "" {
		return // 如果输入为空，直接返回空结果
	}

	// 数字到字母的映射，模拟手机按键
	mps := map[string][]string{
		"2": {"a", "b", "c"},
		"3": {"d", "e", "f"},
		"4": {"g", "h", "i"},
		"5": {"j", "k", "l"},
		"6": {"m", "n", "o"},
		"7": {"p", "q", "r", "s"},
		"8": {"t", "u", "v"},
		"9": {"w", "x", "y", "z"},
	}

	var (
		path []string        // 当前组合路径
		bt   func(index int) // 回溯函数：从第 index 个数字开始处理
	)

	// 回溯函数定义
	bt = func(index int) {
		if index == len(digits) {
			// 所有数字都处理完了，组合完成，加入结果
			res = append(res, strings.Join(path, ""))
			return
		}

		curr := string(digits[index])  // 当前处理的数字字符
		for _, ch := range mps[curr] { // 遍历该数字对应的所有字母
			path = append(path, ch)   // 做选择
			bt(index + 1)             // 递归处理下一个数字
			path = path[:len(path)-1] // 回溯，撤销选择
		}
	}

	bt(0) // 从第 0 个数字开始回溯
	return
}
