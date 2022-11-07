package leetcode

import (
	"fmt"
	"testing"
)

func lemonadeChange(bills []int) bool {
	m5, m10 := 0, 0
	for _, one := range bills {
		switch one {
		case 5:
			m5 += 1
		case 10:
			m5 -= 1
			m10 += 1
		case 20:
			if m10 > 0 {
				m10 -= 1
				m5 -= 0
			} else {
				m5 -= 3
			}
		}
		if m5 < 0 {
			return false
		}
	}
	return true
}

func Test_860(t *testing.T) {
	bills := []int{5, 5, 5, 10, 5, 5, 10, 20, 20, 20}
	ret := lemonadeChange(bills)
	fmt.Println(ret)
}
