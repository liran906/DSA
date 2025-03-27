// https://leetcode.cn/problems/happy-number
// e

package main

func isHappy1(n int) bool {
	seen := map[int]struct{}{}
	for n != 1 {
		sum := 0
		for n > 0 {
			sum += (n % 10) * (n % 10)
			n = n / 10
		}
		if _, exists := seen[sum]; exists {
			return false
		}
		seen[sum] = struct{}{}
		n = sum
	}
	return true
}

func isHappy2(n int) bool {
	fast, slow := n, n
	for fast != 1 {
		fast = getNext(getNext(fast))
		slow = getNext(slow)
		if fast == slow && fast != 1 {
			return false
		}
	}
	return fast == 1
}

func getNext(n int) (sum int) {
	for tmp := n; tmp > 0; {
		sum += (tmp % 10) * (tmp % 10)
		tmp /= 10
	}
	return
}
