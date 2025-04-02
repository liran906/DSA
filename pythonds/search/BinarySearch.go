package search

func BinarySearch_recursive(target int, alist []int) bool {
	if len(alist) == 0 {
		return false
	}
	mid := len(alist) / 2
	if alist[mid] == target {
		return true
	} else if alist[mid] > target {
		return BinarySearch_recursive(target, alist[:mid])
	} else {
		return BinarySearch_recursive(target, alist[mid+1:])
	}
}

func BinarySearch_pointer(target int, alist []int) bool {
	l, r := 0, len(alist)-1
	if alist[l] > target || alist[r] < target {
		return false
	}
	for m := (l + r) / 2; l <= r; m = (l + r) / 2 {
		if alist[m] == target {
			return true
		} else if alist[m] > target {
			r = m - 1
		} else {
			l = m + 1
		}
	}
	return false
}
