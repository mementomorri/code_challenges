package main

// The function f(n) computes 2n,
// the function g(n) computes 2^n,
// and the function h(n) computes 2^2-2,
// where the number of 2s in the chain
// of exponentiation is n.

import "fmt"

func Ackermann(x, y int64) int64 {
	fmt.Println("Current values x:", x, "y:", y)
	if y == 0 {
		return 0
	} else if x == 0 {
		return 2 * y
	} else if y == 1 {
		return 2
	} else {
		return Ackermann(x-1, Ackermann(x, y-1))
	}
}

func f(n int64) int64 {
	return Ackermann(0, n)
}

func g(n int64) int64 {
	return Ackermann(1, n)
}

func h(n int64) int64 {
	return Ackermann(2, n)
}

func k(n int64) int64 {
	return 5 * n * n
}

func main() {
	fmt.Println("Call Ackermann's function with A(1, 10):", Ackermann(1, 10))
	fmt.Println("Call Ackermann's function with A(2, 4):", Ackermann(2, 4))
	fmt.Println("Call Ackermann's function with A(3, 3):", Ackermann(3, 3))
}
