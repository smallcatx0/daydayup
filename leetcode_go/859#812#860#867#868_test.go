package leetcode

import (
	"fmt"
	"testing"
)

/*
给你两个字符串 s 和 goal ，只要我们可以通过交换 s 中的两个字母得到与 goal 相等的结果，就返回 true ；否则返回 false 。
交换字母的定义是：取两个下标 i 和 j （下标从 0 开始）且满足 i != j ，接着交换 s[i] 和 s[j] 处的字符。
例如，在 "abcd" 中交换下标 0 和下标 2 的元素可以生成 "cbad" 。
*/
func buddyStrings(s string, goal string) bool {
	not := make([]int, 0, 2)
	same := 0
	mpp := [26]int{25: 0}
	db := len(s) >= 26
	for i := 0; i < len(s); i++ {
		if s[i] != goal[i] {
			not = append(not, i)
			same += 1
			if same > 2 {
				return false
			}
		}
		if !db {
			mpp[s[i]-'a'] += 1
			if mpp[s[i]-'a'] == 2 {
				db = true
			}
		}
	}
	if same == 0 {
		if db {
			return true
		} else {
			return false
		}
	}
	if same != 2 {
		return false
	}
	if s[not[0]] == goal[not[1]] && s[not[1]] == goal[not[0]] {
		return true
	} else {
		return false
	}
}

func Test_859(t *testing.T) {
	s := "abac"
	goal := "abad"
	ret := buddyStrings(s, goal)
	fmt.Println(ret)
	// fmt.Println([24]int{23: 0})
}

// #821. 字符的最短距离

func shortestToChar(s string, c byte) []int {
	l := len(s)
	ans := make([]int, l)
	p := []int{3 * l}
	for i := 0; i < l; i++ {
		if s[i] == c {
			p = append(p, i)
			ans[i] = 0
		}
	}
	p = append(p, 2*l)
	fmt.Println(ans)
	pi := 1
	for i := 0; i < l; i++ {
		if i > p[pi] {
			pi += 1
		}
		ans[i] = abs_min(p[pi-1]-i, p[pi]-i)
		// fmt.Println(p[pi-1], i, p[pi])
	}
	return ans
}
func abs_min(x, y int) int {
	if x < 0 {
		x = -x
	}
	if y < 0 {
		y = -y
	}
	if x > y {
		return y
	} else {
		return x
	}
}
func Test_821(t *testing.T) {
	// "aaba"
	// "b"
	s := "baaaa"
	c := byte('b')
	ret := shortestToChar(s, c)
	fmt.Println(ret)
}

func lemonadeChange(bills []int) bool {
	m5, m10 := 0, 0
	for _, one := range bills {
		switch one {
		case 5:
			m5 += 1
		case 10:
			m5 -= 1
			m10 += 1
		case 20:
			if m10 > 0 {
				m10 -= 1
				m5 -= 0
			} else {
				m5 -= 3
			}
		}
		if m5 < 0 {
			return false
		}
	}
	return true
}

func Test_860(t *testing.T) {
	bills := []int{5, 5, 5, 10, 5, 5, 10, 20, 20, 20}
	ret := lemonadeChange(bills)
	fmt.Println(ret)
}

func transpose(matrix [][]int) [][]int {
	if len(matrix) == 0 {
		return matrix
	}
	ret := [][]int{}
	row, col := len(matrix), len(matrix[0])
	for i := 0; i < col; i++ {
		tmp := []int{}
		for j := 0; j < row; j++ {
			tmp = append(tmp, matrix[j][i])
		}
		ret = append(ret, tmp)
	}
	return ret
}

func Test_867(t *testing.T) {
	matrix := [][]int{
		{1, 2},
		{4, 5},
		{7, 8},
	}
	ret := transpose(matrix)
	fmt.Println(ret)
}

func binaryGap(n int) int {
	maxl := 0
	st, i := -1, 0
	for n > 0 {
		b := n % 2
		// 找起点
		if st == -1 {
			if b == 1 {
				st = i
			}
		} else {
			// 找终点
			if b == 1 {
				if i-st > maxl {
					maxl = i - st
				}
				st = i
			}
		}
		n = n / 2
		i += 1
	}
	return maxl
}

func Test_868(t *testing.T) {
	n := 9
	ret := binaryGap(n)
	fmt.Println("ret", ret)
}
