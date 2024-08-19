package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	reader *bufio.Reader = bufio.NewReader(os.Stdin)
	writer *bufio.Writer = bufio.NewWriter(os.Stdout)
	N, L   int
	board  [][]int
)

func main() {
	defer writer.Flush()

	var answer int = 0
	fmt.Fscanf(reader, "%d %d\n", &N, &L)

	board = make([][]int, N)
	for i := 0; i < N; i++ {
		board[i] = make([]int, N)
		for j := 0; j < N; j++ {
			fmt.Fscanf(reader, "%d ", &board[i][j])
		}
	}

	for i := 0; i < N; i++ {
		if checkRow(i) {
			answer++
		}
		if checkCol(i) {
			answer++
		}
	}
	fmt.Fprintln(writer, answer)
}

func checkRow(r int) bool {
	ladder := make(map[int]bool)

	for i := 0; i < N; {
		curr := board[r][i]
		if i+1 == N {
			return true
		}
		switch curr - board[r][i+1] {
		case 0:
			i++
		case -1: // next block is higher than current block
			// check if there are enough blocks to make a ladder before the next block
			for j := 0; j < L; j++ {
				if i-j < 0 || ladder[i-j] || curr != board[r][i-j] {
					return false
				}
				ladder[i-j] = true
			}
			i++
		case 1: // next block is lower than current block
			// check if there are enough blocks to make a ladder after the next block
			for j := 1; j < L+1; j++ {
				if i+j >= N || ladder[i+j] || curr-1 != board[r][i+j] {
					return false
				}
				ladder[i+j] = true
			}
			i = i + L
		default:
			return false
		}
	}
	return true
}

func checkCol(c int) bool {
	ladder := make(map[int]bool)

	for i := 0; i < N; {
		curr := board[i][c]
		if i+1 == N {
			return true
		}
		switch curr - board[i+1][c] {
		case 0:
			i++
		case -1: // next block is higher than current block
			// check if there are enough blocks to make a ladder before the next block
			for j := 0; j < L; j++ {
				if i-j < 0 || ladder[i-j] || curr != board[i-j][c] {
					return false
				}
				ladder[i-j] = true
			}
			i++
		case 1: // next block is lower than current block

			// check if there are enough blocks to make a ladder after the next block
			for j := 1; j < L+1; j++ {
				if i+j >= N || ladder[i+j] || curr-1 != board[i+j][c] {
					return false
				}
				ladder[i+j] = true
			}
			i = i + L
		default:
			return false
		}
	}
	return true
}
