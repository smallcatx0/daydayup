package leetcode

import (
	"fmt"
	"testing"
)

// 桶排序
func sortString(s string) string {
	cnt := ['z' + 1]int{}
	for _, c := range s {
		cnt[c]++
	}
	n := len(s)
	ret := make([]byte, 0, n)
	for len(ret) < n {
		for i := byte('a'); i <= 'z'; i++ {
			if cnt[i] > 0 {
				ret = append(ret, i)
			}
			cnt[i]--
		}
		for i := byte('z'); i >= 'a'; i-- {
			if cnt[i] > 0 {
				ret = append(ret, i)
				cnt[i]--
			}
		}
	}
	return string(ret)
}

func Test_1370(t *testing.T) {
	s := "aaaabbbbcccc"
	res := sortString(s)
	fmt.Println(res)
}
