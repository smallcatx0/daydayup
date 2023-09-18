package leetcode

import (
	"fmt"
	"testing"
)

// 找最低点
func canCompleteCircuit(gas []int, cost []int) int {
	l := len(gas)
	re := 0
	min, mini := int(10e5+1), 0
	for i := 0; i < l; i++ {
		re += gas[i] - cost[i]
		if re < min && gas[(i+1)%l]-cost[(i+1)%l] > 0 {
			min = re
			mini = i
		}
	}
	if re < 0 {
		return -1
	}
	return (mini + 1) % l
}
func Test_134(t *testing.T) {
	gas := []int{1, 2, 3, 4, 5}
	cost := []int{3, 4, 5, 1, 2}
	res := canCompleteCircuit(gas, cost)
	fmt.Println(res)
}
