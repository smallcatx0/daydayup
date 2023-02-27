package leetcode

import (
	"fmt"
	"testing"
)

func isLongPressedName(name string, typed string) bool {
	if name[0] != typed[0] {
		return false
	}
	j := 0
	for i := 1; i < len(typed); i++ {
		if j+1 < len(name) && typed[i] == name[j+1] {
			j += 1
		} else if typed[i] == name[j] {

		} else {
			return false
		}
	}
	return j == len(name)-1
}

func Test_925(t *testing.T) {
	name := "alexd"
	typed := "ale"
	res := isLongPressedName(name, typed)
	fmt.Println(res)
}
