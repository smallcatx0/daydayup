package leetcode

import (
	"fmt"
	"testing"
)

/**
质数个数的全排列 * 非质数个数的全排列
*/

const mod = 1e9 + 7

func numPrimeArrangements(n int) int {
	p := 0
	for i := 2; i <= n; i++ {
		if isPrime(i) {
			p++
		}
	}
	return jie(p) * jie(n-p) % mod
}

func isPrime(n int) bool {
	for i := 2; i*i <= n; i++ {
		if n%i == 0 {
			return false
		}
	}
	return true
}

func jie(x int) int {
	f := 1
	for i := 1; i <= x; i++ {
		f = f * i % mod
	}
	return f
}

func Test_1175(t *testing.T) {
	n := 5
	ret := numPrimeArrangements(n)
	fmt.Println(ret)
}
