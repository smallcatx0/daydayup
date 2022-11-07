package leetcode

import (
	"fmt"
	"testing"
)

/*
给你两个字符串 s 和 goal ，只要我们可以通过交换 s 中的两个字母得到与 goal 相等的结果，就返回 true ；否则返回 false 。
交换字母的定义是：取两个下标 i 和 j （下标从 0 开始）且满足 i != j ，接着交换 s[i] 和 s[j] 处的字符。
例如，在 "abcd" 中交换下标 0 和下标 2 的元素可以生成 "cbad" 。
*/
func buddyStrings(s string, goal string) bool {
	not := make([]int, 0, 2)
	same := 0
	mpp := [26]int{25: 0}
	db := len(s) >= 26
	for i := 0; i < len(s); i++ {
		if s[i] != goal[i] {
			not = append(not, i)
			same += 1
			if same > 2 {
				return false
			}
		}
		if !db {
			mpp[s[i]-'a'] += 1
			if mpp[s[i]-'a'] == 2 {
				db = true
			}
		}
	}
	if same == 0 {
		if db {
			return true
		} else {
			return false
		}
	}
	if same != 2 {
		return false
	}
	if s[not[0]] == goal[not[1]] && s[not[1]] == goal[not[0]] {
		return true
	} else {
		return false
	}
}

func Test_859(t *testing.T) {
	s := "abac"
	goal := "abad"
	ret := buddyStrings(s, goal)
	fmt.Println(ret)
	// fmt.Println([24]int{23: 0})
}
