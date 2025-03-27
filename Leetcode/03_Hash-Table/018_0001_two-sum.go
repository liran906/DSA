// https://leetcode.cn/problems/two-sum/
// e

package main

func twoSum(nums []int, target int) []int {
	dict := make(map[int]int)
	for i, v := range nums {
		if val, exists := dict[target-v]; exists {
			return []int{i, val}
		}
		dict[v] = i
	}
	return []int{}
}
