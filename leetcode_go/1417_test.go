package leetcode

import (
	"fmt"
	"testing"
)

func reformat(s string) string {
	n, z := []byte{}, []byte{}
	l := len(s)
	ret := make([]byte, l)
	for i := 0; i < l; i++ {
		if charIsNum(s[i]) {
			n = append(n, s[i])
		} else {
			z = append(z, s[i])
		}
	}
	if len(z) > len(n) {
		if len(z)-len(n) >= 2 {
			return ""
		}
	} else {
		if len(n)-len(z) >= 2 {
			return ""
		}
		z, n = n, z
	}
	k := 0
	for i := 0; i < len(n); i++ {
		ret[k] = z[i]
		k++
		ret[k] = n[i]
		k++
	}
	if k != len(s) {
		ret[k] = z[len(z)-1]
	}
	return string(ret)
}

func charIsNum(c byte) bool {
	return '0' <= c && '9' >= c
}

// 双指针。原地算法
func reformat_2(s string) string {
	nc, zc := 0, 0
	ret := make([]byte, len(s))
	for i := range s {
		if charIsNum(s[i]) {
			nc++
		} else {
			zc++
		}
	}
	ni, zi := 0, 0
	if nc > zc {
		if nc-zc >= 2 {
			return ""
		}
		zi = 1
	} else {
		if zc-nc >= 2 {
			return ""
		}
		ni = 1
	}
	for i := 0; i < len(s); i++ {
		if charIsNum(s[i]) {
			ret[ni] = s[i]
			ni += 2
		} else {
			ret[zi] = s[i]
			zi += 2
		}
	}
	return string(ret)
}

func Test_1417(t *testing.T) {
	s := "1234abc"
	res := reformat_2(s)
	fmt.Println(res)
}
