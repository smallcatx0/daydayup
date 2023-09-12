package leetcode

import (
	"sort"
	"testing"
)

func findTheDistanceValue(arr1 []int, arr2 []int, d int) int {
	sort.Ints(arr2)
	// 二分查找
	count := 0
	for _, v := range arr1 {
		if !isInsec(arr2, v-d, v+d) {
			count++
		}
	}
	return count
}

// 查找数组中是否存在区间内置
func isInsec(arr []int, low, high int) bool {
	l, r := 0, len(arr)-1
	for l <= r {
		mid := l + (r-l)/2
		if arr[mid] >= low && arr[mid] <= high {
			return true
		} else if arr[mid] < low {
			l = mid + 1
		} else if arr[mid] > low {
			r = mid - 1
		}
	}
	return false
}
func Test_1385(t *testing.T) {
	arr1 := []int{1, 4, 2, 3}
	arr2 := []int{-4, -3, 6, 10, 20, 30}
	res := findTheDistanceValue(arr1, arr2, 3)
	println(res)
}
