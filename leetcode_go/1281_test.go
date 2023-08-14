package leetcode

import (
	"fmt"
	"testing"
)

func subtractProductAndSum(n int) int {
	sum, pro := 0, 1
	for n > 0 {
		v := n % 10
		sum += v
		pro *= v
		n = n / 10
	}
	return pro - sum
}

func Test_1281(t *testing.T) {
	n := 4421
	res := subtractProductAndSum(n)
	fmt.Println(res)
}
