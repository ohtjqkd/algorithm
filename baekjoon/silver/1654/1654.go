package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

var (
	reader *bufio.Reader = bufio.NewReader(os.Stdin)
)

func main() {
	var k, n, l int
	var lans []int
	ans := 0
	MAX := math.MaxInt32

	fmt.Fscanf(reader, "%d %d\n", &k, &n)
	for i := 0; i < k; i++ {
		fmt.Fscanf(reader, "%d\n", &l)
		lans = append(lans, l)
	}

	s, e := 0, MAX
	for s <= e {
		mid := (s + e) / 2
		cnt := 0
		for _, length := range lans {
			cnt += (length / mid)
		}
		if cnt < n {
			e = mid - 1
		} else {
			ans = mid
			s = mid + 1
		}
	}
	fmt.Println(ans)
}
