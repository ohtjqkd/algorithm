package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func max(a, b int) int {
	if a >= b {
		return a
	}
	return b
}

func main() {
	var r1, c1, r2, c2 int

	writer := bufio.NewWriterSize(os.Stdout, 1000000)
	defer writer.Flush()
	fmt.Scan(&r1, &c1, &r2, &c2)
	board := make([][]int, r2-r1+1)
	for i := r1; i <= r2; i++ {
		board[i-r1] = make([]int, c2-c1+1)
		for j := c1; j <= c2; j++ {
			board[i-r1][j-c1] = 0
		}
	}
	maxValue := 0
	for i := 0; i < r2-r1+1; i++ {
		for j := 0; j < c2-c1+1; j++ {
			var index int
			x, y := i+r1, j+c1
			level := max(abs(x), abs(y))
			startLevelLoc := [2]int{level - 1, level}
			startValue := (level*2-1)*(level*2-1) + 1
			if y == level && x <= startLevelLoc[0] {
				index = abs(startLevelLoc[0] - x)
			} else if -x == level {
				index = abs(startLevelLoc[1]-y) + level*2 - 1
			} else if y == -level {
				index = abs(level+x) + level*4 - 1
			} else {
				index = y + level*7 - 1
			}
			board[i][j] = startValue + index
			maxValue = max(maxValue, board[i][j])
		}
	}
	maxExp := len(strconv.Itoa(maxValue))
	for i := 0; i < len(board); i++ {
		for j := 0; j < len(board[0]); j++ {
			fmt.Fprintf(writer, "%*d", maxExp, board[i][j])
			if j != len(board[0])-1 {
				fmt.Fprint(writer, " ")
			}
		}
		fmt.Fprintln(writer)
	}
}
