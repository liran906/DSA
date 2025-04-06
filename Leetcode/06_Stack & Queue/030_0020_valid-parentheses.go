// https://leetcode.com/problems/valid-parentheses/description/
// e

package main

// Define MyStack
type MyStack[T any] struct {
	items []T
}

func NewMyStack[T any]() MyStack[T] {
	return MyStack[T]{}
}

func (s *MyStack[T]) Push(x T) {
	s.items = append(s.items, x)
}

func (s *MyStack[T]) IsEmpty() bool {
	return len(s.items) == 0
}

func (s *MyStack[T]) Pop() (T, bool) {
	var zero T
	if s.IsEmpty() {
		return zero, false
	}
	cur := s.items[len(s.items)-1]
	s.items = s.items[:len(s.items)-1]
	return cur, true
}

func (s *MyStack[T]) Peek() (T, bool) {
	var zero T
	if s.IsEmpty() {
		return zero, false
	}
	return s.items[len(s.items)-1], true
}

// Now to the problem
func isValid(s string) bool {
	stack := MyStack[byte]{}
	paren := map[byte]byte{'(': ')', '[': ']', '{': '}'}
	for i := range s {
		ch := s[i]
		if rightP, ok := paren[ch]; ok {
			// is left parenthese
			stack.Push(rightP)
		} else {
			// is right parenthese
			actualP, ok := stack.Pop()
			if !ok || actualP != ch {
				return false
			}
		}
	}
	return stack.IsEmpty()
}
