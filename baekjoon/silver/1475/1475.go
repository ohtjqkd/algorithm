package main

import (
	"fmt"
	"math"
)

func main() {
	var nStr string
	var cnt [10]int

	fmt.Scan(&nStr)
	for _, v := range nStr {
		cnt[v-'0']++
	}
	max := 0
	for i, v := range cnt {
		if i == 6 || i == 9 {
			continue
		}
		if v > max {
			max = v
		}
	}
	sn := int(math.Ceil((float64(cnt[6]) + float64(cnt[9])) / 2))
	if max > sn {
		fmt.Println(max)
	} else {
		fmt.Println(sn)
	}
}
