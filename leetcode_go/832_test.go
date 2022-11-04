package leetcode

import (
	"fmt"
	"testing"
)

func reverse(x int) int {
	if x == 0 {
		return 1
	} else {
		return 0
	}
}

func flipAndInvertImage(image [][]int) [][]int {
	for i := 0; i < len(image); i++ {
		l, r := 0, len(image[i])-1
		for l < r {
			image[i][l], image[i][r] = reverse(image[i][r]), reverse(image[i][l])
			l += 1
			r -= 1
		}
		if l == r {
			image[i][l] = reverse(image[i][l])
		}
	}
	return image
}

func Test_832(t *testing.T) {
	img := [][]int{
		{1, 1, 0},
		{1, 0, 1},
		{0, 0, 0},
	}
	ret := flipAndInvertImage(img)
	fmt.Println(ret)
}
