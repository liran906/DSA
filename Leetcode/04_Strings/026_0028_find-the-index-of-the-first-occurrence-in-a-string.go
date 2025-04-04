// https://leetcode.cn/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
// e

package main

// KMP 算法
func strStr(haystack string, needle string) int {
	n := len(needle)
	if n == 0 {
		return 0
	}
	next := getNext(needle)
	hi, ni := 0, 0
	for hi < len(haystack) {
		for hi < len(haystack) && ni < n && haystack[hi] == needle[ni] {
			hi++
			ni++
		}
		if ni == n {
			return hi - n
		}
		if ni > 0 {
			ni = next[ni-1]
		} else {
			hi++
		}
	}
	return -1
}

func getNext(str string) (next []int) {
	next = make([]int, len(str))
	for i, j := 0, 1; j < len(next); j++ {
		for str[i] != str[j] && i > 0 {
			i = next[i-1]
		}
		if str[i] == str[j] {
			i++
		}
		next[j] = i
	}
	return
}
