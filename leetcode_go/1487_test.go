package leetcode

import (
	"fmt"
	"strconv"
	"testing"
)

func getFolderNames(names []string) []string {
	m := make(map[string]int, len(names)/4)
	s := make(map[string]bool, len(names)/2)
	for i, a := range names {
		if m[a] > 0 {
			ns := a + "(" + strconv.Itoa(m[a]) + ")"
			for s[ns] {
				m[a]++
				ns = a + "(" + strconv.Itoa(m[a]) + ")"
			}
			names[i] = ns
		} else {
			names[i] = a
		}
		m[a]++
		if a != names[i] {
			m[names[i]]++
		}
		s[names[i]] = true
	}
	return names
}

func Test_1487(t *testing.T) {
	names := []string{"kaido", "kaido(2)", "kaido", "kaido", "kaido(1)"}
	res := getFolderNames(names)
	fmt.Println(res)
}
