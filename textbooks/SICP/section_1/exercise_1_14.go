package main

import "fmt"

func main() {
	amount := 11
	result := countChange(amount)
	fmt.Println("there are", result, "ways to make", amount, "cents change")
}

func countChange(amount int) int {
	return cc(amount, 5)
}

func cc(amount int, kindsOfCoins int) int {
	if amount == 0 {
		return 1
	} else if amount < 0 || kindsOfCoins == 0 {
		return 0
	} else {
		return cc(amount, kindsOfCoins-1) + cc(amount-firstDenomination(kindsOfCoins), kindsOfCoins)
	}
}

func firstDenomination(kindsOfCoins int) int {
	switch kindsOfCoins {
	case 1:
		return 1
	case 2:
		return 5
	case 3:
		return 10
	case 4:
		return 25
	case 5:
		return 50
	default:
		return 0
	}
}

// cc(11, 5)
// ├── cc(11, 4)
// │   ├── cc(11, 3)
// │   │   ├── cc(11, 2)
// │   │   │   ├── cc(11, 1)
// │   │   │   │   ├── cc(11, 0) -> 0
// │   │   │   │   └── cc(10, 1)
// │   │   │   │       ├── cc(10, 0) -> 0
// │   │   │   │       └── cc(9, 1)
// │   │   │   │           ├── cc(9, 0) -> 0
// │   │   │   │           └── cc(8, 1)
// │   │   │   │               ├── cc(8, 0) -> 0
// │   │   │   │               └── cc(7, 1)
// │   │   │   │                   ├── cc(7, 0) -> 0
// │   │   │   │                   └── cc(6, 1)
// │   │   │   │                       ├── cc(6, 0) -> 0
// │   │   │   │                       └── cc(5, 1)
// │   │   │   │                           ├── cc(5, 0) -> 0
// │   │   │   │                           └── cc(4, 1)
// │   │   │   │                               ├── cc(4, 0) -> 0
// │   │   │   │                               └── cc(3, 1)
// │   │   │   │                                   ├── cc(3, 0) -> 0
// │   │   │   │                                   └── cc(2, 1)
// │   │   │   │                                       ├── cc(2, 0) -> 0
// │   │   │   │                                       └── cc(1, 1)
// │   │   │   │                                           ├── cc(1, 0) -> 0
// │   │   │   │                                           └── cc(0, 1) -> 1
// │   │   │   └── cc(6, 2)
// │   │   │       ├── cc(6, 1)
// │   │   │       └── cc(1, 2)
// │   │   └── cc(1, 3)
// │   └── cc(6, 4)
// └── cc(1, 5)
//
//The time complexity of this recursive approach is exponential
