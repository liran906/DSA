// https://leetcode.cn/problems/reverse-string/description/
// e

package main

func reverseString(s []byte) {
	l, r := 0, len(s)-1
	for l < r {
		s[r], s[l] = s[l], s[r]
		l++
		r--
	}
}

// concise ver:
func reverseString_(s []byte) {
	for l, r := 0, len(s)-1; l < r; l, r = l+1, r-1 {
		s[r], s[l] = s[l], s[r]
	}
}
