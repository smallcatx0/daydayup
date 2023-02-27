package leetcode

import (
	"fmt"
	"testing"
)

type RecentCounter struct {
	q     [][2]int // 队列
	count int      // 数量
}

func Constructor() RecentCounter {
	return RecentCounter{
		q:     make([][2]int, 0),
		count: 0,
	}
}

func (this *RecentCounter) Ping(t int) int {
	// 入队 (计数+)
	top := len(this.q) - 1
	if top > 0 && this.q[top][0] == t {
		this.q[top][1] += 1
	} else {
		this.q = append(this.q, [2]int{t, 1})
	}
	this.count++
	// 计算淘汰(计数-)
	i := 0
	for ; t-this.q[i][0] > 3000; i++ {
		this.count -= this.q[i][1]
	}
	this.q = this.q[i:]
	// 返回计数
	return this.count
}

func Test_933(t *testing.T) {
	q := Constructor()
	fmt.Println(q.Ping(1))
	fmt.Println(q.Ping(100))
	fmt.Println(q.Ping(3001))
	fmt.Println(q.Ping(3002))

}
