// https://leetcode.com/problems/top-k-frequent-elements/description/
// m
package main

func topKFrequent(nums []int, k int) []int {
	// Count frequencies
	freqMap := map[int]int{}
	for _, num := range nums {
		freqMap[num]++
	}

	// Bucket sort: freq -> list of numbers
	bucket := make([][]int, len(nums)+1)
	for num, freq := range freqMap {
		bucket[freq] = append(bucket[freq], num)
	}

	// Collect result from high frequency to low
	res := []int{}
	for i := len(bucket) - 1; i >= 0 && len(res) < k; i-- {
		if len(bucket[i]) > 0 {
			res = append(res, bucket[i]...)
		}
	}

	// Trim to k if needed (just in case)
	return res[:k]
}
