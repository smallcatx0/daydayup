package leetcode

import (
	"fmt"
	"testing"
)

// 时间复杂度 O(n^2) 空间复杂度O(1)
func fairCandySwap(aliceSizes []int, bobSizes []int) []int {
	// 先暴力算 sum(aliceSizes...) - aliceSizes[i] + bobSizes[j] == sum(bobSizes...) - bobSizes[j] + aliceSizes[i]
	// sumA - a[i] + x = sumB - x + a[i]
	// 2x = sumB-sumA - 2a[i]
	sum := func(arr []int) (sum int) {
		for _, v := range arr {
			sum += v
		}
		return
	}
	sumA := sum(aliceSizes)
	sumB := sum(bobSizes)
	for i := 0; i < len(aliceSizes); i++ {
		for j := 0; j < len(bobSizes); j++ {
			if sumA-aliceSizes[i]+bobSizes[j] == sumB-bobSizes[j]+aliceSizes[i] {
				return []int{aliceSizes[i], bobSizes[j]}
			}
		}
	}
	return nil
}

//
func fairCandySwap1(aliceSizes []int, bobSizes []int) []int {
	var sumA, sumB int
	amap := map[int]bool{}
	for i := 0; i < len(aliceSizes); i++ {
		amap[aliceSizes[i]] = true
		sumA += aliceSizes[i]
	}
	for i := 0; i < len(bobSizes); i++ {
		sumB += bobSizes[i]
	}
	for i := 0; i < len(bobSizes); i++ {
		// 先暴力算 sum(aliceSizes...) - aliceSizes[i] + bobSizes[j] == sum(bobSizes...) - bobSizes[j] + aliceSizes[i]
		// sumA - a[i] + b[j] = sumB - b[j] + a[i]
		// sumA - sunB + 2b[j] = 2a[i]
		// a[i] = (sumA - sumB)2 + 2b[j]
		x := (sumA-sumB)/2 + bobSizes[i]
		fmt.Println(x)
		if amap[x] {
			fmt.Println()
			return []int{x, bobSizes[i]}
		}
	}
	return nil
}

func Test_888(t *testing.T) {
	a := []int{1, 1}
	b := []int{2, 2}
	ret := fairCandySwap1(a, b)
	fmt.Println(ret)
}
