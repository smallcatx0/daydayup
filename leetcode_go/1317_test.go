package leetcode

import (
	"fmt"
	"testing"
)

func getNoZeroIntegers(n int) []int {
	for i := 1; i < n; i++ {
		if noZeroValid(i) && noZeroValid(n-i) {
			return []int{i, n - i}
		}
	}
	return nil
}

func noZeroValid(n int) bool {
	for n > 1 {
		if n%10 == 0 {
			return false
		}
		n = n / 10
	}
	return true
}
func Test_1317(t *testing.T) {
	n := 11
	res := getNoZeroIntegers(n)
	fmt.Println(res)
	fmt.Println(noZeroValid(11101))
}
