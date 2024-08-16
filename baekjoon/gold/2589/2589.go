package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	writer  *bufio.Writer = bufio.NewWriter(os.Stdout)
	reader  *bufio.Reader = bufio.NewReader(os.Stdin)
	board   [][]byte
	visited [][]bool
	dist    [][]int
	dx      = []int{0, 0, 1, -1}
	dy      = []int{1, -1, 0, 0}
	n, m    int
)

func main() {
	defer writer.Flush()
	var ans int
	fmt.Fscan(reader, &n)
	fmt.Fscanf(reader, "%d\n", &m)

	visited = make([][]bool, n)
	dist = make([][]int, n)

	for i := 0; i < n; i++ {
		board = append(board, readline())
		visited[i] = make([]bool, m)
		dist[i] = make([]int, m)
		for j := 0; j < m; j++ {
			visited[i][j] = false
			dist[i][j] = 0
		}
	}

	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			if board[i][j] == 'L' {
				ans = max(ans, bfs(i, j))
			}
		}
	}
	fmt.Fprintln(writer, ans)
}

func bfs(x, y int) int {
	visited := make(map[int]bool, 1024)
	ret := 0
	dist[x][y] = 0
	visited[x*m+y] = true
	q := []int{x*m + y}

	for len(q) > 0 {
		t := q[0]
		q = q[1:]
		for i := 0; i < 4; i++ {
			nx, ny := t/m+dx[i], t%m+dy[i]
			if nx < 0 || nx >= n || ny < 0 || ny >= m {
				continue
			}
			if visited[nx*m+ny] || board[nx][ny] == 'W' {
				continue
			}
			visited[nx*m+ny] = true
			dist[nx][ny] = dist[t/m][t%m] + 1
			q = append(q, nx*m+ny)
			ret = max(ret, dist[nx][ny])
		}
	}
	return ret
}

func readline() []byte {
	buf, _, _ := reader.ReadLine()
	return buf
}

func max(a ...int) int {
	var m int
	for _, v := range a {
		if v > m {
			m = v
		}
	}
	return m
}
