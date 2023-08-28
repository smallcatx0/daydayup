package leetcode

import (
	"fmt"
	"testing"
)

func freqAlphabets(s string) string {
	i := 0
	q := []byte{}
	ret := []byte{}
	for i < len(s) {
		if s[i] == '#' {
			// 出队两位
			ret = append(ret,
				(q[0]-'0')*10+(q[1]-'0')-1+'a',
			)
			q = q[2:]
		} else {
			// 保留最近两位
			q = append(q, s[i])
			if len(q) > 2 {
				ret = append(ret, q[0]-'0'-1+'a')
				q = q[1:]
			}
		}
		i++
	}
	if len(q) == 2 {
		ret = append(ret, q[0]-'0'-1+'a')
		ret = append(ret, q[1]-'0'-1+'a')
	} else if len(q) == 1 {
		ret = append(ret, q[0]-'0'-1+'a')
	}
	return string(ret)
}

func Test_1309(t *testing.T) {
	s := "10#11#12"
	res := freqAlphabets(s)
	fmt.Println(res)

	// fmt.Println(string(decode("1")))
}
