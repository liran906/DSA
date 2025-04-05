// https://leetcode.cn/problems/implement-stack-using-queues
// e

package main

type MyStack struct {
	q []int
}

func Constructor() MyStack {
	return MyStack{}
}

func (s *MyStack) Push(x int) {
	s.q = append(s.q, x)
}

func (s *MyStack) Pop() (cur int) {
	n := len(s.q)
	for i := range n {
		cur = s.q[0]
		s.q = s.q[1:]
		if i == n-1 {
			return
		}
		s.q = append(s.q, cur)
	}
	return // only to avoid syntax error
}

func (s *MyStack) Top() (cur int) {
	n := len(s.q)
	for range n {
		cur = s.q[0]
		s.q = s.q[1:]
		s.q = append(s.q, cur)
	}
	return
}

func (s *MyStack) Empty() bool {
	return len(s.q) == 0
}

/**
 * Your MyStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(x);
 * param_2 := obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.Empty();
 */
