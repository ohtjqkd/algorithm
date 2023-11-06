package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

var (
	r *bufio.Reader = bufio.NewReader(os.Stdin)
	w *bufio.Writer = bufio.NewWriter(os.Stdout)
)

func main() {
	var n, st, et int
	var times [][]int

	defer w.Flush()
	fmt.Fscanf(r, "%d\n", &n)
	for i := 0; i < n; i++ {
		fmt.Fscanf(r, "%d %d\n", &st, &et)
		times = append(times, []int{st, et})
	}
	sort.Slice(times, func(i, j int) bool {
		if times[i][1] < times[j][1] {
			return true
		} else if times[i][1] == times[j][1] && times[i][0] < times[j][0] {
			return true
		}
		return false
	})
	lt, ans := 0, 0
	for _, v := range times {
		if v[0] >= lt {
			ans++
			lt = v[1]
		}
	}
	fmt.Fprintln(w, ans)
}
