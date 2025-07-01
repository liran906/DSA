// https://leetcode.cn/problems/palindrome-partitioning/description/
// m

package backtrack

// partition returns all possible palindrome partitioning of the input string.
func partition1(s string) (ans [][]string) {
	var path []string // 当前路径，保存已经选择的回文子串
	var bt func(int)  // 回溯函数，参数是当前处理的起始下标

	// 定义回溯逻辑
	bt = func(index int) {
		// 如果 index 到达字符串末尾，说明当前路径是一种合法的划分方式
		if index >= len(s) {
			// 这里要 copy 一份 path，因为 path 是全局可变切片
			ans = append(ans, append([]string{}, path...))
			return
		}

		// 枚举所有可能的划分：从 index 到 len(s)-1
		// 这里的思路是，从 index 开始，依次增加，每次取 s[index:i+1] 作为子串
		// 然后进入递归，判断从第 i+1 个字符开始的所有子串
		for i := index; i < len(s); i++ {
			// 如果 s[index:i+1] 是一个回文子串，则尝试使用它
			if isPal(s[index : i+1]) {
				// 做选择：加入当前的回文子串
				path = append(path, s[index:i+1])

				// 递归：继续从 i+1 开始划分后续字符串
				bt(i + 1)

				// 回溯：撤销选择，尝试下一个划分
				path = path[:len(path)-1]
			}
		}
	}

	// 从第 0 个字符开始回溯划分
	bt(0)
	return
}

// 判断字符串 s 是否是回文
func isPal(s string) bool {
	l, r := 0, len(s)-1
	for l <= r {
		if s[l] != s[r] {
			return false
		}
		l++
		r--
	}
	return true
}

// 优化：用动态规划提前算出回文子串

// 用动态规划提前算出字符串的所有回文子串
func partition(s string) (ans [][]string) {
	var path []string // 当前路径，保存已经选择的回文子串
	var bt func(int)  // 回溯函数，参数是当前处理的起始下标

	// 创建 palMap：palMap[i][j] 表示 s[i:j+1] 是否为回文
	palMap := make([][]bool, len(s))
	// 要先遍历一遍，把 []bool 初始化，否则后面会index error
	for i := range palMap {
		palMap[i] = make([]bool, len(s))
	}

	// 定义 calPal 函数：使用动态规划预处理所有回文子串
	// 这里是一个优化
	var calPal func()
	calPal = func() {
		// 从后往前遍历起点 i
		for i := len(s) - 1; i >= 0; i-- {
			// 从前往后遍历终点 j，确保 i <= j
			for j := i; j < len(s); j++ {
				if s[i] != s[j] {
					palMap[i][j] = false
					continue
				}
				// 情况一：单个字符 or 两个字符相同 -> 一定是回文
				if j-i <= 1 {
					palMap[i][j] = true
					continue
				}
				// 情况二：多字符，只需看中间是否是回文
				palMap[i][j] = palMap[i+1][j-1]
			}
		}
	}

	calPal()

	// 定义回溯逻辑
	bt = func(index int) {
		// 如果 index 到达字符串末尾，说明当前路径是一种合法的划分方式
		if index >= len(s) {
			// 这里要 copy 一份 path，因为 path 是全局可变切片
			ans = append(ans, append([]string{}, path...))
			return
		}

		// 枚举所有可能的划分：从 index 到 len(s)-1
		// 这里的思路是，从 index 开始，依次增加，每次取 s[index:i+1] 作为子串
		// 然后进入递归，判断从第 i+1 个字符开始的所有子串
		for i := index; i < len(s); i++ {
			// 如果 s[index:i+1] 是一个回文子串，则尝试使用它
			if palMap[index][i] {
				// 做选择：加入当前的回文子串
				path = append(path, s[index:i+1])

				// 递归：继续从 i+1 开始划分后续字符串
				bt(i + 1)

				// 回溯：撤销选择，尝试下一个划分
				path = path[:len(path)-1]
			}
		}
	}

	// 从第 0 个字符开始回溯划分
	bt(0)
	return
}
