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
	var n, m int
	var dx, dy = [4]int{0, 0, 1, -1}, [4]int{1, -1, 0, 0}
	var maze []string
	var dist [][]uint
	defer writer.Flush()

	fmt.Fscanf(reader, "%d %d\n", &m, &n)
	maze = make([]string, n)
	dist = make([][]uint, n)
	for i := 0; i < n; i++ {
		dist[i] = make([]uint, m)
		for j := 0; j < m; j++ {
			dist[i][j] = math.MaxUint
		}
	}
	dist[0][0] = 0
	for i := 0; i < n; i++ {
		fmt.Fscanf(reader, "%s\n", &maze[i])
	}
	heap := NewHeap()
	heap.Insert(Node{0, 0, 0})
	for heap.Size() > 0 {
		node := heap.Pop()
		for i := 0; i < 4; i++ {
			xx := node.x + dx[i]
			yy := node.y + dy[i]
			// if xx == n-1 && yy == m-1 {
			// 	fmt.Fprintln(writer, node.w)
			// 	return
			// }
			if xx < 0 || xx >= n || yy < 0 || yy >= m {
				continue
			} else if dist[xx][yy] > node.w+uint(maze[xx][yy]-'0') {
				dist[xx][yy] = node.w + uint(maze[xx][yy]-'0')
				heap.Insert(Node{node.w + uint(maze[xx][yy]-'0'), xx, yy})
			}
		}
	}
	fmt.Fprintln(writer, dist[n-1][m-1])
}

type Node struct {
	w uint
	x int
	y int
}

type Heap struct {
	heap []Node
}

func (n *Node) Less(b Node) bool {
	if n.w < b.w {
		return true
	}
	return false
}

func NewHeap() *Heap {
	return &Heap{}
}

func (h *Heap) Insert(val Node) {
	h.heap = append(h.heap, val)
	child := len(h.heap) - 1
	parent := (child - 1) / 2
	for h.heap[child].Less(h.heap[parent]) {
		h.heap[parent], h.heap[child] = h.heap[child], h.heap[parent]
		child = parent
		parent = (child - 1) / 2
	}
}

func (h *Heap) Pop() Node {
	ret := h.heap[0]

	h.heap[0] = h.heap[len(h.heap)-1]

	h.heap = h.heap[:len(h.heap)-1]
	curr := 0
	for {
		left := curr*2 + 1
		right := curr*2 + 2
		if left >= len(h.heap) {
			break
		}
		next := left
		if right < len(h.heap) && h.heap[right].Less(h.heap[left]) {
			next = right
		}
		if h.heap[curr].Less(h.heap[next]) {
			break
		}
		h.heap[curr], h.heap[next] = h.heap[next], h.heap[curr]
		curr = next
	}
	return ret
}

func (h *Heap) Size() int {
	return len(h.heap)
}
