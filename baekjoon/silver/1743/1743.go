package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	dx     = [4]int{0, 0, 1, -1}
	dy     = [4]int{1, -1, 0, 0}
	board  [][]int
	reader *bufio.Reader = bufio.NewReader(os.Stdin)
)

func main() {
	var n, m, k, r, c int

	fmt.Fscanf(reader, "%d %d %d\n", &n, &m, &k)
	board = make([][]int, n)
	for i := 0; i < n; i++ {
		board[i] = make([]int, m)
	}

	for i := 0; i < k; i++ {
		fmt.Fscanf(reader, "%d %d\n", &r, &c)
		board[r-1][c-1] = 1
	}

	ans := 0
	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			if board[i][j] != 0 {
				ans = max(ans, dfs(i, j))
			}
		}
	}
	fmt.Println(ans)
}

func dfs(x, y int) int {
	var xx, yy int
	board[x][y] = 0
	ret := 1
	for i := 0; i < 4; i++ {
		xx, yy = x+dx[i], y+dy[i]
		if xx < 0 || xx >= len(board) || yy < 0 || yy >= len(board[0]) {
			continue
		}
		if board[xx][yy] != 0 {
			ret += dfs(xx, yy)
		}
	}
	return ret
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
