package leetcode

import (
	"fmt"
	"strings"
	"testing"
)

/**
给出第一个词 first 和第二个词 second，考虑在某些文本 text 中可能以 "first second third" 形式出现的情况，其中 second 紧随 first 出现，third 紧随 second 出现
*/

func findOcurrences(text string, first string, second string) []string {
	// 一次遍历 分词
	text += " "
	fs := first + " " + second
	s, pre := 0, ""
	next := false
	ret := []string{}
	for i := 0; i < len(text); i++ {
		if text[i] != ' ' {
			continue
		}
		if next {
			ret = append(ret, text[s:i])
			next = false
		}
		// fmt.Println(text[s:i])
		if pre != "" && pre+" "+text[s:i] == fs {
			next = true
		}
		pre = text[s:i]
		s = i + 1
	}
	return ret
}
func findOcurrences_1(text string, first string, second string) []string {
	words := strings.Split(text, " ")
	ret := []string{}
	for i := 1; i < len(words)-1; i++ {
		if words[i-1] == first && words[i] == second {
			ret = append(ret, words[i+1])
		}
	}
	return ret
}

func Test_1078(t *testing.T) {
	text := "alice is a good girl she is a good student"
	first := "a"
	second := "good"
	res := findOcurrences(text, first, second)
	res = findOcurrences_1(text, first, second)
	fmt.Println(res)
}
