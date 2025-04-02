package sort

// import "fmt"

// func MergeSort(alist []int) []int {
// 	n := len(alist)
// 	if n <= 1 {
// 		return alist
// 	}

// 	left := MergeSort(alist[:n/2])
// 	right := MergeSort(alist[n/2:])

// 	for l, i, r := 0, 0, 0; l < len(left) && r < len(right); i++ {
// 		if left[l] > right[r] {
// 			alist[i] = right[r]
// 			r++
// 		} else {
// 			alist[i] = left[l]
// 			l++
// 		}
// 	}

// 	if len(left) > 0 {
// 		alist = append(alist, left...)
// 	} else if len(right) > 0 {
// 		alist = append(alist, right...)
// 	}
// 	return alist
// }

func MergeSort(alist []int) []int {
	n := len(alist)
	if n <= 1 {
		return alist
	}

	// 递归拆分
	left := MergeSort(alist[:n/2])
	right := MergeSort(alist[n/2:])

	// 合并
	return merge(left, right)
}

func merge(left, right []int) []int {
	merged := make([]int, 0, len(left)+len(right))

	l, r := 0, 0
	for l < len(left) && r < len(right) {
		if left[l] < right[r] {
			merged = append(merged, left[l])
			l++
		} else {
			merged = append(merged, right[r])
			r++
		}
	}

	// 添加剩余元素
	merged = append(merged, left[l:]...)
	merged = append(merged, right[r:]...)

	return merged
}
