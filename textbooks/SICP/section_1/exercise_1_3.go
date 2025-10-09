package main

import (
	"fmt"
	"math"
)

func TreeSum(a, b, c float64) float64 {
	if a >= c && b >= c {
		return math.Pow(a, 2) + math.Pow(b, 2)
	} else if a >= b && c >= b {
		return math.Pow(a, 2) + math.Pow(c, 2)
	} else if b >= a && c >= a {
		return math.Pow(b, 2) + math.Pow(c, 2)
	} else {
		return 0
	}
}

func main() {
	fmt.Println("TreeSum: 3, 2, 1:", TreeSum(3, 2, 1))
	fmt.Println("TreeSum: 1, 2, 3:", TreeSum(1, 2, 3))
	fmt.Println("TreeSum: 3, 1, 2:", TreeSum(3, 1, 2))
	fmt.Println("TreeSum: 2, 2, 2:", TreeSum(2, 2, 2))
	fmt.Println("TreeSum: 1, 2, 1:", TreeSum(1, 2, 1))
}
