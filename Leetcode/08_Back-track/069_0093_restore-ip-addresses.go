// https://leetcode.cn/problems/restore-ip-addresses/description/
// m

package backtrack

import (
	"strconv"
	"strings"
)

func restoreIpAddresses(s string) (ans []string) {
	var path []string // 存放当前分割出的每一段 IP 片段（总共最多 4 段）

	// 回溯函数：从 s[index:] 开始尝试切分 IP 地址
	var bt func(int)
	bt = func(index int) {
		// 终止条件：如果正好切分出了 4 段，且已经用完了所有字符
		if index == len(s) && len(path) == 4 {
			ans = append(ans, strings.Join(path, ".")) // 组合成合法 IP，加进结果
			return
		}

		// 剪枝：如果段数已经 >= 4，但字符串还没用完，说明不合法，提前返回
		if len(path) >= 4 {
			return
		}

		// 每次尝试切 1 到 3 个字符作为 IP 段
		for i := index + 1; i <= index+3 && i <= len(s); i++ {
			segment := s[index:i] // 当前尝试的字符串片段

			// 非法情况：不能有前导零（但单个 "0" 是合法的）
			// eg 1.01.00.1 是非法的，但 10.10.0.1 是合法的
			if len(segment) > 1 && segment[0] == '0' {
				continue
			}

			// 字符转数字，并判断是否在 [0, 255] 范围内
			val, _ := strconv.Atoi(segment)
			if val <= 255 {
				path = append(path, segment) // 加入当前段
				bt(i)                        // 递归尝试剩下部分
				path = path[:len(path)-1]    // 回溯，撤销最后一次 append
			}
		}
	}

	bt(0) // 从索引 0 开始回溯
	return
}
