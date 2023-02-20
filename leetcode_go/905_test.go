package leetcode

import (
	"fmt"
	"testing"
)

/**
3,1,2,4
i=0 j=1 [3,1,2,4]
i=1 j=2 [2,1,3,4]
i=2 j=3 [2,4,3,1]
*/

func sortArrayByParity(nums []int) []int {
	// 双指针,i指遍历位置,j指奇偶分界线
	i, j := -1, 0
	for ; j <= len(nums)-1; j++ {
		// 先找偶奇分界线 i指向第一个奇数
		if i == -1 {
			if nums[j]%2 == 0 {
				continue
			} else {
				i = j
			}
		}
		if nums[j]%2 == 0 {
			// 偶数,当前位置 与i交换
			nums[i], nums[j] = nums[j], nums[i]
			i += 1
		}
	}
	return nums
}

func Test_905(t *testing.T) {
	num := []int{3, 1, 2, 4}
	// num := []int{1, 2}
	res := sortArrayByParity(num)
	fmt.Println(res)
}
