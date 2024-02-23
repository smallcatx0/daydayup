package leetcode

import (
	"fmt"
	"testing"
)

func numWaterBottles(numBottles int, numExchange int) int {
	total := numBottles
	for numBottles >= numExchange {
		e := numBottles / numExchange
		numBottles = numBottles%numExchange + e
		total += e
	}
	return total
}

func Test_1518(t *testing.T) {
	var res int
	res = numWaterBottles(9, 3)
	fmt.Println(res)
}
