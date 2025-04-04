// https://leetcode.cn/problems/repeated-substring-pattern/description/
// e

package main

import "strings"

// 把给的字符串*2, 扣除首尾第一个字符如果还包含给的字符串本身，则返回 true
func repeatedSubstringPattern(s string) bool {
	return strings.Contains((s + s)[1:len(s)*2-1], s)
}

// KMP算法更加高效
func repeatedSubstringPattern_KMP(s string) bool {
	// 首先算出 next
	n := len(s)
	next := make([]int, len(s))
	i := 0
	for j := 1; j < n; j++ {
		for i > 0 && s[i] != s[j] {
			i = next[i-1]
		}
		if s[i] == s[j] {
			i++
		}
		next[j] = i
	}

	// 然后判断 len(s) 能否被 len(s) - next[-1] 整除
	return next[n-1] > 0 && n%(n-next[n-1]) == 0
}
