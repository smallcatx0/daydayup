package leetcode

import (
	"fmt"
	"sort"
	"testing"
)

func heightChecker(heights []int) int {
	oldH := make([]int, len(heights))
	copy(oldH, heights)
	sort.Ints(heights)
	// fmt.Println(oldH, heights)
	ret := 0
	for i := 0; i < len(heights); i++ {
		if oldH[i] != heights[i] {
			ret += 1
		}
	}
	return ret
}

func heightChecker_1(heights []int) int {
	ret := 0
	if len(heights) == 0 {
		return 0
	}
	for i := 0; i < len(heights); i++ {
		min := heights[i]
		for j := i + 1; j < len(heights); j++ {
			fmt.Printf("%d > %d: %v \n", min, heights[j], heights[j] < min)
			if heights[j] < min {
				ret += 1
				break
			}
		}
	}
	return ret
}

func Test_1051(t *testing.T) {
	h := []int{1, 3, 2, 4}
	// ret := heightChecker(h)
	ret := heightChecker_1(h)
	fmt.Println(ret)
}
