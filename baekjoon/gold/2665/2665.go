package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

var (
	reader *bufio.Reader = bufio.NewReader(os.Stdin)
	writer *bufio.Writer = bufio.NewWriter(os.Stdout)
)

func main() {
	defer writer.Flush()
	var r int

	dx := []int{0, 0, 1, -1}
	dy := []int{1, -1, 0, 0}

	fmt.Fscanf(reader, "%d\n", &r)
	board := make([][]int, r)
	dist := make([][]uint64, r)

	for i := range dist {
		dist[i] = make([]uint64, r)
		board[i] = make([]int, r)
		line, _, _ := reader.ReadLine()
		for j := range dist[i] {
			dist[i][j] = math.MaxUint64
			board[i][j] = int(line[j] - '0')
		}
	}

	h := NewHeap()

	h.Push(0, 0, 0)
	for !h.Empty() {
		// for i := 0; i < 10; i++ {
		n := h.Pop()
		if n == nil {
			break
		}
		for i := 0; i < 4; i++ {
			nx, ny := n.x+dx[i], n.y+dy[i]
			if nx < 0 || ny < 0 || nx >= r || ny >= r {
				continue
			}
			if board[nx][ny] == 0 && dist[nx][ny] > n.weight+1 {
				h.Push(n.weight+1, nx, ny)
				dist[nx][ny] = n.weight + 1
			} else if board[nx][ny] == 1 && dist[nx][ny] > n.weight {
				h.Push(n.weight, nx, ny)
				dist[nx][ny] = n.weight
			}
		}
	}
	fmt.Fprintln(writer, dist[r-1][r-1])
}

type Node struct {
	weight uint64
	x, y   int
}

func NewNode(weight uint64, x, y int) *Node {
	return &Node{weight: weight, x: x, y: y}
}

type Heap struct {
	arr  []*Node
	size int
}

func NewHeap() *Heap {
	return &Heap{arr: make([]*Node, 2048), size: 0}
}

func (h *Heap) Push(value uint64, x, y int) {
	h.arr[h.size] = NewNode(value, x, y)
	for i := h.size; i > 0; i /= 2 {
		if h.arr[i].weight < h.arr[i/2].weight {
			h.arr[i], h.arr[i/2] = h.arr[i/2], h.arr[i]
		}
	}
	h.size++
}

func (h *Heap) Pop() *Node {
	if h.size == 0 {
		return nil
	}
	ret := h.arr[0]
	h.size--
	h.arr[0] = h.arr[h.size]
	h.arr[h.size] = nil
	if h.size == 0 {
		return ret
	}
	for i := 0; i*2+1 < h.size; {
		child := i*2 + 1
		if child+1 < h.size && h.arr[child].weight > h.arr[child+1].weight {
			child++
		}
		if h.arr[i].weight < h.arr[child].weight {
			break
		}
		h.arr[i], h.arr[child] = h.arr[child], h.arr[i]
		i = child
	}
	return ret
}

func (h *Heap) Top() *Node {
	if h.size == 0 {
		return nil
	}
	return h.arr[0]
}

func (h *Heap) Empty() bool {
	return h.size == 0
}
