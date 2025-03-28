// https://leetcode.cn/problems/4sum/
// m

package main

import "sort"

// same as 3sum.
func fourSum(nums []int, target int) (res [][]int) {
	sort.Ints(nums)
	for i := 0; i < len(nums)-3; i++ {
		if i > 0 && nums[i] == nums[i-1] {
			continue
		}
		for j := i + 1; j < len(nums)-2; j++ {
			if j > i+1 && nums[j] == nums[j-1] {
				continue
			}
			l, r := j+1, len(nums)-1
			jackpot := target - nums[i] - nums[j]
			for l < r {
				sum := nums[l] + nums[r]
				if sum < jackpot {
					l++
				} else if sum > jackpot {
					r--
				} else {
					res = append(res, []int{nums[i], nums[j], nums[l], nums[r]})
					l++
					r--
					for l < r && nums[l] == nums[l-1] {
						l++
					}
					for l < r && nums[r] == nums[r+1] {
						r--
					}
				}
			}
		}
	}
	return
}
