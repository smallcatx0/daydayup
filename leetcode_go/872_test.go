package leetcode

import (
	"testing"
)

func leafSimilar(root1 *TreeNode, root2 *TreeNode) bool {
	var s1, s2 int64
	p(root1, &s1)
	p(root2, &s2)
	return s1 == s2
}

func p(root *TreeNode, sum *int64) {
	if root == nil {
		return
	}
	p(root.Left, sum)
	if root.Left == nil && root.Right == nil {
		// 校验和 每次 加一个比较大的数据
		*sum += 8981
		*sum ^= int64(root.Val)
	}
	p(root.Right, sum)
}

func Test_872(t *testing.T) {
}
