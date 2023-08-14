package leetcode

import "testing"

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func getDecimalValue(head *ListNode) int {
	s := 0
	for head != nil {
		s = s*2 + head.Val
		head = head.Next
	}
	return s
}

func Test_1290(t *testing.T) {

}
