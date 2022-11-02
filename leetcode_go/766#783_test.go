package leetcode

import (
	"fmt"
	"testing"
)

// #766. 托普利茨矩阵
/**
{1, 2, 3, 4},
{5, 1, 2, 3},
{9, 5, 1, 2},

(x+1, y+1) = (0, 0) (1, 1) (2, 2) (3, 3)
(x+1, y+1) = (0, 1) (1, 2) (2, 3)
(x+1, y+1) = (0, 2) (1, 3)
(x+1, y+1) = (0, 3)
--
(x+1, y+1) = (1, 0) (2, 1)
(x+1, y+1) = (2, 0)
*/
func isToeplitzMatrix(matrix [][]int) bool {
	if len(matrix) == 0 {
		return true
	}
	l, r := len(matrix), len(matrix[0])
	lz := func(m [][]int, l, r, x, y int) bool {
		n := m[x][y]
		for x < l && y < r {
			if n != m[x][y] {
				return false
			}
			x += 1
			y += 1
		}
		return true
	}
	// 从左往右扫描
	for i := 0; i < r; i++ {
		if !lz(matrix, l, r, 0, i) {
			return false
		}
	}
	// 从上往下扫描
	for i := 1; i < l; i++ {
		if !lz(matrix, l, r, i, 0) {
			return false
		}
	}
	return true
}

func Test_766(t *testing.T) {
	matrix := [][]int{
		{1, 2, 3, 4},
		{5, 1, 2, 3},
		{9, 5, 1, 2},
	}
	matrix = [][]int{
		{1, 2},
		{5, 2},
	}
	ret := isToeplitzMatrix(matrix)
	fmt.Println(ret)
}

// #783. 二叉搜索树节点最小距离

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func pre(root *TreeNode) []int {
	if root == nil {
		return []int{}
	}
	l := pre(root.Left)
	l = append(l, []int{root.Val}...)
	l = append(l, pre(root.Right)...)
	return l
}

// 二叉搜索树中序遍历 升序
func minDiffInBST(root *TreeNode) int {
	l := pre(root)
	min := -1
	for i := 1; i < len(l); i++ {
		d := l[i] - l[i-1]
		if min == -1 {
			min = d
		} else if min > d {
			min = d
		}
	}
	return min
}

func Test_783(t *testing.T) {
	root := &TreeNode{Val: 4}
	root.Left = &TreeNode{Val: 2}
	root.Right = &TreeNode{Val: 6}
	root.Left.Left = &TreeNode{Val: 1}
	root.Left.Right = &TreeNode{Val: 3}

	ret := minDiffInBST(root)
	fmt.Println("ret=", ret)
}
