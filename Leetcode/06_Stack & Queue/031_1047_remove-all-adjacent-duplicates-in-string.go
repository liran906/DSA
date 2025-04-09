// https://leetcode.cn/problems/remove-all-adjacent-duplicates-in-string/
// e

package main

// use stack to compare last with current
func removeDuplicates(s string) string {
	stack := []byte{}
	for i := range s {
		ch := s[i]
		if len(stack) > 0 && ch == stack[len(stack)-1] {
			stack = stack[:len(stack)-1]
		} else {
			stack = append(stack, ch)
		}
	}
	return string(stack)
}

// 双指针模拟栈
func removeDuplicates2(s string) string {
	res := []byte(s)   // 将字符串转换为字节切片，方便原地修改
	fast, slow := 0, 0 // fast 是读指针，slow 是写指针（模拟栈顶）

	for fast < len(res) {
		res[slow] = res[fast] // 将 fast 指向的字符写入 slow 位置

		// 如果当前字符和前一个字符一样，说明形成了一对重复，删除它们
		if slow > 0 && res[slow] == res[slow-1] {
			slow -= 2 // 删除重复对，相当于弹出栈顶两元素
		}

		fast++ // 移动读取指针
		slow++ // 写入完成后，移动写入指针
	}

	return string(res[:slow]) // 截取有效部分并转换回字符串
}
