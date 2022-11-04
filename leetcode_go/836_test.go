package leetcode

import (
	"fmt"
	"testing"
)

// 0    ,1    ,2    ,3
// x_min,y_min,x_max,y_max
// 四个顶点 (x_min,y_min) (x_min,y_max) (x_max,y_max) (x_max,y_min)
//         (0,1) (0,3) (2,3) (2,1)
const (
	Xmin = 0
	Ymin = 1
	Xmax = 2
	Ymax = 3
)

func isRectangleOverlap(rec1 []int, rec2 []int) bool {
	// 2在1左边 2xmax <= 1xmax
	if rec2[Xmax] <= rec1[Xmin] {
		return false
	}
	// 2在1上边 2ymin >= 1ymax
	if rec2[Ymin] >= rec1[Ymax] {
		return false
	}
	// 2在1右边 2xmin >= 1xmax
	if rec2[Xmin] >= rec1[Xmax] {
		return false
	}
	// 2在1下边
	if rec2[Ymax] <= rec1[Ymin] {
		return false
	}
	return true
}

func Test_836(t *testing.T) {
	rec1 := []int{-7, -3, 10, 5}
	rec2 := []int{-6, -5, 5, 10}
	// 	[-7,-3,10,5]
	// [-6,-5,5,10]
	ret := isRectangleOverlap(rec1, rec2)
	fmt.Println(ret)
}
