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
	var n, m, v int
	var nums []int
	defer w.Flush()

	d := make(map[int]bool)

	fmt.Fscanf(r, "%d\n", &n)
	fmt.Fscanf(r, "%d\n", &m)

	for i := 0; i < n; i++ {
		fmt.Fscan(r, &v)
		nums = append(nums, v)
		d[v] = true
	}

	ans := 0
	for _, v := range nums {
		if d[v] == true {
			d[v] = false
			if d[m-v] == true {
				d[m-v] = false
				ans++
			}
		}
	}
	fmt.Fprintln(w, ans)
}
