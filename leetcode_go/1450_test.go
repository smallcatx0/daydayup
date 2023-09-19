package leetcode

import (
	"fmt"
	"testing"
)

func busyStudent(startTime []int, endTime []int, queryTime int) int {
	c := 0
	for i := 0; i < len(startTime); i++ {
		if startTime[i] <= queryTime && endTime[i] >= queryTime {
			c++
		}
	}
	return c
}

func Test_1450(t *testing.T) {
	st := []int{1, 2, 3}
	ed := []int{3, 2, 7}
	res := busyStudent(st, ed, 4)
	fmt.Println(res)
}
