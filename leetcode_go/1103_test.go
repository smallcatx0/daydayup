package leetcode

import (
	"fmt"
	"math"
	"testing"
)

/**
n=3 第k轮 消耗 ()糖果
1,2,3
4,5,6   => (1 + n*k)* n*k / 2
7,      => s(m) = (1 + m)*m/2 ; m = n*k+i

*/

func distributeCandies(candies int, n int) []int {
	// 礼物份数
	p := int(math.Sqrt(float64(2*candies)+0.25) - 0.5)
	// 最后一份礼物糖果
	rem := candies - (p+1)*p/2
	// 行列数
	rows, cols := p/n, p%n
	d := make([]int, n)
	for i := 0; i < n; i++ {
		d[i] = (i+1)*rows + rows*(rows-1)/2*n
		if i < cols {
			d[i] += i + 1 + rows*n
		}
	}
	d[cols] += rem
	return d
}

func Test_1103(t *testing.T) {
	c, n := 31, 3

	res := distributeCandies(c, n)
	fmt.Println(res)
}
