package main

import (
	"fmt"
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

func equal(a, b []any) bool {
	if len(a) != len(b) {
		return false
	}
	for i := range a {
		if a[i] != b[i] {
			return false
		}
	}
	return true
}

func main() {
	test1 := equal([]any{"this", "is", "a", "list"}, []any{"this", "is", "a", "list"})
	fmt.Println("['this', 'is', 'a', 'list'] == ['this', 'is', 'a', 'list']:", test1)

	// My original implementation of equal would not allow  comparing list
	// of strings with list with sub lists becauase of a strict type check,
	// we can bypass that with []any, which is practically silly, but
	// for learnin purposes it is ok

	test2 := equal([]any{"this", "is", "a", "list"}, []any{"this", []string{"is", "a"}, "list"})
	fmt.Println("['this', 'is', 'a', 'list'] == ['this', ['is', 'a'], 'list']:", test2)
}
