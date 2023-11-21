// input
// 4 4
// 1 2 4 6
// 16 9 13 11
// 5 10 8 15
// 12 14 7 3
// output
// 72
package main

import (
	"bufio"
	"fmt"
	"os"
)

var sc = bufio.NewScanner(os.Stdin)

func main() {
	var n, m int

	nm := nextIntArr(2)
	n, m = nm[0], nm[1]
	a, ans := make([][]int, n), 0
	for i := range a {
		a[i] = nextIntArr(m)
	}
	rx, cx := make([]int, n), make([]int, m)
	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			if a[i][j] > a[i][rx[i]] {
				rx[i] = j
			}
			if a[i][j] > a[cx[j]][j] {
				cx[j] = i
			}
		}
	}
	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			if rx[i] != j && cx[j] != i {
				ans += a[i][j]
			}
		}
	}
	fmt.Println(ans)
}

func nextIntArr(size int) []int {
	ret := make([]int, size)
	idx, e := 0, 0
	sc.Scan()
	for i := range sc.Bytes() {
		if sc.Bytes()[i] == ' ' {
			ret[idx] = e
			e = 0
			idx++
		} else {
			e = e*10 + int(sc.Bytes()[i]-'0')
		}
		if i == len(sc.Bytes())-1 {
			ret[idx] = e
		}
	}
	return ret
}

func nextInt() int {
	sc.Scan()
	fmt.Println(sc.Bytes())
	r := 0
	for i := range sc.Bytes() {
		r = r*10 + int(sc.Bytes()[i]-'0')
	}
	return r
}
