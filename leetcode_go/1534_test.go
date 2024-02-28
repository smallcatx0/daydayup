package leetcode

import (
	"fmt"
	"testing"
)

func countGoodTriplets(arr []int, a int, b int, c int) int {
	count := 0
	i, j := 0, 1
	for i < len(arr)-2 {
		if j == len(arr)-1 {
			i += 1
			j = i + 1
		} else if abs_dt(arr[i], arr[j]) <= a {
			for k := j + 1; k < len(arr); k++ {
				if abs_dt(arr[j], arr[k]) <= b && abs_dt(arr[i], arr[k]) <= c {
					count += 1
				}
			}
			j += 1
		} else {
			j += 1
		}
	}
	return count
}
func abs_dt(x, y int) int {
	if x > y {
		return x - y
	} else {
		return y - x
	}
}

func Test_1534(t *testing.T) {
	arr := []int{3, 0, 1, 1, 9, 7}
	a, b, c := 7, 2, 3
	res := countGoodTriplets(arr, a, b, c)
	fmt.Println(res)
}
