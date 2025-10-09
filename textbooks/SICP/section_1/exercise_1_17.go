package main

import "fmt"

func main() {
	a := 5
	b := 6
	fmt.Println("Run Mult(a, b) for a=", a, "and b=", b)
	fmt.Println("Result:", Mult(a, b))
}

// func Mult(a, b int) int {
// 	if b == 0 {
// 		return 0
// 	} else {
// 		return a + mult(a, b-1)
// 	}
// }

func Mult(a, b int) int {
	return MultIter(a, b, 0)
}

func MultIter(a, b int, acc int) int {
	if b == 0 {
		return acc
	} else {
		return MultIter(a, b-1, a+acc)
	}
}

func Double(a int) int {
	return a + a
}

func Half(a int) int {
	return a / 2
}
