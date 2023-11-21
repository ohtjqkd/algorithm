package main

import (
	"bufio"
	"os"
)

var (
	r = bufio.NewReader(os.Stdin)
	w = bufio.NewWriter(os.Stdout)
)

func main() {

}

func rotate90(n int, board [][]int) [][]int {
	ret := make([][]int, n)
	for i := 0; i < n; i++ {
		ret[i] = make([]int, n)
	}
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			ret[j][n-i-1] = board[i][j]
		}
	}
	return ret
}

func swipe(n int, line []int) {
	idx := 0
	for i := 0; i < n-1; i++ {
		if line[i] == line[i+1] {
			line[idx] = line[i] * 2
			line[i+1] = 0
			i++
		} else {
			line[idx] = line[i]
		}
		idx++
	}
}

func dfs(n, m int, board [][]int) int {
	ret := 0
	for i := 0; i < n; i++ {
		ret = max(nil, ret, max(board[i]))
	}
	if n == 0 {
		return ret
	}
	for i := 0; i < 4; i++ {
		swiped := 
	}
}

func max(iter []int, n ...int) int {
	if iter == nil {
		iter = n
	}
	for _, v := range iter {
		if v > iter[0] {
			iter[0] = v
		}
	}
	return iter[0]
}
