package leetcode

import (
	"fmt"
	"strings"
	"testing"
)

func stringMatching(words []string) []string {
	s := strings.Join(words, ",")
	res := []string{}
	for _, v := range words {
		first := strings.Index(s, v)
		last := strings.LastIndex(s, v)
		if first != -1 && last != 0 && first != last {
			res = append(res, v)
		}
	}
	return res
}

func Test_1408(t *testing.T) {
	words := []string{"mass", "as", "hero", "superhero"}
	res := stringMatching(words)
	fmt.Println(res)
}
