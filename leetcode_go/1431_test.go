package leetcode

import (
	"fmt"
	"testing"
)

//
func kidsWithCandies(candies []int, extraCandies int) []bool {
	max := 0
	for i := 0; i < len(candies); i++ {
		if candies[i] > max {
			max = candies[i]
		}
	}
	res := make([]bool, len(candies))
	for i, v := range candies {
		if v+extraCandies >= max {
			res[i] = true
		}
	}
	return res
}

func Test_1431(t *testing.T) {
	candies := []int{2, 3, 5, 1, 3}
	extraCandies := 3
	res := kidsWithCandies(candies, extraCandies)
	fmt.Println(res)
}
