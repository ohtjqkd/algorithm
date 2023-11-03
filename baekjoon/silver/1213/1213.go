// TODO
// golang fail

package main

import (
	"fmt"
	"strings"
)

func main() {
	var s string
	var cSet []rune

	fmt.Scan(&s)
	cMap := make(map[rune]int)
	ans := make([]string, len(s))
	for i := 0; i < len(s); i++ {
		c := rune(s[i])
		if cMap[c] == 0 {
			cSet = append(cSet, c)
		}
		cMap[rune(s[i])]++
	}
	cSet = mergeSort(cSet)
	avail, v := checkPalindrome(cMap)
	if avail {
		if v != nil {
			ans[len(s)/2] = string(*v)
			cMap[*v]--
		}
		k := 0
		for i := 0; i < len(cSet); i++ {
			target := cSet[i]
			for j := 0; j < cMap[target]/2; j++ {
				ans[k] = string(target)
				ans[len(s)-k-1] = string(target)
				k++
			}
		}
		fmt.Println(strings.Join(ans, ""))
	} else {
		fmt.Println("I'm Sorry Hansoo")
	}
}

func checkPalindrome(cMap map[rune]int) (bool, *rune) {
	oddCnt := 0

	ov := new(rune)
	for k, v := range cMap {
		if v%2 == 1 {
			oddCnt++
			*ov = k
		}
		if oddCnt > 1 {
			return false, nil
		}
	}
	return true, ov
}

func mergeSort(arr []rune) []rune {
	if len(arr) <= 1 {
		return arr
	}

	mid := len(arr) / 2
	left := mergeSort(arr[:mid])
	right := mergeSort(arr[mid:])

	return merge(left, right)
}

func merge(left, right []rune) []rune {
	result := make([]rune, len(left)+len(right))

	l, r := 0, 0
	for i := 0; i < len(left)+len(right); i++ {
		if len(left) > l && len(right) > r {
			if left[l] < right[r] {
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
