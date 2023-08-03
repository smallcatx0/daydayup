package leetcode

import (
	"fmt"
	"strconv"
	"testing"
)

func dayOfYear(date string) int {
	year, _ := strconv.Atoi(date[:4])
	month, _ := strconv.Atoi(date[5:7])
	day, _ := strconv.Atoi(date[8:])
	days := []int{31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31}
	if year%400 == 0 || (year%4 == 0 && year%10 != 100) {
		days[1]++
	}
	for _, d := range days[:month-1] {
		day += d
	}
	return day
}

func Test_1154(t *testing.T) {
	date := "2019-04-09"
	res := dayOfYear(date)
	fmt.Println(res)
}
