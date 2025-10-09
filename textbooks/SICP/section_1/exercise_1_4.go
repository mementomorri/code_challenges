package main

import "fmt"

func Plus(a, b int) int {
	return a + b
}

func Minus(a, b int) int {
	return a - b
}

func APlusAbsB(a, b int) int {
	if b >= 0 {
		return Plus(a, b)
	} else {
		return Minus(a, b)
	}
}

func main() {
	fmt.Println(APlusAbsB(2, -2))
	fmt.Println(APlusAbsB(2, 3))
	fmt.Println(APlusAbsB(2, 0))
}
