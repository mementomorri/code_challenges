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
	return div3(x/(guess*guess), 2*guess)
}

func cube_root(guess, x float64) float64 {
	fmt.Println("current guess =", guess)
	if is_good_enough(guess, x) {
		return guess
	}
	return cube_root(improve(guess, x), x)
}

func is_good_enough(guess, x float64) bool {
	return math.Abs(math.Pow(guess, 3)-x) < relative_tolerance
}

func div3(x, y float64) float64 {
	return (x + y) / 3
}

func main() {
	fmt.Println(cube_root(1, 27))
}

// [mementomori@fedora code_challenges]$ go run textbooks/SICP_go_edition/section_1/exercise_1_8.go
// current guess = 1
// current guess = 9.666666666666666
// current guess = 6.540758356453956
// current guess = 4.570876778578707
// current guess = 3.4780192333867963
// current guess = 3.0626891086275365
// current guess = 3.001274406506175
// current guess = 3.0000005410641766
// 3.0000005410641766
