// https://leetcode.cn/problems/intersection-of-two-arrays
// e

package main

func intersection(nums1 []int, nums2 []int) []int {
	dict := make(map[int]bool, len(nums1))
	res := []int{}
	for _, v := range nums1 {
		dict[v] = true
	}
	for _, v := range nums2 {
		if val, exists := dict[v]; exists && val {
			dict[v] = false
			res = append(res, v)
		}
	}
	return res
}

func intersection2(nums1 []int, nums2 []int) []int {
	dict := make(map[int]struct{}, len(nums1))
	res := []int{}
	for _, v := range nums1 {
		dict[v] = struct{}{}
	}
	for _, v := range nums2 {
		if _, exists := dict[v]; exists {
			delete(dict, v)
			res = append(res, v)
		}
	}
	return res
}
