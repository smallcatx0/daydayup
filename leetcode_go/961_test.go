package leetcode

import (
	"fmt"
	"math/rand"
	"testing"
	"time"
)

func repeatedNTimes(nums []int) int {
	n := len(nums) / 2
	m := make(map[int]int, n/2+1)
	rand.Int()
	for _, v := range nums {
		m[v]++
		if m[v] == n {
			return v
		}
	}
	return 0
}

// 猴子算法
func repeatedNTimes_1(nums []int) int {
	n := len(nums)
	i, j := 0, 0
	for {
		i = (time.Now().Nanosecond() / 1000) % n
		j = (time.Now().Nanosecond() / 1000) % n
		// fmt.Println(i, nums[i], " :: ", j, nums[j])
		if i != j && nums[i] == nums[j] {
			return nums[i]
		}
	}
}

func Test_961(t *testing.T) {
	nums := []int{1, 2, 3, 3}
	ret := repeatedNTimes_1(nums)
	fmt.Println(ret)
}
