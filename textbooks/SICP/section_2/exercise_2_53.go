package main

import (
	"fmt"
	"strings"
)

func tail(lst [][]string) [][]string {
	if len(lst) == 0 {
		return nil
	}
	return lst[1:]
}

func head(lst [][]string) []string {
	if len(lst) == 0 {
		return nil
	}
	return lst[0]
}

func member(item string, x []string) []string {
	if len(x) == 0 || x == nil {
		return []string{}
	} else if item == x[0] {
		return x
	} else {
		return member(item, x[1:])
	}
}

func main() {
	test1 := member("apple", []string{"pear", "banana", "prune"})
	fmt.Println("member('apple', ['pear', 'banana', 'prune']):", test1)

	test2 := member("apple", []string{"x", "y", "apple", "banana"})
	fmt.Println("member('apple', ['x', 'y', 'apple', 'banana']):", test2)
	fmt.Println([]string{"a", "b", "c"})
	fmt.Println(strings.Split("George", ""))
	fmt.Println(tail([][]string{{"x1", "x2"}, {"y1", "y2"}}))

	fmt.Println(head([][]string{{"x1", "x2"}, {"y1", "y2"}}))
	fmt.Println(member("red", []string{"blue", "shoes", "yellow", "socks"}))
	fmt.Println(member("red", []string{"red", "shoes", "yellow", "socks"}))
}
