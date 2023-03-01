package leetcode

func isCousins(root *TreeNode, x int, y int) bool {
	// 层序遍历
	type n struct {
		N    *TreeNode
		H    int
		Pval int
	}
	q := make([]n, 0, 5)
	q = append(q, n{root, 0, -1})
	match := make([]n, 0, 2)
	canVal := map[int]bool{x: true, y: true}
	currH := 0
	for len(q) != 0 {
		// 出队
		node := q[0]
		q = q[1:]
		if currH != node.H {
			currH = node.H
			// 换层时,匹配到一个 直接失败
			if len(match) == 1 {
				return false
			}
		}
		if canVal[node.N.Val] {
			canVal[node.N.Val] = false
			match = append(match, node)
			// 匹配到两个,开始比较父节点
			if len(match) == 2 && match[0].Pval != match[1].Pval {
				return true
			}
		}
		if node.N.Left != nil {
			q = append(q, n{node.N.Left, node.H + 1, node.N.Val})
		}
		if node.N.Right != nil {
			q = append(q, n{node.N.Right, node.H + 1, node.N.Val})
		}
	}
	return false
}
