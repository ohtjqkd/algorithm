package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	reader *bufio.Reader = bufio.NewReader(os.Stdin)
	writer *bufio.Writer = bufio.NewWriter(os.Stdout)
)

func main() {
	var n, m int

	defer writer.Flush()

	fmt.Fscanf(reader, "%d %d\n", &n, &m)
	ans := n * m
	board := make([]string, n)
	for i := 0; i < n; i++ {
		fmt.Fscanf(reader, "%s\n", &board[i])
	}
	for i := 0; i < n-7; i++ {
		for j := 0; j < m-7; j++ {
			ans = min(ans, min(start_x(i, j, board, 'W', 'B'), start_x(i, j, board, 'B', 'W')))
		}
	}
	fmt.Fprintln(writer, ans)
}

func start_x(x, y int, board []string, color1, color2 rune) int {
	var ret = 0
	for i := x; i < x+8; i++ {
		for j := y; j < y+8; j++ {
			if ((i-x+j-y)%2 == 0 && rune(board[i][j]) == color1) || ((i-x+j-y)%2 == 1 &&
				rune(board[i][j]) == color2) {
				ret++
			}
		}
	}
	return ret
}

func min(a, b int) int {
	if a > b {
		return b
	}
	return a
}
