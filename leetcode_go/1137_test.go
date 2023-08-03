package leetcode

import (
	"fmt"
	"testing"
)

func tribonacci(n int) int {
	cache := map[int]int{
		0: 0, 1: 1, 2: 1,
	}
	return fbn(n, cache)
}

func fbn(x int, cahce map[int]int) int {
	if v, ok := cahce[x]; ok {
		return v
	}
	v := fbn(x-3, cahce) + fbn(x-2, cahce) + fbn(x-1, cahce)
	cahce[x] = v
	return v
}

func tribonacci_1(n int) int {
	if n == 0 {
		return 0
	}
	if n <= 2 {
		return 1
	}
	t0, t1, t2, t3 := 0, 0, 1, 1
	for i := 3; i <= n; i++ {

		t2, t1, t0 = t3, t2, t1
		t3 = t2 + t1 + t0
	}
	return t3
}

func Test_1137(t *testing.T) {
	n := 25
	res := tribonacci(n)
	res = tribonacci_1(n)
	fmt.Println(res)
}
