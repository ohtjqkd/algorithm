package main

import (
	"bufio"
	"fmt"
	"os"
)

var reader *bufio.Reader = bufio.NewReader(os.Stdin)
var writer *bufio.Writer = bufio.NewWriter(os.Stdout)

func main() {
	var n, m, ans int
	var line string

	fmt.Fscan(reader, &n, &m)
	board := make([][]int, n)
	for i := 0; i < n; i++ {
		board[i] = make([]int, m)
		fmt.Fscan(reader, &line)
		for j := 0; j < m; j++ {
			board[i][j] = int(line[j] - '0')
		}
	}

	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			t := board[i][j]
			for d := 0; i+d < n && j+d < m; d++ {
				if board[i+d][j] == t && board[i][j+d] == t && board[i+d][j+d] == t {
					ans = max(ans, (d+1)*(d+1))
				}
			}
		}
	}
	fmt.Println(ans)
}
