// https://leetcode.cn/problems/reverse-words-in-a-string
// m

package main

import "strings"

func reverseWords_short(s string) string {
	t := strings.Fields(s) //使用该函数可切割单个/多个空格，提取出单词

	//遍历数组的前半段直接交换即可
	for i := 0; i < len(t)/2; i++ {
		t[i], t[len(t)-1-i] = t[len(t)-1-i], t[i]
	}

	//重新使用空格连接多个单词
	new := strings.Join(t, " ")
	return (new)
}

func reverseWords(s string) string {
	ss := []byte(s)
	// deleting extra white spaces at head and tail
	l, r := 0, len(ss)-1
	for ss[l] == ' ' {
		l++
	}
	for ss[r] == ' ' {
		r--
	}
	ss = ss[l : r+1]

	// deleting extra white spaces between words
	r = 0
	for r < len(ss) {
		for r < len(ss) && ss[r] != ' ' {
			r++
		}
		l = r + 1
		for r < len(ss) && ss[r] == ' ' {
			r++
		}
		if r-l > 0 {
			ss = append(ss[:l], ss[r:]...)
			r = l // the index changes, so set r to l
		}
	}

	swap(0, len(ss)-1, ss)

	l, r = 0, 0
	for r < len(ss) {
		for r < len(ss) && ss[r] == ' ' {
			r++
		}
		l = r
		for r < len(ss) && ss[r] != ' ' {
			r++
		}
		swap(l, r-1, ss)
	}
	return string(ss)
}

// 加了个seek 函数，遍历切片查找目标 byte，主要提升熟练度用，参考意义不大
func reverseWords1(s string) string {
	ss := []byte(s)
	// deleting extra white spaces at head and tail
	l, r := 0, len(ss)-1
	seek(&l, ss, ' ', true, true)
	seek(&r, ss, ' ', true, false)
	ss = ss[l : r+1]

	// deleting extra white spaces between words
	r = 0
	for r < len(ss) {
		seek(&r, ss, ' ', false, true)
		l = r + 1
		seek(&r, ss, ' ', true, true)
		if r-l > 0 {
			ss = append(ss[:l], ss[r:]...)
			r = l // the index changes, so set r to l
		}
	}

	swap(0, len(ss)-1, ss)

	l, r = 0, 0
	for r < len(ss) {
		seek(&r, ss, ' ', true, true)
		l = r
		seek(&r, ss, ' ', false, true)
		swap(l, r-1, ss)
	}
	return string(ss)
}

func swap(l, r int, ss []byte) {
	for l < r {
		ss[l], ss[r] = ss[r], ss[l]
		l++
		r--
	}
}

func seek(p *int, word []byte, target byte, equalTarget, toRight bool) {
	if equalTarget {
		for *p >= 0 && *p < len(word) && word[*p] == target {
			if toRight {
				*p++
			} else {
				*p--
			}
		}
	} else {
		for *p >= 0 && *p < len(word) && word[*p] != target {
			if toRight {
				*p++
			} else {
				*p--
			}
		}
	}
}
