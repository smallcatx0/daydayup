package leetcode

import (
	"fmt"
	"testing"
)

var head *TreeNode

func increasingBST(root *TreeNode) *TreeNode {
	head = &TreeNode{}
	// 中序遍历
	ldr(root, head)
	return head.Right
}

func ldr(root *TreeNode, new *TreeNode) {
	if root == nil {
		return
	}
	ldr(root.Left, new)
	new.Right = &TreeNode{Val: root.Val}
	ldr(root.Right, new.Right)
}

func Test_897(t *testing.T) {
	root := TreeNode{Val: 5}
	root.Left = &TreeNode{Val: 3}
	root.Right = &TreeNode{Val: 6}
	// fmt.Println(root)
	ret := increasingBST(&root)
	for ret != nil {
		fmt.Print(ret.Val, " ")
		ret = ret.Right
	}
}
