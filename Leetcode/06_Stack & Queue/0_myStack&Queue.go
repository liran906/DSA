package main

type MyStack[T any] struct {
	items []T
}

func NewMyStack[T any]() MyStack[T] {
	return MyStack[T]{}
}

func (s *MyStack[T]) Push(x T) {
	s.items = append(s.items, x)
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

func (s *MyStack[T]) IsEmpty() bool {
	return len(s.items) == 0
}

// Queue
type MyQueue[T any] struct {
	items []T
}

func NewMyQueue[T any]() MyQueue[T] {
	return MyQueue[T]{}
}

func (q *MyQueue[T]) Push(x T) {
	q.items = append(q.items, x)
}

func (q *MyQueue[T]) Pop() (T, bool) {
	var zero T
	if q.IsEmpty() {
		return zero, false
	}
	cur := q.items[0]
	q.items = q.items[1:]
	return cur, true
}

func (q *MyQueue[T]) Peek() (T, bool) {
	var zero T
	if q.IsEmpty() {
		return zero, false
	}
	return q.items[0], true
}

func (q *MyQueue[T]) IsEmpty() bool {
	return len(q.items) == 0
}
