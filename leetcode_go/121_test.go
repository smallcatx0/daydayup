package leetcode

import (
	"fmt"
	"testing"
)

func maxProfit(prices []int) int {
	low, maxP := prices[0], 0
	for _, v := range prices {
		if v < low {
			low = v
		}
		if n := v - low; n > maxP {
			maxP = n
		}
	}
	return maxP
}

func Test_121(t *testing.T) {
	p := []int{7, 1, 5, 3, 6, 4}
	res := maxProfit(p)
	fmt.Println(res)
}
