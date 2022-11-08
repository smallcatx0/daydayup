package leetcode

func middleNode(head *ListNode) *ListNode {
	// 快慢指针
	curr, mid := head, head
	for curr.Next != nil {
		curr = curr.Next
		if curr.Next != nil {
			curr = curr.Next
		}
		mid = mid.Next
	}
	return mid
}
