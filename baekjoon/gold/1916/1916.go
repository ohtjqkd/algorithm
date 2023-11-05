package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

var (
	r *bufio.Reader = bufio.NewReader(os.Stdin)
	w *bufio.Writer = bufio.NewWriter(os.Stdout)
)

func main() {
	var n, m, s, e, weight, start, end int
	var node *Node

	defer w.Flush()

	fmt.Fscanf(r, "%d\n", &n)
	fmt.Fscanf(r, "%d\n", &m)

	cityMap := make(map[int][][]int, n+1)
	fee := make([]int, n+1)
	for i := 1; i < n+1; i++ {
		fee[i] = math.MaxInt64
	}
	for i := 0; i < m; i++ {
		fmt.Fscanf(r, "%d %d %d\n", &s, &e, &weight)
		cityMap[s] = append(cityMap[s], []int{e, weight})
	}

	fmt.Fscanf(r, "%d %d\n", &start, &end)
	heap := NewHeap()

	fee[start] = 0
	heap.Push(&Node{fee: fee[start], start: start})

	for heap.Size() > 0 {
		node = heap.Pop()
		if fee[node.start] < node.fee {
			continue
		}
		for _, b := range cityMap[node.start] {
			ne, nw := b[0], b[1]
			nw += node.fee
			if fee[ne] > nw {
				fee[ne] = nw
				heap.Push(&Node{fee: nw, start: ne})
			}
		}
	}
	fmt.Fprintln(w, fee[end])
}

type Node struct {
	fee   int
	start int
}

func NewNode() *Node {
	return &Node{}
}

func (n *Node) Less(a *Node) bool {
	return n.fee < a.fee
}

type Heap struct {
	nodes []*Node
	size  int
}

func NewHeap() *Heap {
	return &Heap{}
}

func (h *Heap) Size() int {
	return h.size
}

func (h *Heap) swap(a, b int) {
	h.nodes[a], h.nodes[b] = h.nodes[b], h.nodes[a]
}

func (h *Heap) up(a int) {
	curr := a
	par := (curr - 1) / 2
	for curr != 0 && h.nodes[curr].Less(h.nodes[par]) {
		h.swap(curr, par)
		curr = par
		par = (curr - 1) / 2
	}
}

func (h *Heap) down() {
	var curr, left, right, nxt int
	curr = 0
	for left < h.size {
		left = curr*2 + 1
		right = curr*2 + 2
		nxt = left
		if left >= h.size {
			break
		}
		if right < h.size && h.nodes[right].Less(h.nodes[left]) {
			nxt = right
		}
		if !h.nodes[nxt].Less(h.nodes[curr]) {
			break
		}
		h.swap(curr, nxt)
		curr = nxt
	}
}

func (h *Heap) Push(n *Node) {
	h.nodes = append(h.nodes, n)
	h.size++
	h.up(len(h.nodes) - 1)
}

func (h *Heap) Pop() *Node {
	if h.size == 0 {
		return nil
	}
	ret := h.nodes[0]
	h.swap(0, len(h.nodes)-1)
	h.nodes = h.nodes[:h.size-1]
	h.size--
	h.down()
	return ret
}
