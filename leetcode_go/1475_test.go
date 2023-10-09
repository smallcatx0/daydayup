package leetcode

import (
	"fmt"
	"testing"
)

func finalPrices(prices []int) []int {
	l := len(prices)
	ret := make([]int, l)
	st := []int{0}
	for i := l - 1; i >= 0; i-- {
		for len(st) > 1 && st[len(st)-1] > prices[i] {
			st = st[:len(st)-1]
		}
		ret[i] = prices[i] - st[len(st)-1]
		st = append(st, prices[i])
	}
	return ret
}
func Test_1475(t *testing.T) {
	p := []int{8, 4, 6, 2, 3}
	res := finalPrices(p)
	fmt.Println(res)
}
