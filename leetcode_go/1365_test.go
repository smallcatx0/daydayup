package leetcode

import (
	"fmt"
	"sort"
	"testing"
)

func smallerNumbersThanCurrent(nums []int) []int {
	numcp := make([]int, len(nums))
	copy(numcp, nums)
	sort.Ints(nums)
	for i, v := range numcp {
		// 二分查找
		p := sortedFind(v, nums)
		for p > 0 && nums[p-1] == nums[p] {
			p -= 1
		}
		numcp[i] = p
	}
	return numcp
}

func sortedFind(v int, arr []int) int {
	i, j := 0, len(arr)-1
	m := 0
	for i <= j {
		m = j - (j-i)/2
		if arr[m] == v {
			return m
		} else if arr[m] > v {
			j = m - 1
		} else {
			i = m + 1
		}
	}
	return -1
}

func Test_1365(t *testing.T) {
	nums := []int{8, 1, 2, 2, 3}
	res := smallerNumbersThanCurrent(nums)
	fmt.Println(res)
	// sort.Ints(nums)
	// fmt.Println(nums)
	// i := find(1, nums)
	// fmt.Println(i)
}
