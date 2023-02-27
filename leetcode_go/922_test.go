package leetcode

import (
	"fmt"
	"testing"
)

func sortArrayByParityII(nums []int) []int {
	i, k := 0, 0
	for i < len(nums) {
		if nums[i]%2 == i%2 {
			i += 1
			continue
		}
		mod := i % 2
		for k = i + 1; k < len(nums); k += 2 {
			if nums[k]%2 == mod {
				nums[i], nums[k] = nums[k], nums[i]
				break
			}
		}
	}
	return nums
}

func Test_922(t *testing.T) {
	// nums := []int{4, 2, 5, 7}
	nums := []int{1, 2}

	res := sortArrayByParityII(nums)
	fmt.Println(res)
}
