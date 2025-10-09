package main

// First function is recursive and so is the process.
// We call function `plus` recursively and keep on stacking
// incremention of result.
//
// Second function is recursive, but process is iterative.
// We increment variables first, and then make tail-recirsive call,
// which makes it iterative.

import "fmt"

func inc(n int64) int64 {
	return n + 1
}

func dec(n int64) int64 {
	return n - 1
}

func plus_recur(a, b int64) int64 {
	fmt.Println("Current values a:", a, "b:", b)
	if a == 0 {
		return b
	}
	return inc(plus_recur(dec(a), b))
}

func plus_iter(a, b int64) int64 {
	fmt.Println("Current values a:", a, "b:", b)
	if a == 0 {
		return b
	}
	return plus_iter(dec(a), inc(b))
}

func main() {
	fmt.Println("Start recursive process...")
	res := plus_recur(4, 5)
	fmt.Println("Result for recursive process:", res)
	fmt.Println("Start iterative process...")
	res = plus_iter(4, 5)
	fmt.Println("Result for iterative process:", res)
}
