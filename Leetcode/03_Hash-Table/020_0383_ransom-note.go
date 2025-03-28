// https://leetcode.cn/problems/ransom-note/description/
// e
package main

func canConstruct(ransomNote string, magazine string) bool {
	rmap := map[rune]int{}
	for _, v := range magazine {
		rmap[v]++
	}
	for _, v := range ransomNote {
		rmap[v]--
		if rmap[v] < 0 {
			return false
		}
	}
	return true
}
