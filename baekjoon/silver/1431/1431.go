package main

import "fmt"

func main() {
	var n int
	var s string
	var ss []string
	fmt.Scan(&n)
	for i := 0; i < n; i++ {
		fmt.Scan(&s)
		ss = append(ss, s)
	}
	ss = mergeSort(ss)
	for _, v := range ss {
		fmt.Println(v)
	}
}

func mergeSort(arr []string) []string {
	if len(arr) == 1 {
		return arr
	}
	left := mergeSort(arr[:len(arr)/2])
	right := mergeSort(arr[len(arr)/2:])
	return merge(left, right)
}

func merge(left, right []string) []string {
	result := make([]string, len(left)+len(right))

	l, r := 0, 0
	for i := 0; i < len(left)+len(right); i++ {
		if len(left) > l && len(right) > r {
			if compareSerial(left[l], right[r]) {
				result[i] = left[l]
				l++
			} else {
				result[i] = right[r]
				r++
			}
		} else if len(left) > l {
			result[i] = left[l]
			l++
		} else if len(right) > r {
			result[i] = right[r]
			r++
		}
	}
	return result
}

func compareSerial(a, b string) bool {
	switch {
	case len(a) < len(b):
		return true
	case len(a) > len(b):
		return false
	}
	sa, sb := serialNumSum(a), serialNumSum(b)
	switch {
	case sa < sb:
		return true
	case sa > sb:
		return false
	}
	if a < b {
		return true
	}
	return false
}

func serialNumSum(serial string) int {
	s := 0
	for _, c := range serial {
		b := int(c - '0')
		if 0 <= b && b <= 9 {
			s += b
		}
	}
	return s
}
