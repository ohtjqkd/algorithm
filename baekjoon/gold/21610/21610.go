package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	reader *bufio.Reader = bufio.NewReader(os.Stdin)
	writer *bufio.Writer = bufio.NewWriter(os.Stdout)
	N, M   int
	dx, dy = []int{0, 0, -1, -1, -1, 0, 1, 1, 1}, []int{0, -1, -1, 0, 1, 1, 1, 0, -1}
)

func main() {
	defer writer.Flush()

	var board [][]int

	fmt.Fscanln(reader, &N, &M)

	// read board
	board = make([][]int, N)
	for i := 0; i < N; i++ {
		board[i] = make([]int, N)
		for j := 0; j < N; j++ {
			fmt.Fscanf(reader, "%d ", &board[i][j])
		}
	}

	// initialize clouds
	var clouds map[int]bool = map[int]bool{(N-1)*N + 0: true, (N-1)*N + 1: true, (N-2)*N + 0: true, (N-2)*N + 1: true}

	for i := 0; i < M; i++ {
		var dir, weight int
		fmt.Fscanf(reader, "%d %d\n", &dir, &weight)

		fmt.Fprintln(writer, dir, weight)
		movedCloud := moveCloud(clouds, dir, weight)
		addWater(movedCloud, board)
		dupWater(movedCloud, board)
		clouds, board = makeCloud(board, clouds)
	}

	s := 0
	for _, row := range board {
		for _, v := range row {
			s += v
		}
	}
	fmt.Fprintln(writer, board)
	fmt.Fprintln(writer, s)
}

func makeCloud(m [][]int, beforeCloud map[int]bool) (map[int]bool, [][]int) {
	c := make(map[int]bool)
	for i := 0; i < N; i++ {
		for j := 0; j < N; j++ {
			if m[i][j] >= 2 && !beforeCloud[i*N+j] {
				c[i*N+j] = true
				m[i][j] -= 2
			}
		}
	}
	return c, m
}

func moveCloud(cloud map[int]bool, dir, weight int) map[int]bool {
	newCloud := make(map[int]bool)
	for k := range cloud {
		x, y := k/N, k%N
		nx, ny := (N+(x+weight*dx[dir])%N)%N, (N+(y+weight*dy[dir])%N)%N

		newCloud[nx*N+ny] = true
	}
	return newCloud
}

func addWater(cloud map[int]bool, m [][]int) {
	for k := range cloud {
		x, y := k/N, k%N
		m[x][y]++
	}
}

func dupWater(cloud map[int]bool, m [][]int) {
	for k := range cloud {
		x, y := k/N, k%N
		m[x][y]++
		dup := 0
		for _, d := range [][]int{{-1, -1}, {-1, 1}, {1, -1}, {1, 1}} {
			rr, cc := x+d[0], y+d[1]
			fmt.Fprintln(writer, rr, cc, m)
			if !(rr < 0 || cc < 0 || rr >= N || cc >= N) && m[rr][cc] > 0 {
				dup++
			}
		}
		m[x][y] += dup
	}
}
