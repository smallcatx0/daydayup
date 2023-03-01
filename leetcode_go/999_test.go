package leetcode

import (
	"fmt"
	"testing"
)

func numRookCaptures(board [][]byte) int {
	L := 8
	count := 0
	for x := 0; x < L; x++ {
		for y := 0; y < L; y++ {
			// 找到R 上下左右 找 p
			if board[x][y] == 'R' {
				// 上
				for i := x; i >= 0; i-- {
					if board[i][y] == 'B' {
						break
					}
					if board[i][y] == 'p' {
						count++
						break
					}
				}
				// 下
				for i := x; i < L; i++ {
					if board[i][y] == 'B' {
						break
					}
					if board[i][y] == 'p' {
						count++
						break
					}
				}
				// 左
				for i := y; i >= 0; i-- {
					if board[x][i] == 'B' {
						break
					}
					if board[x][i] == 'p' {
						count++
						break
					}
				}
				// 右
				for i := y; i < L; i++ {
					if board[x][i] == 'B' {
						break
					}
					if board[x][i] == 'p' {
						count++
						break
					}
				}
			}
		}
	}
	return count
}

func Test_999(t *testing.T) {
	b := [][]byte{
		{'.', '.', '.', '.', '.', '.', '.', '.'},
		{'.', '.', '.', 'p', '.', '.', '.', '.'},
		{'.', '.', '.', 'R', '.', '.', '.', 'p'},
		{'.', '.', '.', '.', '.', '.', '.', '.'},
		{'.', '.', '.', '.', '.', '.', '.', '.'},
		{'.', '.', '.', 'p', '.', '.', '.', '.'},
		{'.', '.', '.', '.', '.', '.', '.', '.'},
		{'.', '.', '.', '.', '.', '.', '.', '.'},
	}
	res := numRookCaptures(b)
	fmt.Println(res)
}
