package main

import "fmt"

func main() {
	t := isHappy(19)
	fmt.Println(t)
}

func isHappy(n int) bool {
	seen := map[int]struct{}{}
	for n != 1 {
		sum := 0
		fmt.Println(n)
		for n > 0 {
			fmt.Println(n, n%10)
			sum += (n % 10) * (n % 10)
			n = n / 10
			fmt.Println(n)
		}
		if _, exists := seen[sum]; exists {
			return false
		}
		fmt.Println("sum is ", sum)
		seen[sum] = struct{}{}
		n = sum
	}
	return true
}
