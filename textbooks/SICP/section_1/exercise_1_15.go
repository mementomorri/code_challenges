package main

import (
	"fmt"
)

func main() {
	angle := 12.15
	result := sine(angle)
	fmt.Println(result)
}

func abs(x float64) float64 {
	if x >= 0 {
		return x
	}
	return -x
}

func cube(x float64) float64 {
	return x * x * x
}

func p(x float64) float64 {
	fmt.Println("Applying p, x=", x)
	return 3*x - 4*cube(x)
}

func sine(angle float64) float64 {
	fmt.Println("Applying sine, ange=", angle)
	if !(abs(angle) > 0.1) {
		return angle
	}
	return p(sine(angle / 3))
}

// func p applies 5 times when sine called with angle = 12.15
//
// he function sine gives rise to a recursive process.
// In each recursive call, the angle is divided by 3 until
// its absolute value is smaller than 0.1.
// Thus the number of steps and the space required has an
// order of growth of $O(\log a)$. Note that the base of
// the logarithm is immaterial for the order of growth
// because the logarithms of different bases differ only
// by a constant factor.
