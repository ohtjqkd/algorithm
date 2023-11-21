// input
// 3
// 7
// 13 10 12 11 10 11 12
// 5
// 2 4 5 7 9
// 8
// 6 6 6 6 6 6 6 6
// output
// 1
// 4
// 0

package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

var (
	r = bufio.NewReader(os.Stdin)
	w = bufio.NewWriter(os.Stdout)
)

func main() {
	defer w.Flush()

	var t, n, ans int

	fmt.Fscan(r, &t)
	for i := 0; i < t; i++ {
		fmt.Fscan(r, &n)
		height := make([]int, n)
		for j := 0; j < n; j++ {
			fmt.Fscan(r, &height[j])
		}
		sort.Slice(height, func(i2, j int) bool {
			return height[i2] < height[j]
		})
		ans = height[len(height)-1] - height[len(height)-2]
		for j := len(height) - 1; j >= 0; j-- {
			if ans < height[j]-height[(len(height)+j-2)%len(height)] {
				ans = height[j] - height[(len(height)+j-2)%len(height)]
			}
		}
		fmt.Fprintln(w, ans)
	}
}
