package main

import "fmt"

func PascalTriangle(row, index int64) int64 {
	if index > row {
		return 0
	} else if index == 0 || index == row {
		return 1
	}
	return PascalTriangle(row-1, index-1) + PascalTriangle(row-1, index)
}

func main() {
	fmt.Println(PascalTriangle(4, 2))
}
