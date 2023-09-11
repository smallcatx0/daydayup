package leetcode

import (
	"fmt"
	"testing"
	"time"
)

// 把1971到date1的天数与1971到date2的天数作差取绝对值。
func daysBetweenDates(date1 string, date2 string) int {
	t1, _ := time.Parse("2006-01-02", date1)
	t2, _ := time.Parse("2006-01-02", date2)
	sec := int(t1.Unix()) - int(t2.Unix())
	if sec < 0 {
		sec = -sec
	}
	return sec / (3600 * 24)
}

func Test_1360(t *testing.T) {
	date1 := "2019-06-29"
	date2 := "2019-06-30"
	res := daysBetweenDates(date1, date2)
	fmt.Println(res)
}
