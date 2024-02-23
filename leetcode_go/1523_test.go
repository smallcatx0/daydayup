package leetcode

/**
奇~奇:
*/
func countOdds(low int, high int) int {
	ret := (high - low) / 2
	if low%2 == 1 || high%2 == 1 {
		ret += 1
	}
	return ret
}
