package leetcode

import (
	"fmt"
	"testing"
)

func minDeletionSize(strs []string) int {
	if len(strs) <= 1 {
		return 0
	}
	count := 0
	n := len(strs[0])
	for i := 0; i < n; i++ {
		for j := 1; j < len(strs); j++ {
			// fmt.Print(string(strs[j][i]), " ")
			if strs[j-1][i] > strs[j][i] {
				count++
				break
			}
		}
		// fmt.Println()
	}
	return count
}

func Test_944(t *testing.T) {
	strs := []string{
		"abc",
		"bce",
		"cae",
	}
	ret := minDeletionSize(strs)
	fmt.Println(ret)
}
