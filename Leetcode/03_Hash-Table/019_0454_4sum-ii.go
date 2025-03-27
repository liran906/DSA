// https://leetcode.cn/problems/4sum-ii/
// m

package main

func fourSumCount(nums1, nums2, nums3, nums4 []int) (count int) {
	sum12Count := map[int]int{}

	// 计算 nums1+nums2 的所有可能和
	for _, n1 := range nums1 {
		for _, n2 := range nums2 {
			sum12Count[n1+n2]++
		}
	}

	// 计算 -(nums3+nums4) 的出现次数
	for _, n3 := range nums3 {
		for _, n4 := range nums4 {
			count += sum12Count[-n3-n4] // 不存在的key会返回0
		}
	}
	return
}
