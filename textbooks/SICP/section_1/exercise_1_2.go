package main

import "fmt"

func main() {
	const numerator = 5 + 4 + (2 - (3 - (6 + 0.20)))
	const divisor = 3 * (6 - 2) * (2 - 7)

	fmt.Println("numerator:", numerator)
	fmt.Println("divisor:", divisor)
	fmt.Println("numerator / divisor:", numerator/divisor)
}
