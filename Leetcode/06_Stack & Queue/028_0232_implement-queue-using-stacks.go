// https://leetcode.cn/problems/implement-queue-using-stacks
// e

package main

type MyQueue struct {
	in, out []int
}

func Constructor() MyQueue {
	return MyQueue{}
}

func (q *MyQueue) Push(x int) {
	q.in = append(q.in, x)
}

func (q *MyQueue) in2out() {
	for range len(q.in) {
		cur := q.in[len(q.in)-1]
		q.in = q.in[:len(q.in)-1]
		q.out = append(q.out, cur)
	}
}

func (q *MyQueue) Pop() int {
	if q.Empty() {
		return -1
	} else {
		if len(q.out) == 0 {
			q.in2out()
		}
		cur := q.out[len(q.out)-1]
		q.out = q.out[:len(q.out)-1]
		return cur
	}
}

func (q *MyQueue) Peek() int {
	if q.Empty() {
		return -1
	} else {
		if len(q.out) == 0 {
			q.in2out()
		}
		return q.out[len(q.out)-1]
	}
}

func (q *MyQueue) Empty() bool {
	return len(q.in) == 0 && len(q.out) == 0
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(x);
 * param_2 := obj.Pop();
 * param_3 := obj.Peek();
 * param_4 := obj.Empty();
 */
