package leetcode

import (
	"fmt"
	"strings"
	"testing"
)

func numUniqueEmails(emails []string) int {
	s := map[string]bool{}
	for _, e := range emails {
		k := emailParse(e)
		s[k] = true
	}
	return len(s)
}

// 解析Email地址
func emailParse(email string) string {
	info := strings.SplitN(email, "@", 2)
	local := []rune{}
	for _, v := range info[0] {
		if v == '+' {
			break
		}
		if v == '.' {
			continue
		}
		local = append(local, v)
	}
	return string(local) + "@" + info[1]
}

func Test_929(t *testing.T) {
	emails := []string{"test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"}
	res := numUniqueEmails(emails)
	fmt.Println(res)

	em := emailParse("alic+e.z@leetcode.com")
	fmt.Println(em)

}
