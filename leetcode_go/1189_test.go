package leetcode

import (
	"fmt"
	"testing"
)

/**
给你一个字符串 text，你需要使用 text 中的字母来拼凑尽可能多的单词 "balloon"（气球）
*/
var ballon = map[rune]int{'a': 1, 'b': 1, 'l': 2, 'o': 2, 'n': 1}

func maxNumberOfBalloons(text string) int {
	var m = map[rune]int{'a': 0, 'b': 0, 'l': 0, 'o': 0, 'n': 0}
	for _, c := range text {
		if _, ok := m[c]; ok {
			m[c]++
		}
	}
	res := len(text)
	for k, v := range m {
		n := v / ballon[k]
		if res > n {
			res = n
		}
	}
	return res
}

func Test_1189(t *testing.T) {
	text := "nlaebolko"
	res := maxNumberOfBalloons(text)

	fmt.Println(res)
}
