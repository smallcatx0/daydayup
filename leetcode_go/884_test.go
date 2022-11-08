package leetcode

import (
	"fmt"
	"strings"
	"testing"
)

/**
句子 是一串由空格分隔的单词。每个 单词 仅由小写字母组成。
如果某个单词在其中一个句子中恰好出现一次，在另一个句子中却 没有出现 ，那么这个单词就是 不常见的 。
给你两个 句子 s1 和 s2 ，返回所有 不常用单词 的列表。返回列表中单词可以按 任意顺序 组织。
*/
func uncommonFromSentences(s1 string, s2 string) []string {
	hs := map[string]int{}
	for _, word := range strings.Split(s1+" "+s2, " ") {
		hs[word] += 1
	}
	// fmt.Println(hs)
	ret := []string{}
	for word, count := range hs {
		if count == 1 {
			ret = append(ret, word)
		}
	}
	return ret
}

func Test_884(t *testing.T) {
	s1 := "this apple is sweet"
	s2 := "this apple is sour"
	ret := uncommonFromSentences(s1, s2)
	fmt.Println(ret)
}
