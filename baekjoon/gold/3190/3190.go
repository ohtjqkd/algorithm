package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	reader    *bufio.Reader = bufio.NewReader(os.Stdin)
	writer    *bufio.Writer = bufio.NewWriter(os.Stdout)
	dx        []int         = []int{0, 1, 0, -1}
	dy        []int         = []int{1, 0, -1, 0}
	head      []int         = []int{1, 1}
	dir, time int           = 0, 0
)

func main() {
	defer writer.Flush()

	var n, k, l int
	fmt.Fscanf(reader, "%d\n", &n)
	fmt.Fscanf(reader, "%d\n", &k)

	apple := make(map[int]bool)
	board := make([][]int, n)
	for i := range board {
		board[i] = make([]int, n)
		for j := range board[i] {
			board[i][j] = 0
		}
	}

	for i := 0; i < k; i++ {
		var a, b int

		fmt.Fscanf(reader, "%d %d\n", &a, &b)
		apple[a*n+b] = true
	}

	board[0][0] = 1

	fmt.Fscanf(reader, "%d\n", &l)
	turnTime := make([]rune, 10001)
	for i := 0; i < l; i++ {
		var t int
		var d rune
		fmt.Fscanf(reader, "%d %c\n", &t, &d)
		turnTime[t] = d
	}

	snake := [][2]int{{1, 1}}

	for {
		nx, ny := head[0]+dx[dir], head[1]+dy[dir]
		if nx < 1 || nx > n || ny < 1 || ny > n || board[nx-1][ny-1] == 1 {
			fmt.Fprintln(writer, time+1)
			return
		}

		snake = append(snake, [2]int{nx, ny})
		board[nx-1][ny-1] = 1

		if apple[nx*n+ny] == false {
			tail := snake[0]
			snake = snake[1:]
			board[tail[0]-1][tail[1]-1] = 0
		} else {
			delete(apple, nx*n+ny)
		}

		head = []int{nx, ny}
		time += 1
		if turnTime[time] == 'L' {
			dir = (dir + 3) % 4
		} else if turnTime[time] == 'D' {
			dir = (dir + 1) % 4
		}
	}
}
