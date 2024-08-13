package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	r = bufio.NewReader(os.Stdin)
	w = bufio.NewWriter(os.Stdout)
)

func main() {
	defer w.Flush()
	var n, m int
	var ans int
	var tmp string

	fmt.Fscan(r, &n, &m)
	board := make([][]bool, n)
	for i := 0; i < n; i++ {
		board[i] = make([]bool, m)
		fmt.Fscan(r, &tmp)
		for j := 0; j < m; j++ {
			if tmp[j] == '1' {
				board[i][j] = true
			} else {
				board[i][j] = false
			}
		}
	}
	for i := n - 1; i >= 0; i-- {
		for j := m - 1; j >= 0; j-- {
			if board[i][j] {
				ans++
				for k := 0; k <= i; k++ {
					for l := 0; l <= j; l++ {
						board[k][l] = !board[k][l]
					}
				}
			}
		}
	}
	fmt.Fprintln(w, ans)
}
