package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	reader  *bufio.Reader = bufio.NewReader(os.Stdin)
	writer  *bufio.Writer = bufio.NewWriter(os.Stdout)
	board   [][]int
	max     int = 0
	sum2row [][]int
	sum2col [][]int
	sum3row [][]int
	sum3col [][]int

	rowVec = [][]int{{-1, 0}, {-1, 1}, {-1, 2}, {0, 3}, {1, 2}, {1, 1}, {1, 0}}
	colVec = [][]int{{0, 1}, {1, 1}, {2, 1}, {3, 0}, {2, -1}, {1, -1}, {0, -1}}
)

func main() {
	defer writer.Flush()

	var N, M int

	fmt.Fscanf(reader, "%d %d\n", &N, &M)
	board = make([][]int, N)
	sum2row = make([][]int, N)
	sum2col = make([][]int, N)
	sum3row = make([][]int, N)
	sum3col = make([][]int, N)

	for i := range board {
		board[i] = make([]int, M)
		sum2row[i] = make([]int, M)
		sum2col[i] = make([]int, M)
		sum3row[i] = make([]int, M)
		sum3col[i] = make([]int, M)

		for j := range board[i] {
			fmt.Fscanf(reader, "%d ", &board[i][j])
		}
	}

	for i := 0; i < N; i++ {
		for j := 0; j < M; j++ {
			if j+1 < M {
				sum2row[i][j] = board[i][j] + board[i][j+1]
			} else {
				sum2row[i][j] = -1
			}

			if i+1 < N {
				sum2col[i][j] = board[i][j] + board[i+1][j]
			} else {
				sum2col[i][j] = -1
			}

			if i+2 < N {
				sum3col[i][j] = board[i][j] + board[i+1][j] + board[i+2][j]
			} else {
				sum3col[i][j] = -1
			}

			if j+2 < M {
				sum3row[i][j] = board[i][j] + board[i][j+1] + board[i][j+2]
			} else {
				sum3row[i][j] = -1
			}
		}
	}

	for i := 0; i < N; i++ {
		for j := 0; j < M; j++ {
			// square
			if sum2row[i][j] > 0 && i+1 < N && sum2row[i+1][j] > 0 {
				max = maxInt(max, sum2row[i][j]+sum2row[i+1][j])
			}
			if sum2row[i][j] > 0 && i+1 < N && j+1 < M && sum2row[i+1][j+1] > 0 {
				max = maxInt(max, sum2row[i][j]+sum2row[i+1][j+1])
			}
			if i+1 < N && j+1 < M && sum2row[i][j+1] > 0 && sum2row[i+1][j] > 0 {
				max = maxInt(max, sum2row[i][j+1]+sum2row[i+1][j])
			}
			if sum2col[i][j] > 0 && i+1 < N && j+1 < M && sum2col[i+1][j+1] > 0 {
				max = maxInt(max, sum2col[i][j]+sum2col[i+1][j+1])
			}
			if i+1 < N && j+1 < M && sum2col[i+1][j] > 0 && sum2col[i][j+1] > 0 {
				max = maxInt(max, sum2col[i+1][j]+sum2col[i][j+1])
			}

			for k := 0; k < 7; k++ {
				if rowVec[k][0]+i >= 0 && rowVec[k][0]+i < N && rowVec[k][1]+j >= 0 && rowVec[k][1]+j < M {
					max = maxInt(max, sum3row[i][j]+board[rowVec[k][0]+i][rowVec[k][1]+j])
				}

				if colVec[k][0]+i >= 0 && colVec[k][0]+i < N && colVec[k][1]+j >= 0 && colVec[k][1]+j < M {
					max = maxInt(max, sum3col[i][j]+board[colVec[k][0]+i][colVec[k][1]+j])
				}
			}

		}
	}
	fmt.Fprintln(writer, max)
}

func maxInt(a, b int) int {
	if a > b {
		return a
	}
	return b
}
