// https://leetcode.cn/problems/reverse-string-ii/description/
// e

package main

func reverseStr(s string, k int) string {
	sb := []byte(s)
	l, r := 0, k-1
	for l < len(sb)-1 {
		if r > len(sb)-1 {
			r = len(sb) - 1
		}
		reverse(sb, l, r)
		l += 2 * k
		r += 2 * k
	}
	return string(sb)
}

func reverse(s []byte, l int, r int) {
	for l < r {
		s[l], s[r] = s[r], s[l]
		l++
		r--
	}
}
