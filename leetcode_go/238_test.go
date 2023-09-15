package leetcode

import (
	"fmt"
	"testing"
)

func productExceptSelf(nums []int) []int {
	lef := make([]int, len(nums))
	rig := make([]int, len(nums))
	i := 1
	lef[i-1] = 1
	for ; i < len(nums); i++ {
		lef[i] = lef[i-1] * nums[i-1]
	}
	rig[i-1] = 1
	i -= 2
	for ; i >= 0; i-- {
		rig[i] = rig[i+1] * nums[i+1]
	}
	for i, v := range rig {
		rig[i] = v * lef[i]
	}
	return rig
}

func productExceptSelf_1(nums []int) []int {
	ret := make([]int, len(nums))
	i := 1
	ret[0] = 1
	for ; i < len(nums); i++ {
		ret[i] = ret[i-1] * nums[i-1]
	}
	R := 1
	for i--; i >= 0; i-- {
		ret[i] = ret[i] * R
		R *= nums[i]
	}
	return ret
}

func Test_238(t *testing.T) {
	nums := []int{1, 2, 3, 4}
	res := productExceptSelf(nums)
	res = productExceptSelf_1(nums)
	fmt.Println(res)
}
