// The absolute tolerance of 0.001 is too
// large when computing the square root of a
// small value. For example, sqrt(0.0001) results
// in 0.03230844833048122 instead of the expected
// value 0.01, an error of over 200%.
//
// On the other hand, for very large values,
// rounding errors might make the algorithm fail
// to ever get close enough to the square root,
// in which case it will not terminate.
//
// The following program alleviates the problem
// by replacing an absolute tolerance with a
// relative tolerance.
//
// In Go sqrt_iter(0.0001) returns
// 0.0101202, which is lot
// more precise than JS.

package main

import (
	"fmt"
	"math"
)

const relative_tolerance = 0.001

func average(x, y float64) float64 {
	return (x + y) / 2
}

func improve(guess, x float64) float64 {
	return average(guess, x/guess)
}

func sqrt_iter(guess, x float64) float64 {
	fmt.Println("current guess =", guess)
	if is_good_enough(guess, x) {
		return guess
	}
	return sqrt_iter(improve(guess, x), x)
}

func is_good_enough(guess, x float64) bool {
	return math.Abs(math.Pow(guess, 2)-x) < guess*relative_tolerance
}

func main() {
	fmt.Println(sqrt_iter(1, 0.0001))
}
