package leetcode

import (
	"fmt"
	"strings"
	"testing"
)

var month = map[string]string{"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06", "Jul": "07", "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}

func reformatDate(date string) string {
	d := strings.Split(date, " ")
	if len(d[0]) == 3 {
		d[0] = "0" + d[0]
	}
	return d[2] + "-" + month[d[1]] + "-" + d[0][0:2]
}

func Test_1507(t *testing.T) {
	res := reformatDate("20th Oct 2052")
	fmt.Println(res)
}
