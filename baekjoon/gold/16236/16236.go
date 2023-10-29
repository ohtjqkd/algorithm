package main

import (
	"container/heap"
	"fmt"
)

type BfsReturn struct {
	x    int
	y    int
	time int
}

type Candidate struct {
	x int
	y int
}

type CandidateHeap []Candidate

func (h CandidateHeap) Len() int { return len(h) }
func (h CandidateHeap) Less(i, j int) bool {
	if h[i].x < h[j].x {
		return true
	} else if h[i].x == h[j].x && h[i].y < h[j].y {
		return true
	} else {
		return false
	}
}
func (h CandidateHeap) Swap(i, j int) { h[i], h[j] = h[j], h[i] }
func (h *CandidateHeap) Push(element interface{}) {
	*h = append(*h, element.(Candidate))
}
func (h *CandidateHeap) Pop() interface{} {
	old := *h
	n := len(old)
	element := old[n-1]
	*h = old[0 : n-1]
	return element
}

func main() {
	var result int = 0
	var size int = 2
	var grownCnt int = size
	var N int
	var board [][]int
	var x, y int

	fmt.Scan(&N)
	for i := 0; i < N; i++ {
		var row []int
		for j := 0; j < N; j++ {
			var tmp int
			fmt.Scan(&tmp)
			if tmp == 9 {
				x, y = i, j
				tmp = 0
			}
			row = append(row, tmp)
		}
		board = append(board, row)
	}

	for {
		ret := bfs(&board, size, x, y, N)
		if ret.x != -1 {
			result += ret.time
			grownCnt--
			if grownCnt == 0 {
				size++
				grownCnt = size
			}
			board[ret.x][ret.y] = 0
			x, y = ret.x, ret.y
			continue
		}
		fmt.Println(result)
		break
	}
}

func bfs(board *[][]int, size, x, y, N int) BfsReturn {
	var dx, dy = []int{-1, 0, 1, 0}, []int{0, -1, 0, 1}
	var visited [20][20]bool
	var queue [][][2]int
	var depth [][2]int
	var time int = 0

	depth = append(depth, [2]int{x, y})
	queue = append(queue, depth)
	cand := &CandidateHeap{}
	heap.Init(cand)
	for len(queue) > 0 {
		currDepth := queue[0]
		var nextDepth [][2]int
		queue = queue[1:]
		for len(currDepth) > 0 {
			xy := currDepth[0]
			currDepth = currDepth[1:]
			var x, y = xy[0], xy[1]
			for i := 0; i < 4; i++ {
				var nx, ny = x + dx[i], y + dy[i]
				if nx < 0 || nx >= N || ny < 0 || ny >= N {
					continue
				}
				if visited[nx][ny] {
					continue
				}
				if (*board)[nx][ny] > size {
					continue
				}
				if (*board)[nx][ny] < size && (*board)[nx][ny] != 0 {
					heap.Push(cand, Candidate{nx, ny})
				}
				visited[nx][ny] = true
				nextDepth = append(nextDepth, [2]int{nx, ny})
			}
		}
		if cand.Len() > 0 {
			loc := heap.Pop(cand).(Candidate)
			return BfsReturn{loc.x, loc.y, time + 1}
		}
		if len(nextDepth) > 0 {
			queue = append(queue, nextDepth)
		}
		time++
	}
	return BfsReturn{-1, -1, -1}
}
