package leetcode

import (
	"fmt"
	"testing"
)

/**
有 n 个筹码。第 i 个筹码的位置是 position[i] 。
*/
func minCostToMoveChips(position []int) int {
	evenNum := 0
	for _, v := range position {
		if v%2 == 0 {
			evenNum++
		}
	}
	oddNum := len(position) - evenNum
	if oddNum < evenNum {
		return oddNum
	} else {
		return evenNum
	}
}

func Test_1217(t *testing.T) {
	position := []int{2, 2, 2, 3, 3}
	res := minCostToMoveChips(position)

	fmt.Println(res)
}
