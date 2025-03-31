package main

import "fmt"

func main01() {
	var input string
	var output string

	fmt.Scan(&input)

	for i := range len(input) {
		if input[i] >= '0' && input[i] <= '9' {
			output += "number"
		} else {
			output += string(input[i])
		}
	}
	fmt.Println(output)
}

func main() {
	var strByte []byte

	fmt.Scanln(&strByte)

	for i := 0; i < len(strByte); i++ {
		if strByte[i] <= '9' && strByte[i] >= '0' {
			inserElement := []byte{'n', 'u', 'm', 'b', 'e', 'r'}
			strByte = append(strByte[:i], append(inserElement, strByte[i+1:]...)...)
			i = i + len(inserElement) - 1
		}
	}

	fmt.Println(string(strByte))
}
