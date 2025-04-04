package main

import (
	"fmt"
)

func main() {
	h := "aabaaabaaac"
	n := "aabaaac"
	fmt.Println(strStr(h, n))
}

func strStr(haystack string, needle string) int {
	n := len(needle)
	if n == 0 {
		return 0
	} else {
		next := getNext(needle)
		hi, ni := 0, 0
		for hi < len(haystack) {
			for hi < len(haystack) && ni < n && haystack[hi] == needle[ni] {
				hi++
				ni++
			}
			if ni == n {
				return hi - n
			} else if ni > 0 {
				ni = next[ni-1]
				continue
			}
			hi++
		}
	}
	return -1
}

func getNext(str string) (next []int) {
	s := []byte(str)
	next = make([]int, len(str))
	for i, j := 0, 1; j < len(next); j++ {
		if s[i] == s[j] {
			i++
		} else {
			i = 0
		}
		next[j] = i
	}
	return
}
