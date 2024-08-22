package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	reader  *bufio.Reader = bufio.NewReader(os.Stdin)
	writer  *bufio.Writer = bufio.NewWriter(os.Stdout)
	dx                    = []int{0, 1, 0, -1}
	dy                    = []int{1, 0, -1, 0}
	axisArr               = []int{6, 3, 1, 4}
	restArr               = []int{5, 2}
	score   [][]int
	board   [][]int
	N, M, K int
)

func solution() int {
	defer writer.Flush()
	answer := 0

	dir := 0

	fmt.Fscanf(reader, "%d %d %d\n", &N, &M, &K)

	board = make([][]int, N)
	score = make([][]int, N)
	for i := 0; i < N; i++ {
		board[i] = make([]int, M)
		score[i] = make([]int, M)
		for j := 0; j < M; j++ {
			fmt.Fscanf(reader, "%d ", &board[i][j])
			score[i][j] = -1
		}
	}

	for i := 0; i < N; i++ {
		for j := 0; j < M; j++ {
			if score[i][j] == -1 {
				same := dfs(i, j, board[i][j])
				multi := len(same)
				for _, v := range same {
					x, y := v[0], v[1]
					score[x][y] = multi * board[i][j]
				}
			}
		}
	}

	r, c, dir := 0, 0, 0

	for i := 0; i < K; i++ {
		rr, cc := r+dx[dir], c+dy[dir]
		if rr < 0 || rr >= N || cc < 0 || cc >= M {
			dir = reverseDir(dir)
		}
		dir, axisArr, r, c = goFunc(dir, axisArr, r, c)
		if axisArr[0] < board[r][c] {
			dir, axisArr, restArr = reverseRotate(dir, axisArr, restArr)
		} else if axisArr[0] > board[r][c] {
			dir, axisArr, restArr = rotate(dir, axisArr, restArr)
		}
		answer += score[r][c]
	}
	return answer
}

func main() {
	fmt.Println(solution())
}

func dfs(row, col, t int) [][2]int {
	ret := [][2]int{{row, col}}
	score[row][col] = 1
	for i := 0; i < 4; i++ {
		rr, cc := row+dx[i], col+dy[i]
		if rr < 0 || rr >= N || cc < 0 || cc >= M || score[rr][cc] != -1 || board[rr][cc] != t {
			continue
		}
		ret = append(ret, dfs(rr, cc, t)...)
	}
	return ret
}

func convertAxis(axisArr, restArr []int) {
	axisArr1, axisArr3 := axisArr[1], axisArr[3]
	restArr0, restArr1 := restArr[0], restArr[1]
	axisArr[1], axisArr[3] = restArr0, restArr1
	restArr[0], restArr[1] = axisArr1, axisArr3
}

func rotate(dir int, axisArr, restArr []int) (int, []int, []int) {
	dir = (dir + 1) % 4
	convertAxis(axisArr, restArr)
	return dir, axisArr, restArr
}

func reverseRotate(dir int, axisArr, restArr []int) (int, []int, []int) {
	dir = (dir + 3) % 4
	convertAxis(axisArr, restArr)
	return dir, axisArr, restArr
}

func reverseDir(dir int) int {
	return (dir + 2) % 4
}

func goFunc(dir int, axisArr []int, r, c int) (int, []int, int, int) {
	if dir < 2 {
		axisArr = append(axisArr[1:], axisArr[0])
	} else {
		axisArr = append([]int{axisArr[len(axisArr)-1]}, axisArr[:len(axisArr)-1]...)
	}
	r, c = r+dx[dir], c+dy[dir]
	return dir, axisArr, r, c
}
