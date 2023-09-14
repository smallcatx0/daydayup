package leetcode

import (
	"fmt"
	"testing"
)

// 找下降沿
func maxProfit_122(prices []int) int {
	low, ret := prices[0], 0
	i := 0
	for ; i < len(prices)-1; i++ {
		if prices[i] > prices[i+1] {
			ret += prices[i] - low
			low = prices[i+1]
		}
	}
	return ret + prices[i] - low
}
func Test_122(t *testing.T) {
	p := []int{7, 1, 5, 3, 6, 4}
	p = []int{1, 2, 3, 4, 5, 1, 1}
	p = []int{5, 4, 3, 2, 1}
	res := maxProfit_122(p)
	fmt.Println(res)
}
