package leetcode

import (
	"fmt"
	"testing"
)

func mostVisited(n int, rounds []int) []int {
	res := []int{}
	st := rounds[0]
	ed := rounds[len(rounds)-1]
	if st <= ed {
		for ; st <= ed; st++ {
			res = append(res, st)
		}
	} else {
		for i := 1; i <= ed; i++ {
			res = append(res, i)
		}
		for i := st; i <= n; i++ {
			res = append(res, i)
		}
	}
	return res
}

func Test_1560(t *testing.T) {
	r := []int{3, 1, 2}
	n := 4
	res := mostVisited(n, r)
	fmt.Println(res)

}
