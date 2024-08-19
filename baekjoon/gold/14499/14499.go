package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

var (
	reader *bufio.Reader = bufio.NewReader(os.Stdin)
	writer *bufio.Writer = bufio.NewWriter(os.Stdout)
	dx                   = []int{0, 0, 0, -1, 1}
	dy                   = []int{0, 1, -1, 0, 0}
)

type Dice struct {
	top, bottom, north, south, east, west int
}

func (d *Dice) move(dir int) {
	switch dir {
	case 1: // east
		d.top, d.bottom, d.east, d.west = d.west, d.east, d.top, d.bottom
	case 2: // west
		d.top, d.bottom, d.east, d.west = d.east, d.west, d.bottom, d.top
	case 3: // north
		d.top, d.bottom, d.north, d.south = d.south, d.north, d.top, d.bottom
	case 4: // south
		d.top, d.bottom, d.north, d.south = d.north, d.south, d.bottom, d.top
	}
}

func NewDice() *Dice {
	return &Dice{0, 0, 0, 0, 0, 0}
}

func main() {
	defer writer.Flush()

	var N, M, x, y, K int
	var board [][]int

	fmt.Fscanf(reader, "%d %d %d %d %d\n", &N, &M, &x, &y, &K)
	board = make([][]int, N)
	for i := range board {
		nums, _ := reader.ReadString('\n')
		nums = strings.TrimSpace(nums)
		board[i] = splitInt(nums)
	}
	nums, _ := reader.ReadString('\n')
	nums = strings.TrimSpace(nums)
	commands := splitInt(nums)
	dice := NewDice()

	for _, cmd := range commands {
		nx, ny := x+dx[cmd], y+dy[cmd]
		if nx < 0 || nx >= N || ny < 0 || ny >= M {
			continue
		}
		x, y = nx, ny
		dice.move(cmd)
		if board[x][y] == 0 {
			board[x][y] = dice.bottom
		} else {
			dice.bottom = board[x][y]
			board[x][y] = 0
		}
		fmt.Fprintf(writer, "%d\n", dice.top)
	}
}

func splitInt(s string) []int {
	var res []int
	for _, v := range strings.Fields(s) {
		res = append(res, parseInt(v))
	}
	return res
}

func parseInt(s string) int {
	var n int
	fmt.Sscanf(s, "%d", &n)
	return n
}
