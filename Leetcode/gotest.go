package main

import "fmt"

func main() {
	reverseStr("test")
}

func reverseStr(s string) {
	fmt.Println(s)
	fmt.Println([]byte(s))
}
