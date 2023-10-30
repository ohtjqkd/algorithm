package main

import (
	"fmt"
	"sort"
)

func main() {
	var n, l, k, ans int
	var easy, hard int
	var scores []int

	fmt.Scan(&n, &l, &k)
	for i := 0; i < n; i++ {
		fmt.Scan(&easy, &hard)
		if l < easy {
			scores = append(scores, 0)
		} else if l >= hard {
			scores = append(scores, 140)
		} else {
			scores = append(scores, 100)
		}
	}
	sort.Slice(scores, func(i, j int) bool {
		return scores[i] > scores[j]
	})
	for i := 0; i < k; i++ {
		ans += scores[i]
	}
	fmt.Println(ans)
}
