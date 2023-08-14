package leetcode

import (
	"fmt"
	"testing"
)

// 列举组合数
var (
	Cx3 = map[int][][]int{
		3: {{0, 1, 2}},
		4: {{0, 1, 2}, {0, 1, 3}, {0, 2, 3}, {1, 2, 3}},
		5: {
			{0, 1, 2}, {0, 1, 3}, {0, 2, 3}, {1, 2, 3},
			{0, 1, 4}, {0, 2, 4}, {1, 2, 4},
			{0, 3, 4}, {1, 3, 4},
			{2, 3, 4},
		},
	}
	LastOpt = map[int]string{
		1: "A", 0: "B",
	}
)

func tictactoe(moves [][]int) string {
	step := len(moves)
	if step <= 4 {
		return "Pending"
	}
	point := [][]int{}
	// 只关注最后一位即可
	for i := step - 1; i >= 0; i -= 2 {
		point = append(point, moves[i])
	}
	for _, v := range Cx3[len(point)] {
		// 后手赢了
		// fmt.Println(point[v[0]], point[v[1]], point[v[2]])
		if inLine(point[v[0]], point[v[1]], point[v[2]]) {
			return LastOpt[step%2]
		}
	}
	if len(moves) != 9 {
		return "Pending"
	}
	return "Draw"
}

func inLine(a, b, c []int) bool {
	return (b[1]-a[1])*(c[0]-a[0]) == (c[1]-a[1])*(b[0]-a[0])
}

/**
所有赢的情况
111  000  000  100  010  001  100  001
000  111  000  100  010  001  010  010
000  000  111  100  010  001  001  100
*/

var Xwins = []int{
	0b111000000, 0b000111000, 0b000000111, 0b100100100, 0b010010010, 0b001001001, 0b100010001, 0b001010100,
}

func tictactoe_2(moves [][]int) string {
	step := len(moves)
	if step <= 4 {
		return "Pending"
	}
	// 将后手转换为二进制
	a, b := 0, 0
	for i := step - 1; i >= 0; i -= 2 {
		a += 1<<moves[i][0]*3 + moves[i][1]
		if i >= 1 {
			b += 1<<moves[i-1][0]*3 + moves[i-1][1]
		}
	}
	fmt.Printf("a: %b b: %b\n", a, b)
	for _, c := range Xwins {
		if a&c == c {
			return "B"
		}
		if b&c == c {
			return "A"
		}
	}
	if len(moves) == 9 {
		return "Draw"
	}
	return "Pending"
}

func Test_1275(t *testing.T) {
	moves := [][]int{{0, 0}, {1, 1}, {2, 0}, {1, 0}, {1, 2}, {2, 1}, {0, 1}, {0, 2}, {2, 2}}
	// moves := [][]int{{0, 0}, {2, 0}, {1, 1}, {2, 1}, {2, 2}}
	// moves := [][]int{{0, 0}, {1, 1}, {0, 1}, {0, 2}, {1, 0}, {2, 0}}
	res := tictactoe(moves)
	// res := tictactoe_2(moves)
	fmt.Println(res)

}
