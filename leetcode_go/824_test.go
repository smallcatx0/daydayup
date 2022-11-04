package leetcode

import (
	"bytes"
	"fmt"
	"testing"
)

var yuan = map[byte]bool{'a': true, 'e': true, 'i': true, 'o': true, 'u': true, 'A': true, 'E': true, 'I': true, 'O': true, 'U': true}

func toGoatLatin(sentence string) string {
	ret := bytes.Buffer{}
	wordIndex := 1
	st := 0
	for i, v := range sentence + " " {
		if v != ' ' {
			continue
		}
		if wordIndex != 1 {
			ret.WriteByte(' ')
		}
		if yuan[sentence[st]] {
			ret.WriteString(sentence[st:i])
			ret.WriteString("ma")
		} else {
			ret.WriteString(sentence[st+1 : i])
			ret.WriteByte(sentence[st])
			ret.WriteString("ma")
		}
		for j := 0; j < wordIndex; j++ {
			ret.WriteByte('a')
		}
		wordIndex += 1
		st = i + 1
	}
	return ret.String()
}

func Test_828(t *testing.T) {
	s := "Each word consists of lowercase and uppercase letters only"
	ret := toGoatLatin(s)
	fmt.Println(ret)
}
