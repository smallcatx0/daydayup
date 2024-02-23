package leetcode

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
//  遍历
func countNodes(root *TreeNode) int {
	if root == nil {
		return 0
	}
	return countNodes(root.Left) + countNodes(root.Right) + 1
}

/**
思路：
	- 根据层数确定完全二叉树的节点范围:[]
	- 二分查找法 确定缺口在哪里
*/
func countNodes_1(root *TreeNode) int {
	// TODO: 二分查找确定完全二叉树底层缺口位置
	return 0
}
