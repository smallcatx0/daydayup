package leetcode

import (
	"bytes"
	"fmt"
	"strconv"
	"testing"
)

type ListNode struct {
	Val  int
	Next *ListNode
}

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func (t *TreeNode) ArrBuild(arr []int) {
	t = arr2Tree(arr)
}

func arr2Tree(arr []int) *TreeNode {
	if len(arr) == 0 {
		return nil
	}
	root := &TreeNode{Val: arr[0]}
	nodes := []*TreeNode{root}
	for i, v := range arr[1:] {
		node := &TreeNode{Val: v}
		nodes = append(nodes, node)
		if i%2 == 1 {
			nodes[(i-1)/2].Left = node
		}
		if i%2 == 0 {
			nodes[(i-2)/2].Right = node
		}
	}
	return root
}

func (t *TreeNode) String() string {
	// 层序遍历
	type anode struct {
		node *TreeNode
		h    int
	}
	q := []anode{{t, 0}}
	ret := bytes.Buffer{}
	line := 0
	for len(q) != 0 {
		node, c := q[0].node, q[0].h // 队首
		q = q[1:]                    // 出队
		ret.WriteString(strconv.Itoa(node.Val))
		if line != c {
			ret.WriteString("\n")
			line = c
		} else {
			ret.WriteString(", ")
		}
		if node.Left != nil {
			q = append(q, anode{node.Left, c + 1})
		} else if node.Right != nil {
			q = append(q, anode{node.Right, c + 1})
		}
	}
	return ret.String()
}

func TestArr2Tree(t *testing.T) {
	t1 := &TreeNode{}
	t1.ArrBuild([]int{3, 5, 1, 6, 2, 9, 8, -1, -1, 7, 4})
	fmt.Println(t1)
}
