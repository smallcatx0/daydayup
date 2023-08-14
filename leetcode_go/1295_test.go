package leetcode

import (
	"fmt"
	"testing"
)

var ou = []int{1e1, 1e3}

func findNumbers(nums []int) int {
	count := 0
	for _, v := range nums {
		if v == 1e5 {
			count++
			break
		}
		for _, s := range ou {
			n := v / s
			if n > 0 && n <= 9 {
				count++
				break
			}
		}
	}
	return count
}

func Test_1295(t *testing.T) {
	nums := []int{555, 901, 482, 1771}
	res := findNumbers(nums)
	fmt.Println(res)
}
