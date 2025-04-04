package main

import (
	"dsa/pythonds/search"
	"dsa/pythonds/sort"
	"fmt"
	"math/rand"
)

func main() {
	n := 30
	alist := make([]int, n)
	for i := range n {
		alist[i] = rand.Intn(100)
	}
	fmt.Println(alist)
	alist = sort.MergeSort(alist)
	fmt.Println(alist)

	a := 21
	fmt.Println(search.BinarySearch_recursive(a, alist))
	fmt.Println(search.BinarySearch_pointer(a, alist))

	str := "abc"
	fmt.Printf("%T,%d", str[0], str[0])
}
