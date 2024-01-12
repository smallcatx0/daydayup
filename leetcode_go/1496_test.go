package leetcode

import (
	"fmt"
	"strconv"
	"testing"
)

// 暴力: 将所有走过的的坐标存入map,
var op = map[rune][2]int{'N': {0, 1}, 'S': {0, -1}, 'E': {1, 0}, 'W': {-1, 0}}

func isPathCrossing(path string) bool {
	m := map[string]struct{}{"0,0": {}}
	x, y := 0, 0
	for _, v := range path {
		x += op[v][0]
		y += op[v][1]
		point := strconv.Itoa(x) + "," + strconv.Itoa(y)
		fmt.Println(m)
		if _, ok := m[point]; ok {
			return true
		}
		m[point] = struct{}{}
	}
	return false
}

func Test_1496(t *testing.T) {
	path := "NESWW"
	ret := isPathCrossing(path)
	fmt.Println(ret)
}
