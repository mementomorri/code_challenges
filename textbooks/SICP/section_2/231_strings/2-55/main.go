package main

import "fmt"

// This is more of ilustrative exercise.
// It's purpose is to illustrate practice of
// using the double quotation mark " with
// single quotation '.
// And it's true, sometimes it's hard to
// notice which one is start of a string
// and whic is an element of a string itself.
// Therefor, good pracitces and code style rules.

func main() {
	fmt.Println("'\"' == \"\"", "\"" == "")
	// In Go single quote is for unsigned runes
	// which solves whole double/single quote
	// problem with strings, since only double
	// quotes can be used to ctreate them.
}
