package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	reader *bufio.Reader = bufio.NewReaderSize(os.Stdin, 1024*1024)
	writer *bufio.Writer = bufio.NewWriterSize(os.Stdout, 1024*1024)
)

func main() {
	var v, e int
	var n1, n2, w int
	var node *Node

	defer writer.Flush()

	fmt.Fscanf(reader, "%d %d\n", &v, &e)
	ans := 0
	parent := make(map[int]int)
	rank := make(map[int]int)
	heap := NewHeap()

	for i := 0; i < e; i++ {
		fmt.Fscanf(reader, "%d %d %d\n", &n1, &n2, &w)
		parent[n1], parent[n2] = n1, n2
		rank[n1], rank[n2] = 0, 0
		heap.Push(&Node{w: w, a: n1, b: n2})
	}
	for heap.Size() > 0 {
		node = heap.Pop()
		if find((*node).a, &parent) != find((*node).b, &parent) {
			ans += node.w
			union(node.a, node.b, &parent, &rank)
		}
	}
	fmt.Fprintln(writer, ans)
}

func find(i int, p *map[int]int) int {
	if (*p)[i] != i {
		(*p)[i] = find((*p)[i], p)
	}
	return (*p)[i]
}

func union(a, b int, p *map[int]int, r *map[int]int) {
	r1 := find(a, p)
	r2 := find(b, p)

	if (*r)[r1] > (*r)[r2] {
		(*p)[r2] = r1
	} else {
		(*p)[r1] = r2
		if (*r)[r1] == (*r)[r2] {
			(*r)[r2]++
		}
	}
}

type Node struct {
	w, a, b int
}

func (n *Node) Less(node *Node) bool {
	return n.w < node.w
}

type Heap struct {
	nodes []*Node
	size  int
}

func NewHeap() *Heap {
	return &Heap{}
}

func (h *Heap) Push(node *Node) {
	h.nodes = append(h.nodes, node)
	h.size++
	h.up(h.size - 1)
}

func (h *Heap) Pop() *Node {
	if h.size == 0 {
		return nil
	}
	ret := h.nodes[0]
	h.nodes[0] = h.nodes[h.size-1]
	h.nodes = h.nodes[:h.size-1]
	h.size--
	h.down(0)
	return ret
}

func (h *Heap) up(idx int) {
	currIdx := idx
	parentIdx := (idx - 1) / 2
	for currIdx > 0 && h.nodes[currIdx].Less(h.nodes[parentIdx]) {
		h.nodes[currIdx], h.nodes[parentIdx] = h.nodes[parentIdx], h.nodes[currIdx]
		currIdx = parentIdx
		parentIdx = (currIdx - 1) / 2
	}
}

func (h *Heap) down(idx int) {
	currIdx := idx
	leftIdx := currIdx*2 + 1
	rightIdx := currIdx*2 + 2
	for leftIdx < h.size {
		next := leftIdx
		if rightIdx < h.size && h.nodes[rightIdx].Less(h.nodes[leftIdx]) {
			next = rightIdx
		}
		if h.nodes[next].Less(h.nodes[currIdx]) {
			h.nodes[next], h.nodes[currIdx] = h.nodes[currIdx], h.nodes[next]
			currIdx = next
			leftIdx = currIdx*2 + 1
			rightIdx = currIdx*2 + 2
		} else {
			break
		}
	}
}

func (h *Heap) Size() int {
	return h.size
}
