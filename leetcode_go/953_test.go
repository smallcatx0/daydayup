package leetcode

import (
	"bytes"
	"fmt"
	"testing"
)

func isAlienSorted(words []string, order string) bool {
	m := make(map[rune]int, len(order))
	for i, c := range order {
		m[c] = i
	}
	for i := 0; i < len(words)-1; i++ {
		// if !strLt(m, words[i], words[i+1]) {
		// 	return false
		// }
		l1, l2 := len(words[i]), len(words[i+1])
		if l1 <= l2 && words[i][:l1] == words[i+1][:l1] {
			continue
		}
		if l1 > l2 && words[i][:l2] == words[i+1][:l2] {
			return false
		}
		if strCv(m, words[i]) > strCv(m, words[i+1]) {
			return false
		}
	}
	return true
}

// 字符串字典序小于
func strLt(m map[rune]int, s1, s2 string) bool {
	l1, l2 := len(s1), len(s2)
	if l1 <= l2 && s1[:l1] == s2[:l1] {
		return true
	}
	if l2 < l1 && s1[:l2] == s2[:l2] {
		return false
	}
	i := 0
	for s1[i] == s2[i] {
		i++
	}
	fmt.Println(i, string(s1[i]), string(s2[i]))
	// 找到第一个不同的字母
	return m[rune(s1[i])] < m[rune(s2[i])]
}

func strCv(m map[rune]int, s string) string {
	ret := bytes.Buffer{}
	for _, v := range s {
		ret.WriteByte(byte(m[v]))
	}
	return ret.String()
}

func Test_953(t *testing.T) {
	words := []string{"word", "word"}
	order := "worldabcefghijkmnpqstuvxyz"
	res := isAlienSorted(words, order)
	fmt.Println(res)
}
