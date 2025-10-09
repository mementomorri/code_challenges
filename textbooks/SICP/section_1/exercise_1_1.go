package main

import "fmt"

func main() {
	fmt.Println(10)
	fmt.Println(5 + 3 + 4)
	fmt.Println(9 - 1)
	fmt.Println(6 / 2)
	fmt.Println(2*4 + (4 - 6))
	const a = 3
	const b = a + 1
	fmt.Println(a + b + a*b)
	fmt.Println(a == b)
	if b > a && b < a*b {
		fmt.Println("branch B:", b)
	} else {
		fmt.Println("branch A", a)
	}
	if a == 4 {
		fmt.Println(6)
	} else if b == 4 {
		fmt.Println(6 + 7 + a)
	} else {
		fmt.Println(25)
	}
	var i int = 2
	if b > a {
		i += b
	} else {
		i += a
	}
	fmt.Println("i=", i)
	var i2 int = a + 1
	if a > b {
		fmt.Println(i2 * a)
	} else if a < b {
		fmt.Println(i2 * b)
	} else {
		fmt.Println(i2 * (-1))
	}
}
