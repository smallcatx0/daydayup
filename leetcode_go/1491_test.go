package leetcode

import (
	"fmt"
	"testing"
)

func average(salary []int) float64 {
	max, min := -1, int(10e7)
	s := 0
	for _, v := range salary {
		if max < v {
			max = v
		}
		if min > v {
			min = v
		}
		s += v
	}
	return float64(s-max-min) / float64(len(salary)-2)
}

func Test_1491(t *testing.T) {
	s := []int{6000, 5000, 4000, 3000, 2000, 1000}
	res := average(s)
	fmt.Println(res)
}
