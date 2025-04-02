package main

import (
	"fmt"
)

func main() {
	fmt.Println(recursive_sum(100))
}

func recursive_sum(num int) int {
	if num == 1 {
		return 1
	} else {
		return num + recursive_sum(num-1)
	}
}
