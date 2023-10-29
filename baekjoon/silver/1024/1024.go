package main

import (
	"fmt"
	"strconv"
	"strings"
)

func main() {
	var n, k int

	fmt.Scanf("%d %d", &n, &k)
	s, d := solution(n, k)

	ans := make([]string, d)
	for i := 0; i < d; i++ {
		ans[i] = strconv.Itoa(s + i)
	}
	fmt.Println(strings.Join(ans, " "))
}

func solution(n, k int) (s, d int) {
	for ; k <= 100; k++ {
		for i := n/k - k; i < n/k+k; i++ {
			if i < 0 {
				continue
			}
			if float64(k)*(2*float64(i)+float64(k)-1)/2 == float64(n) {
				return i, k
			}
		}
	}
	return -1, 1
}
