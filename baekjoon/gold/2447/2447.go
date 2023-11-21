package main

import (
	"bufio"
	"fmt"
	"os"
)

var writer = bufio.NewWriter(os.Stdout)
var board [][]rune

func main() {
	defer writer.Flush()
	var n int

	fmt.Scan(&n)
	board = make([][]rune, n)
	for i := 0; i < n; i++ {
		board[i] = make([]rune, n)
		for j := 0; j < n; j++ {
			board[i][j] = ' '
		}
	}
	setRunes(0, 0, n)
	for i := 0; i < n; i++ {
		fmt.Fprintln(writer, string(board[i]))
	}
}

func setRunes(x, y, n int) {
	if n == 1 {
		board[x][y] = '*'
		return
	}
	div := n / 3
	for i := 0; i < 3; i++ {
		for j := 0; j < 3; j++ {
			if i == 1 && j == 1 {
				continue
			}
			setRunes(x+div*i, y+div*j, div)
		}
	}
}
