package main

import "fmt"

type Callable func()

func p() Callable { return p() }

func test(x int, y Callable) Callable {
	if x != 0 {
		return y
	}
	return y
}

func main() {
	fmt.Println(test(9, p()))
}
