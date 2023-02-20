package leetcode

import (
	"fmt"
	"testing"
)

var preNode *TreeNode
var r *TreeNode

func increasingBST(root *TreeNode) *TreeNode {
	// 中序遍历
	ldr(root)
	return r
}

func ldr(root *TreeNode) {
	if root == nil {
		return
	}
	ldr(root.Left)
	// 中序的逻辑

	root.Left = nil      // 当前节点的左分支 砍掉
	preNode.Right = root // 生成单边树
	preNode = root       // 当前节点记录为前驱节点

	ldr(root.Right)
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
