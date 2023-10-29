// Need to confirm that this problem can be solved by go

package main

import (
	"fmt"
	"sort"
)

func max(a []int) (idx, val int) {
	for i, v := range a {
		if val < v {
			idx, val = i, v
		}
	}
	return idx, val
}

func main() {
	var n int
	var info [][4]int
	var a, h, w int

	fmt.Scan(&n)
	for i := 0; i < n; i++ {
		fmt.Scan(&a, &h, &w)
		info = append(info, [4]int{i, a, h, w})
	}
	dph := make([]int, n)
	dpi := make([][]int, n)
	for i := 0; i < n; i++ {
		dph[i] = info[i][2]
		dpi[i] = []int{info[i][0]}
	}
	sort.Slice(info, func(i, j int) bool {
		return info[i][3] < info[j][3]
	})
	for i := 0; i < n-1; i++ {
		idx := info[i][0]
		for j := i + 1; j < n; j++ {
			jdx, jh := info[j][0], info[j][2]
			if info[i][1] > info[j][1] || info[i][3] > info[j][3] {
				continue
			}
			if dph[jdx] < dph[idx]+jh {
				dph[jdx] = dph[idx] + jh
				dpi[jdx] = append(dpi[idx], jdx)
			}
		}
	}
	idx, _ := max(dph)
	fmt.Println(dph, dpi)
	fmt.Println(len(dpi[idx]))
	for _, v := range dpi[idx] {
		fmt.Println(v + 1)
	}
}
