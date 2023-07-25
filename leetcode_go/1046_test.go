package leetcode

import (
	"fmt"
	"testing"
)

func lastStoneWeight(stones []int) int {
	for len(stones) > 1 {
		top, sec := 0, 0
		topi, seci := 0, 0
		for i, one := range stones {
			if top < one {
				seci, topi = topi, i
				sec, top = top, one
			} else if sec < one {
				sec, seci = one, i
			}
		}
		if topi > seci {
			stones = remove(stones, seci)
			stones = remove(stones, topi-1)
		} else {
			stones = remove(stones, topi)
			stones = remove(stones, seci-1)
		}
		if d := top - sec; d != 0 {
			stones = append(stones, d)
		}
		// fmt.Println(stones)
	}
	if len(stones) == 0 {
		return 0
	}
	return stones[0]
}

func remove(s []int, i int) []int {
	return append(s[:i], s[i+1:]...)
}

func Test_1046(t *testing.T) {
	stones := []int{2, 7, 4, 1, 8, 1}
	// stones := []int{1, 1, 1}
	ret := lastStoneWeight(stones)
	fmt.Println(ret)
}
