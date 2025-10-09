package main

import (
	"fmt"
)

func main() {
	base := 2.0
	exponent := 8
	fmt.Println("Run", base, "to the", exponent, "power")
	fmt.Println("Result:", expt(base, exponent))
}

func expt(b float64, n int) float64 {
	return fast_expt(b, n, 1)
}

func expt_iter(b float64, n int, acc float64) float64 {
	if n == 0 {
		return acc
	} else {
		return expt_iter(b, n-1, b*acc)
	}
}

func fast_expt(b float64, n int, acc float64) float64 {
	fmt.Println("b=", b, "n=", n)
	if n == 0 {
		return acc
	} else if n%2 == 0 {
		return fast_expt(b*b, n/2, acc)
	} else {
		return fast_expt(b, n-1, b*acc)
	}
}
