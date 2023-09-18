package leetcode

import (
	"bytes"
	"fmt"
	"testing"
)

var (
	romaInt = [13]int{1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1}
	romaStr = [13]string{"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"}
)

func intToRoman(num int) string {
	res := bytes.NewBuffer(nil)
	i := 0
	for num > 0 {
		for ; i < 13; i++ {
			if num >= romaInt[i] {
				num -= romaInt[i]
				res.WriteString(romaStr[i])
				i--
			}
		}
	}
	return res.String()
}

// o(1) o(1)
var (
	个 = [10]string{"", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"}
	十 = [10]string{"", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"}
	百 = [10]string{"", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "LCCC", "CM"}
	千 = [10]string{"", "M", "MM", "MMM"}
)

func intToRoman_2(num int) string {
	return 千[num/1000] + 百[num%1000/100] + 十[num%100/10] + 个[num%10]
}

func Test_12(t *testing.T) {
	n := 93
	res := intToRoman_2(n)
	fmt.Println(res)
}
