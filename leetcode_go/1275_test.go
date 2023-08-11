package leetcode

import (
	"fmt"
	"testing"
)

// 只关注最后一位即可
func tictactoe(moves [][]int) string {
	step := len(moves)
	if step <= 4 {
		return "Pending"
	}
	point := [][]int{}
	for i := step - 1; i >= 0; i -= 2 {
		point = append(point, moves[i])
	}

	// if step%2 == 1 {

	// } else {

	// }
	// if inLine(moves[0], moves[2], moves[4]) {
	// 	return "A"
	// }
	return ""
}

func inLine(x1, x2, x3 []int) bool {
	return (x1[0]-x2[0])*(x3[1]-x1[1]) == (x3[0]-x1[0])*(x2[1]-x1[1])
}

func Test_1275(t *testing.T) {
	moves := [][]int{{0, 0}, {2, 0}, {1, 1}, {2, 1}, {2, 2}}
	res := tictactoe(moves)
	fmt.Println(res)

}
