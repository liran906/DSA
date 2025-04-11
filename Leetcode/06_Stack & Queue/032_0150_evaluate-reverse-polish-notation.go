// https://leetcode.cn/problems/evaluate-reverse-polish-notation/description/
// m
package main

import (
	"strconv"
)

type MyStack[T any] struct {
	items []T
}

func (s *MyStack[T]) isEmpty() bool {
	return len(s.items) == 0
}

func (s *MyStack[T]) push(item T) {
	s.items = append(s.items, item)
}

func (s *MyStack[T]) pop() (T, bool) {
	var zero T
	if s.isEmpty() {
		return zero, false
	}
	cur := s.items[len(s.items)-1]
	s.items = s.items[:len(s.items)-1]
	return cur, true
}

func (s *MyStack[T]) peek() (T, bool) {
	var zero T
	if s.isEmpty() {
		return zero, false
	}
	return s.items[len(s.items)-1], true
}

func doMath(op1, op2 int, o string) int {
	switch o {
	case "+":
		return op1 + op2
	case "-":
		return op1 - op2
	case "*":
		return op1 * op2
	case "/":
		return op1 / op2
	}
	return 0
}

func evalRPN(tokens []string) int {
	s := MyStack[int]{}
	for _, t := range tokens {
		if t == "+" || t == "-" || t == "*" || t == "/" {
			op2, _ := s.pop() // 注意顺序，1 和 2 是反的
			op1, _ := s.pop()
			s.push(doMath(op1, op2, t))
		} else {
			num, _ := strconv.Atoi(t)
			s.push(num)
		}
	}
	res, _ := s.pop()
	return res
}
