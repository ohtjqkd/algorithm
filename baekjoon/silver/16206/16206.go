// input
// 5 8
// 34 45 56 12 23
// output
// 8
package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

var sc = bufio.NewScanner(os.Stdin)

func main() {
	nm := nextIntArr(0)
	n, m := nm[0], nm[1]

	arr := nextIntArr(n)
	sort.Slice(arr, func(i, j int) bool {
		if arr[i]%10 == 0 && arr[j]%10 == 0 {
			return arr[i] < arr[j]
		} else if arr[i]%10 == 0 {
			return true
		} else if arr[j]%10 == 0 {
			return false
		}
		return arr[i] < arr[j]
	})
	ans := 0
	for i := 0; i < len(arr) && m > 0; i++ {
		for arr[i] >= 10 && m > 0 {
			arr[i] -= 10
			switch {
			case arr[i] == 0:
				ans++
				break
			case arr[i] < 0:
				break
			default:
				ans++
				m--
			}
			if m == 0 && arr[i] == 10 {
				ans++
			}
		}
	}
	fmt.Println(ans)
}

func nextIntArr(size int) []int {
	sc.Scan()
	if size == 0 {
		var ret []int
		i := 0
		for _, v := range sc.Bytes() {
			if v == ' ' {
				ret = append(ret, i)
				i = 0
			} else if v >= '0' && v <= '9' {
				i = i*10 + int(v-'0')
			}
		}
		ret = append(ret, i)
		return ret
	} else {
		ret := make([]int, size)
		i, idx := 0, 0
		for _, v := range sc.Bytes() {
			if v == ' ' {
				ret[idx] = i
				idx++
				i = 0
			} else if v >= '0' && v <= '9' {
				i = i*10 + int(v-'0')
			}
		}
		ret[idx] = i
		return ret
	}
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
