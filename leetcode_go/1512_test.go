package leetcode

import (
	"fmt"
	"testing"

	"github.com/stretchr/testify/assert"
)

// 排列组合问题, n选2
func numIdenticalPairs(nums []int) int {
	nn := map[int]int{}
	for _, v := range nums {
		nn[v]++
	}
	res := 0
	for _, v := range nn {
		res += cn2(v)
	}
	return res
}

func cn2(n int) int {
	return n * (n - 1) / 2
}

func Test_cn2(t *testing.T) {
	assert.Equal(t, 0, cn2(1))
	assert.Equal(t, 1, cn2(2))
	assert.Equal(t, 3, cn2(3))
	assert.Equal(t, 6, cn2(4))
	assert.Equal(t, 28, cn2(8))
}

func Test_1512(t *testing.T) {
	nums := []int{1, 2, 3, 1, 1, 3}
	res := numIdenticalPairs(nums)
	fmt.Println(res)
}
