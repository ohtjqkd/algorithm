package main

import (
	"fmt"
)

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func pop(que *[][2]int) [2]int {
	var ret = (*que)[0]
	*que = (*que)[1:]
	return ret
}

func dfs(visited *[][]int, N, x, y, day int, board *[][]int, L, R int, isChanged *bool) {
	var dx = []int{0, 0, -1, 1}
	var dy = []int{-1, 1, 0, 0}
	var que = [][2]int{}
	var loc = [][2]int{}
	var sum = (*board)[x][y]
	(*visited)[x][y]++
	que = append(que, [2]int{x, y})
	loc = append(loc, [2]int{x, y})
	for len(que) > 0 {
		var cur = pop(&que)
		var x, y = cur[0], cur[1]
		for i := 0; i < 4; i++ {
			var nx = cur[0] + dx[i]
			var ny = y + dy[i]
			if nx < 0 || nx >= N || ny < 0 || ny >= N || abs((*board)[x][y]-(*board)[nx][ny]) < L || abs((*board)[x][y]-(*board)[nx][ny]) > R {
				continue
			}
			if (*visited)[nx][ny] == day+1 {
				continue
			}
			(*visited)[nx][ny]++
			sum += (*board)[nx][ny]
			que = append(que, [2]int{nx, ny})
			loc = append(loc, [2]int{nx, ny})
		}
	}
	if len(loc) > 1 {
		*isChanged = true
		var avg = sum / len(loc)
		for i := 0; i < len(loc); i++ {
			var x, y = loc[i][0], loc[i][1]
			(*board)[x][y] = avg
		}
	}

}

func main() {
	var N int
	var L int
	var R int
	var board [][]int

	fmt.Scan(&N, &L, &R)
	for i := 0; i < N; i++ {
		var row []int
		for j := 0; j < N; j++ {
			var input int
			fmt.Scan(&input)
			row = append(row, input)
		}
		board = append(board, row)
	}

	var day = 0
	visited := [][]int{}
	for i := 0; i < N; i++ {
		row := []int{}
		for j := 0; j < N; j++ {
			row = append(row, 0)
		}
		visited = append(visited, row)
	}

	for {
		var isChanged = false
		for i := 0; i < N; i++ {
			for j := 0; j < N; j++ {
				if visited[i][j] == day+1 {
					continue
				}
				dfs(&visited, N, i, j, day, &board, L, R, &isChanged)
			}
		}
		if !isChanged {
			break
		}
		day++
	}
	fmt.Println(day)
}
