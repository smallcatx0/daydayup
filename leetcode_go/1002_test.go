package leetcode

import (
	"fmt"
	"testing"
)

func commonChars(words []string) []string {
	l := len(words)
	ret := []string{}
	m := [2][26]int{}
	empt := [26]int{}
	k := 0
	for _, c := range words[0] {
		m[k][c-'a']++
	}
	retM := m[0]
	for i := 1; i < l; i++ {
		k = (k + 1) % 2
		m[k] = empt // 清空上次统计
		for _, c := range words[i] {
			m[k][c-'a']++
		}
		// 找出m中相同的字母频次 与结果集对比
		for i := 0; i < 26; i++ {
			retM[i] = minInts(m[0][i], m[1][i], retM[i])
		}
	}
	for k, v := range retM {
		for i := 0; i < v; i++ {
			ret = append(ret, string(rune(k+'a')))
		}
	}
	return ret
}

func minInts(x ...int) int {
	m := x[0]
	for i := 1; i < len(x); i++ {
		if m > x[i] {
			m = x[i]
		}
	}
	return m
}

func Test_1002(t *testing.T) {
	// words := []string{"bella", "label", "roller"}
	words := []string{"bella"}
	res := commonChars(words)
	fmt.Println(res)
}
