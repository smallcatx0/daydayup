package leetcode

import (
	"fmt"
	"testing"
)

func isPrefixOfWord(sentence string, searchWord string) int {
	s := 1
	sl := len(searchWord)
	if len(sentence) >= sl && sentence[0:sl] == searchWord {
		return s
	}
	for i := 0; i < len(sentence)-sl; i++ {
		if sentence[i] == ' ' {
			s++
			i++
			if sentence[i:i+sl] == searchWord {
				return s
			}
		}
	}
	return -1
}

func Test_1455(t *testing.T) {
	sentence := "i love eating burger"
	searchWord := "burg"
	res := isPrefixOfWord(sentence, searchWord)
	fmt.Println(res)
}
