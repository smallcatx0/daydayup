package leetcode

import (
	"fmt"
	"testing"
)

/**
1971-01-01  % 7

*/
var week = []string{"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}
var monthDays = []int{31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30}

func dayOfTheWeek(day int, month int, year int) string {
	days := 0
	// 输入年份之前的年份的天数贡献
	days += 365*(year-1971) + (year-1969)/4
	// 输入年份中，输入月份之前的月份的天数贡献
	for _, d := range monthDays[:month-1] {
		days += d
	}
	if month >= 3 && (year%400 == 0 || year%4 == 0 && year%100 != 0) {
		days++
	}
	days += day
	return week[(days+3)%7]
}

func Test_1185(t *testing.T) {
	day, month, year := 31, 8, 2019
	res := dayOfTheWeek(day, month, year)
	fmt.Println(res)
}
