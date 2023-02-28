package leetcode

func isUnivalTree(root *TreeNode) bool {
	if root == nil {
		return true
	}
	return f(root.Val, root)
}

func f(v int, node *TreeNode) bool {
	if node == nil {
		return true
	}
	if v != node.Val {
		return false
	}
	if !f(v, node.Left) {
		return false
	}
	return f(v, node)
}
