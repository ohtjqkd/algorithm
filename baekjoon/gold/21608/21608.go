package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	r = bufio.NewReader(os.Stdin)
	w = bufio.NewWriter(os.Stdout)
)

type Pair struct {
	v    int
	pair []int
}

func main() {
	var n, v1, v2, v3, v4, v5, score int
	var res [][]int
	var likePair []Pair
	var likePairOtherside map[int][]int

	defer w.Flush()
	fmt.Fscan(r, &n)
	likePairOtherside = make(map[int][]int)
	for i := 0; i < n*n; i++ {
		fmt.Fscan(r, &v1, &v2, &v3, &v4, &v5)
		p := Pair{v1 - 1, []int{v2 - 1, v3 - 1, v4 - 1, v5 - 1}}
		likePair = append(likePair, p)
		for _, v := range p.pair {
			likePairOtherside[v] = append(likePairOtherside[v], v1-1)
		}
	}
	checkBoard := make([][][]int, n*n)
	emptyBoard := make([][]int, n)
	for i := 0; i < n*n; i++ {
		checkBoard[i] = make([][]int, n)
		for j := 0; j < n; j++ {
			checkBoard[i][j] = make([]int, n)
			emptyBoard[j] = make([]int, n)
			for k := 0; k < n; k++ {
				checkBoard[i][j][k] = 0
				emptyBoard[j][k] = 4
			}
		}
	}
	for i := 0; i < n; i++ {
		emptyBoard[i][0] = 3
		emptyBoard[0][i] = 3
		emptyBoard[n-1][i] = 3
		emptyBoard[i][n-1] = 3
	}
	emptyBoard[0][0], emptyBoard[0][n-1], emptyBoard[n-1][0], emptyBoard[n-1][n-1] = 2, 2, 2, 2

	for _, p := range likePair {
		rc := findMaxEmptySeat(emptyBoard, findMaxSeat(checkBoard[p.v], emptyBoard))
		res = append(res, []int{p.v, rc[0], rc[1]})
		emptyBoard = decreaseEmpty(emptyBoard, rc[0], rc[1])
		checkBoard = increaseLike(checkBoard, likePairOtherside[p.v], rc[0], rc[1], n)
	}
	for _, v := range res {
		if checkBoard[v[0]][v[1]][v[2]] != 0 {
			score += pow(10, (checkBoard[v[0]][v[1]][v[2]] - 1))
		}
	}
	fmt.Println(score)
}

func findMaxSeat(cb [][]int, eb [][]int) [][]int {
	var ret [][]int
	mx := -1
	for i := 0; i < len(eb); i++ {
		for j := 0; j < len(eb); j++ {
			if eb[i][j] >= 0 {
				if cb[i][j] > mx {
					ret = [][]int{{i, j}}
					mx = cb[i][j]
				} else if cb[i][j] == mx {
					ret = append(ret, []int{i, j})
				}
			}
		}
	}
	return ret
}

func findMaxEmptySeat(eb, locs [][]int) [2]int {
	var ret [2]int
	mx := -1
	for _, loc := range locs {
		if eb[loc[0]][loc[1]] > mx {
			ret = [2]int{loc[0], loc[1]}
			mx = eb[loc[0]][loc[1]]
		}
	}
	return ret
}

func decreaseEmpty(eb [][]int, r, c int) [][]int {
	dx, dy := []int{0, 1, 0, -1}, []int{1, 0, -1, 0}
	eb[r][c] = -1
	for i := 0; i < 4; i++ {
		nx, ny := r+dx[i], c+dy[i]
		if nx >= 0 && nx < len(eb) && ny >= 0 && ny < len(eb) {
			eb[nx][ny]--
		}
	}
	return eb
}

func increaseLike(cb [][][]int, pair []int, r, c, n int) [][][]int {
	dx, dy := []int{0, 1, 0, -1}, []int{1, 0, -1, 0}
	for _, j := range pair {
		for i := 0; i < 4; i++ {
			nx, ny := r+dx[i], c+dy[i]
			if nx >= 0 && nx < n && ny >= 0 && ny < n {
				cb[j][nx][ny]++
			}
		}
	}
	return cb
}

func pow(n, m int) int {
	ret := 1
	for i := 0; i < m; i++ {
		ret *= n
	}
	return ret
}
