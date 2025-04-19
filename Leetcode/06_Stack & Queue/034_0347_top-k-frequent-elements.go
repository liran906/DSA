// https://leetcode.com/problems/top-k-frequent-elements/description/
// m
package main

import (
	"container/heap"
)

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

// Using heap
func topKFrequent_heap(nums []int, k int) []int {
	// 记录每个元素出现的次数
	freqMap := map[int]int{}
	for _, i := range nums {
		freqMap[i]++
	}

	//所有元素入堆，堆的长度为k
	h := &MinHeap{}
	heap.Init(h)
	for item, freq := range freqMap {
		heap.Push(h, [2]int{item, freq})
		if h.Len() > k {
			heap.Pop(h)
		}
	}

	//按顺序返回堆中的元素
	res := make([]int, 0, k)
	for h.Len() > 0 {
		res = append(res, heap.Pop(h).([2]int)[0])
	}
	return res
}

// Define Min Heap
type MinHeap [][2]int

func (h MinHeap) Len() int {
	return len(h)
}

func (h MinHeap) Less(i, j int) bool {
	return h[i][1] < h[j][1]
}

func (h MinHeap) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}

func (h *MinHeap) Push(x interface{}) {
	*h = append(*h, x.([2]int))
}

func (h *MinHeap) Pop() interface{} {
	toPop := (*h)[len(*h)-1]
	*h = (*h)[:len(*h)-1]
	return toPop
}
