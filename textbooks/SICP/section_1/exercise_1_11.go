package main

func f_recur(n int64) int64 {
	if n >= 3.0 {
		return f_recur(n-1) + 2*f_recur(n-2) + 3*f_recur(n-3)
	}
	return n
}

func f_iter(n int64) int64 {
	if n >= 3.0 {
		return helper(2, 1, 0, n-2.0)
	}
	return n
}

func helper(a int64, b int64, c int64, count int64) int64 {
	if count == 0 {
		return a
	}
	return helper(a+2*b+3*c, a, b, count-1)
}
