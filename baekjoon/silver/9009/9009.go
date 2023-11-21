// input
// 4
// 100
// 200
// 12345
// 1003
// output
// 3 8 89
// 1 55 144
// 1 34 377 987 10946
// 3 13 987

package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

var (
	r = bufio.NewReader(os.Stdin)
	w = bufio.NewWriter(os.Stdout)
)

func main() {
	defer w.Flush()

	var t, n int
	f1, f2 := 0, 1
	var fArr = []int{f1, f2}
	for f2 < 1_000_000_000 {
		f1, f2 = f2, f1+f2
		fArr = append(fArr, f2)
	}
	fmt.Fscan(r, &t)
	for i := 0; i < t; i++ {
		fmt.Fscan(r, &n)
		var ans []string
		for j := len(fArr) - 1; j >= 0 && n > 0; j-- {
			if fArr[j] <= n {
				ans = append(ans, strconv.Itoa(fArr[j]))
				n -= fArr[j]
			}
		}
		for i2, j := 0, len(ans)-1; i2 < j; i2, j = i2+1, j-1 {
			ans[i2], ans[j] = ans[j], ans[i2]
		}
		fmt.Fprintln(w, strings.Join(ans, " "))
	}
}
