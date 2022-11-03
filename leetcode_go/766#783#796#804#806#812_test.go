package leetcode

import (
	"bytes"
	"fmt"
	"strings"
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

// #796. 旋转字符串
func rotateString(s string, goal string) bool {
	l := len(s)
	for i := 0; i < l; i++ {
		if goal[0] == s[i] {
			s2 := s[i:] + s[:i]
			fmt.Println(string(s2))
			if s2 == goal {
				return true
			}
		}
	}
	return false
}

func Test_796(t *testing.T) {
	s := "bbbacddceeb"
	goal := "ceebbbbacdd"
	ret := rotateString(s, goal)
	fmt.Println(ret)
}

// #804. 唯一摩尔斯密码词
var mores = []string{".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."}

func uniqueMorseRepresentations(words []string) int {
	s := map[string]bool{}
	for _, word := range words {
		if m := word2mores(word); !s[m] {
			s[m] = true
		}
	}
	return len(s)
}

func word2mores(word string) string {
	var m bytes.Buffer
	for i := 0; i < len(word); i++ {
		// fmt.Println(word[i] - 'a')
		m.WriteString(mores[word[i]-'a'])
	}
	return m.String()
}

func Test_804(t *testing.T) {
	words := []string{"gin", "zen", "gig", "msg"}
	ret := uniqueMorseRepresentations(words)
	// ret := word2mores("gin")
	fmt.Println(ret)
}

// #806. 写字符串需要的行数
func numberOfLines(widths []int, s string) []int {
	max := 100
	l := 1
	for _, c := range s {
		w := widths[c-'a']
		if max-w < 0 {
			// 行数加一
			l += 1
			max = 100 - w
		} else {
			max -= w
		}
	}
	return []int{l, 100 - max}
}

func Test_806(t *testing.T) {
	wd := []int{10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10}
	// s := "abcdefghijklmnopqrstuvwxyz"
	s := "a"
	ret := numberOfLines(wd, s)
	fmt.Println(ret)
}

// #812. 最大三角形面积
func largestTriangleArea(points [][]int) float64 {
	// 最高点, 最低点,
	if len(points) == 3 {
		return float64(area2(points[0], points[1], points[2])) / 2
	}
	var maxs = 0
	for i, p1 := range points {
		// fmt.Println(p1, points[:i])
		for j, p2 := range points[:i] {
			for _, p3 := range points[:j] {
				if s := area2(p1, p2, p3); s > int(maxs) {
					maxs = s
				}
			}
		}
	}
	return float64(maxs) / 2
}

func area2(p1, p2, p3 []int) int {
	s := p1[0]*p2[1] + p2[0]*p3[1] + p3[0]*p1[1] - p1[0]*p3[1] - p2[0]*p1[1] - p3[0]*p2[1]
	if s < 0 {
		s = -s
	}
	return s
}

func Test_812(t *testing.T) {
	points := [][]int{
		{9, 7}, {6, 10}, {1, 10}, {2, 7},
	}
	ret := largestTriangleArea(points)
	fmt.Println(ret)
}

// #819. 最常见的单词
func mostCommonWord(paragraph string, banned []string) string {
	m := map[string]int{}
	ban := map[string]bool{}
	for _, word := range banned {
		ban[word] = true
	}
	l := -1
	pre, now := false, false
	max := 0
	ret := ""
	for i, c := range paragraph + " " {
		now = isLetter(c)
		if pre == false && now == true {
			// 上跳变: 记录起点
			l = i
		}
		if pre == true && now == false {
			// 下跳变: 记录单词
			word := strings.ToLower(paragraph[l:i])
			if !ban[word] {
				m[word] += 1
				if m[word] > max {
					max = m[word]
					ret = word
				}
			}
		}
		pre = now
	}
	return ret
}

func isLetter(c rune) bool {
	return (c >= 'A' && c <= 'Z') || (c >= 'a' && c <= 'z')
}

func Test_819(t *testing.T) {
	p := "Bob hit a ball, the hit BALL flew far after it was hit."
	ban := []string{"hit"}
	ret := mostCommonWord(p, ban)
	fmt.Println(ret)
}
