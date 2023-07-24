package leetcode

import (
	"fmt"
	"sort"
	"testing"
)

/**
给定四个整数 rows ,   cols ,  rCenter 和 cCenter 。有一个 rows x cols 的矩阵，你在单元格上的坐标是 (rCenter, cCenter) 。

返回矩阵中的所有单元格的坐标，并按与 (rCenter, cCenter) 的 距离 从最小到最大的顺序排。你可以按 任何 满足此条件的顺序返回答案。

单元格(r1, c1) 和 (r2, c2) 之间的距
*/

func allCellsDistOrder(rows int, cols int, rCenter int, cCenter int) [][]int {
	bk := map[int][][]int{}
	for x := 0; x < rows; x++ {
		for y := 0; y < cols; y++ {
			// 计算距离
			d := abs(rCenter-x) + abs(cCenter-y)
			bk[d] = append(bk[d], []int{x, y})
		}
	}
	dls := []int{}
	for d := range bk {
		dls = append(dls, d)
	}
	// key排序
	sort.Ints(dls)
	ret := [][]int{}
	for _, v := range dls {
		ret = append(ret, bk[v]...)
	}
	return ret
}

func abs(num int) int {
	if num < 0 {
		return -num
	}
	return num
}

func Test_1030(t *testing.T) {
	rows, cols := 1, 2
	rCenter, cCenter := 0, 0
	ret := allCellsDistOrder(rows, cols, rCenter, cCenter)
	fmt.Println(ret)
}
