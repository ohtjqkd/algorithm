package main

import (
	"bufio"
	"fmt"
	"os"
)

var reader *bufio.Reader = bufio.NewReader(os.Stdin)

func main() {
	var n, m, x1, y1, x2, y2 int
	var board [101][101]int
	fmt.Fscanf(reader, "%d %d\n", &n, &m)

	for i := 0; i < n; i++ {
		fmt.Fscanf(reader, "%d %d %d %d\n", &x1, &y1, &x2, &y2)
		for j := x1; j < x2+1; j++ {
			for k := y1; k < y2+1; k++ {
				board[j][k]++
			}
		}
	}
	ans := 0
	for i := 0; i < len(board); i++ {
		for j := 0; j < len(board); j++ {
			if board[i][j] > m {
				ans++
			}
		}
	}
	fmt.Println(ans)
}
