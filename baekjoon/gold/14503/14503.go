package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	reader *bufio.Reader = bufio.NewReader(os.Stdin)
	writer *bufio.Writer = bufio.NewWriter(os.Stdout)
	dx                   = []int{-1, 0, 1, 0}
	dy                   = []int{0, 1, 0, -1}
	N, M   int
	area   [][]int
)

func main() {
	defer writer.Flush()

	var r, c, d int
	ret := 0

	fmt.Fscanf(reader, "%d %d\n", &N, &M)
	fmt.Fscanf(reader, "%d %d %d\n", &r, &c, &d)

	area = make([][]int, N)
	for i := range area {
		area[i] = make([]int, M)
		for j := range area[i] {
			fmt.Fscanf(reader, "%d ", &area[i][j])
		}
	}

	for {
		if area[r][c] == 0 {
			ret++
		}
		area[r][c] = 2
		isAvailable, r1, c1, d1 := checkRotate(r, c, d)
		r, c, d = r1, c1, d1
		if isAvailable {
			continue
		}
		if area[r][c] == 1 {
			fmt.Fprintln(writer, ret)
			return
		}
	}
}

func checkRotate(r, c, d int) (bool, int, int, int) {
	for i := 3; i >= 0; i-- {
		dd := (d + i) % 4
		nr, nc := r+dx[dd], c+dy[dd]
		if nr < 1 || nr >= N-1 || nc < 1 || nc >= M-1 || area[nr][nc] != 0 {
			continue
		}
		return true, nr, nc, dd
	}
	return false, r - dx[d], c - dy[d], d
}
