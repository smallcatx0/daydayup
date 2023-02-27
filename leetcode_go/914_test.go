package leetcode

import (
	"fmt"
	"testing"
)

/**
频次统计

从 2 ~ min 找公约数
*/

func hasGroupsSizeX(deck []int) bool {
	fer := map[int]int{}
	for _, v := range deck {
		fer[v] += 1
	}
	min := int(10e5)
	for _, k := range fer {
		if min > k {
			min = k
		}
	}
	// 找频次的公约数 2~min
	for i := 2; i <= min; i++ {
		ok := true
		for _, k := range fer {
			if k%i != 0 {
				ok = false
				break
			}
		}
		if ok == true {
			return true
		}
	}
	return false
}

var Prime = []int{2, 3, 5, 7, 11, 13, 17, 19, 31, 37, 41, 43, 47, 53, 59, 61, 73, 79, 83, 89, 97, 101, 103, 107, 127}

func hasGroupsSizeX_1(deck []int) bool {
	fer := map[int]int{}
	for _, v := range deck {
		fer[v] += 1
	}
	min := int(10e5)
	for _, k := range fer {
		if min > k {
			min = k
		}
	}
	// 找频次的公约数 2~min
	for i := 0; Prime[i] <= min; i++ {
		ok := true
		for _, k := range fer {
			if k%Prime[i] != 0 {
				ok = false
				break
			}
		}
		if ok == true {
			return true
		}
	}
	return false
}

// 1,1,1,1,2,2,2,2,2,2
func Test_914(t *testing.T) {
	deck := []int{1, 1, 2, 2, 3, 3, 4, 4}
	res := hasGroupsSizeX(deck)
	fmt.Println(res)
}
