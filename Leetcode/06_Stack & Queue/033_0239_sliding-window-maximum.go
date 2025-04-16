// https://leetcode.cn/problems/sliding-window-maximum/
// h

package main

// O(k*n) 会超时，过不了
func maxSlidingWindow1(nums []int, k int) []int {
	l, r := 0, k // l 开；r 闭
	m := findMax(nums[l:r])
	res := make([]int, 0, len(nums)-k+1)
	for r <= len(nums) {
		if m < l {
			m = findMax(nums[l:r]) + l
		} else if new := nums[r-1]; new > nums[m] {
			m = r - 1
		}
		res = append(res, nums[m])
		r++
		l++
	}
	return res
}

func findMax(nums []int) (cmax int) {
	for p := 0; p < len(nums); p++ {
		if nums[p] > nums[cmax] {
			cmax = p
		}
	}
	return
}

// 单调队列 O(n)
// https://programmercarl.com/0239.%E6%BB%91%E5%8A%A8%E7%AA%97%E5%8F%A3%E6%9C%80%E5%A4%A7%E5%80%BC.html
func maxSlidingWindow(nums []int, k int) []int {
	maxQ := []int{}
	n := len(nums)
	for i := 0; i < k; i++ {
		for len(maxQ) > 0 && nums[i] > maxQ[len(maxQ)-1] {
			maxQ = maxQ[:len(maxQ)-1]
		}
		maxQ = append(maxQ, nums[i])
	}

	res := []int{maxQ[0]}

	for i := 0; i < n-k; i++ {
		// pop
		toPop := nums[i]
		if toPop == maxQ[0] {
			maxQ = maxQ[1:]
		}

		// push
		for len(maxQ) > 0 && nums[k+i] > maxQ[len(maxQ)-1] {
			maxQ = maxQ[:len(maxQ)-1]
		}
		maxQ = append(maxQ, nums[k+i])
		res = append(res, maxQ[0])
	}
	return res
}

// 还有把单调队列先封装起来的方法，更清晰一些：
type MyQueue struct {
	queue []int
}

func NewMyQueue() *MyQueue {
	return &MyQueue{
		queue: make([]int, 0),
	}
}

func (m *MyQueue) Front() int {
	return m.queue[0]
}

func (m *MyQueue) Back() int {
	return m.queue[len(m.queue)-1]
}

func (m *MyQueue) Empty() bool {
	return len(m.queue) == 0
}

func (m *MyQueue) Push(val int) {
	for !m.Empty() && val > m.Back() {
		m.queue = m.queue[:len(m.queue)-1]
	}
	m.queue = append(m.queue, val)
}

func (m *MyQueue) Pop(val int) {
	if !m.Empty() && val == m.Front() {
		m.queue = m.queue[1:]
	}
}

func maxSlidingWindow0(nums []int, k int) []int {
	queue := NewMyQueue()
	length := len(nums)
	res := make([]int, 0)
	// 先将前k个元素放入队列
	for i := 0; i < k; i++ {
		queue.Push(nums[i])
	}
	// 记录前k个元素的最大值
	res = append(res, queue.Front())

	for i := k; i < length; i++ {
		// 滑动窗口移除最前面的元素
		queue.Pop(nums[i-k])
		// 滑动窗口添加最后面的元素
		queue.Push(nums[i])
		// 记录最大值
		res = append(res, queue.Front())
	}
	return res
}
