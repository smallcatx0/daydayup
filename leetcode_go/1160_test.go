package leetcode

import (
	"fmt"
	"testing"
)

func countCharacters(words []string, chars string) int {
	m := [27]int{}
	for _, c := range chars {
		m[c-'a']++
	}
	ret := 0
	for _, w := range words {
		wc := [27]int{}
		ok := true
		for _, c := range w {
			k := c - 'a'
			wc[k]++
			if wc[k] > m[k] {
				ok = false
				break
			}
		}
		if ok {
			ret += len(w)
		}
	}
	return ret
}

func Test_1160(t *testing.T) {
	words := []string{"cat", "bt", "hat", "tree"}
	chars := "atach"

	res := countCharacters(words, chars)
	fmt.Println(res)
}
