package leetcode

import (
	"bytes"
	"fmt"
	"testing"
)

var yuan = map[byte]bool{'a': true, 'e': true, 'i': true, 'o': true, 'u': true, 'A': true, 'E': true, 'I': true, 'O': true, 'U': true}

func toGoatLatin(sentence string) string {
	ret := bytes.Buffer{}
	wordIndex := 1
	st := 0
	for i, v := range sentence + " " {
		if v != ' ' {
			continue
		}
		if wordIndex != 1 {
			ret.WriteByte(' ')
		}
		if yuan[sentence[st]] {
			ret.WriteString(sentence[st:i])
			ret.WriteString("ma")
		} else {
			ret.WriteString(sentence[st+1 : i])
			ret.WriteByte(sentence[st])
			ret.WriteString("ma")
		}
		for j := 0; j < wordIndex; j++ {
			ret.WriteByte('a')
		}
		wordIndex += 1
		st = i + 1
	}
	return ret.String()
}

func Test_828(t *testing.T) {
	s := "Each word consists of lowercase and uppercase letters only"
	ret := toGoatLatin(s)
	fmt.Println(ret)
}

func largeGroupPositions(s string) [][]int {
	l := len(s)
	ret := [][]int{}
	if l < 3 {
		return ret
	}
	st := 0
	for i := 1; i < l; i++ {
		if s[i] == s[st] {
			continue
		}
		// 记录长度
		if i-st >= 3 {
			ret = append(ret, []int{st, i - 1})
		}
		st = i
	}
	if l-st >= 3 {
		ret = append(ret, []int{st, l - 1})
	}
	return ret
}

func Test_830(t *testing.T) {
	s := "aaa"
	ret := largeGroupPositions(s)
	fmt.Println(ret)
}

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

// 0    ,1    ,2    ,3
// x_min,y_min,x_max,y_max
// 四个顶点 (x_min,y_min) (x_min,y_max) (x_max,y_max) (x_max,y_min)
//
//	(0,1) (0,3) (2,3) (2,1)
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

func backspaceCompare(s string, t string) bool {
	return string(Parse(s)) == string(Parse(t))
}

func Parse(s string) []byte {
	b := []byte(s)
	top := 0
	for i := 0; i < len(b); i++ {
		if b[i] == '#' {
			if top != 0 {
				top -= 1
			}
		} else {
			b[top] = b[i]
			top += 1
		}
	}
	// fmt.Println(string(b[:top]))
	return b[:top]
}
func Test_844(t *testing.T) {
	s := "y#fo##f"
	tar := "y#f#o##f"
	ret := backspaceCompare(s, tar)
	fmt.Println(ret)
}
