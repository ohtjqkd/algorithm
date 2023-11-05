package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	r *bufio.Reader = bufio.NewReader(os.Stdin)
	w *bufio.Writer = bufio.NewWriter(os.Stdout)
)

func main() {
	var n, v int
	var dp, arr []int

	defer w.Flush()

	fmt.Fscanf(r, "%d\n", &n)
	dp = make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Fscan(r, &v)
		arr = append(arr, v)
	}
	dp[0] = arr[0]
	max := dp[0]
	for i := 1; i < n; i++ {
		if arr[i] > arr[i]+dp[i-1] {
			dp[i] = arr[i]
		} else {
			dp[i] = arr[i] + dp[i-1]
		}
		if dp[i] > max {
			max = dp[i]
		}
	}
	fmt.Fprintln(w, max)
}
