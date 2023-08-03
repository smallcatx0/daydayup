package leetcode

import (
	"fmt"
	"testing"
)

func distanceBetweenBusStops(distance []int, s int, e int) int {
	n := len(distance)
	i, j := s, s
	s1, s2 := 0, 0
	for i != e || j != e {
		if i != e {
			// 顺时针
			s1 += distance[i]
			i = (i + 1) % n
		}
		if j != e {
			// 逆时针
			j = (j - 1 + n) % n
			s2 += distance[j]
		}
	}
	if s1 < s2 {
		return s1
	} else {
		return s2
	}
}

func Test_1184(t *testing.T) {
	distance := []int{1, 2, 3, 4}
	s, e := 0, 1
	ret := distanceBetweenBusStops(distance, s, e)
	fmt.Println(ret)

}
