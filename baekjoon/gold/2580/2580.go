package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	sc = bufio.NewScanner(os.Stdin)
	wr = bufio.NewWriter(os.Stdout)
	z  = 0
	o  = 1
)

type Cand struct {
	colSet []*CustomMap
	rowSet []*CustomMap
	secSet []*CustomMap
}

type CustomMap map[int]*int

func (m CustomMap) Get(key int) *int {
	if val, exists := m[key]; exists {
		return val
	}
	return nil
}

func (m CustomMap) Set(key int, val *int) {
	m[key] = val
}

func NewCustomMap() *CustomMap {
	m := make(CustomMap)
	for i := 1; i <= 9; i++ {
		m[i] = &o
	}
	return &m
}

type Empty struct {
	x, y  int
	avail *CustomMap
}

func NewEmpty(x, y int, avail *CustomMap) *Empty {
	return &Empty{x: x, y: y, avail: avail}
}

func main() {
	defer wr.Flush()
	var location []*Empty
	var locationMap [9][9]*Empty
	board := make([][]int, 9)
	for i := 0; i < 9; i++ {
		board[i] = make([]int, 9)
	}
	colSet := make([]*CustomMap, 9)
	rowSet := make([]*CustomMap, 9)
	secSet := make([]*CustomMap, 9)
	for i := 0; i < 9; i++ {
		colSet[i] = NewCustomMap()
		rowSet[i] = NewCustomMap()
		secSet[i] = NewCustomMap()
		for j := 0; j < 9; j++ {
			locationMap[i][j] = NewEmpty(i, j, NewCustomMap())
		}
	}
	for i := 0; i < 9; i++ {
		for j := 0; j < 9; j++ {
			n := nextInt()
			board[i][j] = n
			for k := 0; k < 9; k++ {
				delete(*locationMap[i][k].avail, board[i][j])
				delete(*locationMap[k][j].avail, board[i][j])
			}
			if board[i][j] == 0 {
				location = append(location, locationMap[i][j])
				(*rowSet[i])[n] = &z
				(*colSet[j])[n] = &z
				(*secSet[(i/3)*3+j/3])[n] = &z
			}
		}
	}

	candSet := Cand{colSet, rowSet, secSet}

	result := sudoku(board, location, &candSet)
	for i := 0; i < 9; i++ {
		for j := 0; j < 9; j++ {
			fmt.Fprintf(wr, "%d", result[i][j])
			if j != 8 {
				fmt.Fprint(wr, " ")
			}
		}
		fmt.Fprintln(wr)
	}
}

func sudoku(board [][]int, locations []*Empty, cand *Cand) [][]int {
	if len(locations) == 0 {
		return board
	} else {
		t := locations[0]
		rowSet := cand.rowSet[t.x]
		colSet := cand.colSet[t.y]
		secSet := cand.secSet[(t.x/3)*3+t.y/3]

		for k := range *t.avail {
			if t.avail.Get(k) == nil || *t.avail.Get(k) == 0 || *rowSet.Get(k) == 0 || *colSet.Get(k) == 0 || *secSet.Get(k) == 0 {
				continue
			}
			var changed []CustomMap
			board[t.x][t.y] = k
			t.avail.Set(k, &z)
			if *rowSet.Get(k) == 1 {
				changed = append(changed, *rowSet)
				rowSet.Set(k, &z)
			}

			if *colSet.Get(k) == 1 {
				changed = append(changed, *colSet)
				colSet.Set(k, &z)
			}

			if *secSet.Get(k) == 1 {
				changed = append(changed, *secSet)
				secSet.Set(k, &z)
			}

			tmpArr := sudoku(board, locations[1:], cand)
			if tmpArr != nil {
				return tmpArr
			}

			board[t.x][t.y] = 0
			t.avail.Set(k, &o)

			for _, m := range changed {
				m.Set(k, &o)
			}
		}
	}
	return nil
}

func nextInt() int {
	ret := 0
	fmt.Scanf("%d", &ret)
	return ret
}
