package main

import "fmt"

// fibonacci is a function that returns
// a function that returns an int.
func fibonacci() func() int {
	last, second_last := 0, 1
	return func() int {
		res := last
		last, second_last = second_last, second_last+last
		return res
	}
}

func main() {
	f := fibonacci()
	for i := 0; i < 10; i++ {
		fmt.Println(f())
	}
}
