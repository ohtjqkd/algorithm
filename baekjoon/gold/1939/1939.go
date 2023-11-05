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
	var n, m, s, e, c, sl, el int

	defer w.Flush()

	fmt.Fscanf(r, "%d %d\n", &n, &m)

	bridgeMap := make(map[int][]Edge, m)
	cap := make([]int, n+1)
	for i := 0; i < m; i++ {
		fmt.Fscanf(r, "%d %d %d\n", &s, &e, &c)
		bridgeMap[s] = append(bridgeMap[s], Edge{e, c})
		bridgeMap[e] = append(bridgeMap[e], Edge{s, c})
	}

	fmt.Fscanf(r, "%d %d\n", &sl, &el)
	cap[sl] = math.MaxInt64

	heap := NewMaxHeap()
	heap.Push(NewNode(sl, math.MaxInt64))

	for heap.size > 0 {
		node := heap.Pop()
		if node.start == el {
			fmt.Fprintln(w, cap[el])
			break
		}
		for _, e := range bridgeMap[node.start] {
			if cap[e.end] < min(node.accumWeight, e.weight) {
				cap[e.end] = min(node.accumWeight, e.weight)
				heap.Push(NewNode(e.end, cap[e.end]))
			}
		}
	}
}

type Edge struct {
	end    int
	weight int
}

type Node struct {
	start       int
	accumWeight int
}

func NewNode(start, weight int) *Node {
	return &Node{start, weight}
}

func (n *Node) Greater(a *Node) bool {
	if n.accumWeight > a.accumWeight {
		return true
	}
	return false
}

type MaxHeap struct {
	nodes []*Node
	size  int
}

func NewMaxHeap() *MaxHeap {
	return &MaxHeap{}
}

func (h *MaxHeap) swap(a, b int) {
	if a < 0 || a >= h.size || b < 0 || b >= h.size {
		return
	}
	h.nodes[a], h.nodes[b] = h.nodes[b], h.nodes[a]
}

func (h *MaxHeap) up(curr int) {
	var par int
	for {
		par = (curr - 1) / 2
		if curr == 0 || !h.nodes[curr].Greater(h.nodes[par]) {
			break
		}
		h.swap(curr, par)
		curr = par
	}
}

func (h *MaxHeap) down(curr int) {
	var left, right, nxt int
	for {
		left = curr*2 + 1
		right = curr*2 + 2
		nxt = left
		if left >= h.size {
			break
		}
		if right < h.size && h.nodes[right].Greater(h.nodes[left]) {
			nxt = right
		}
		if h.nodes[curr].Greater(h.nodes[nxt]) {
			break
		}
		h.swap(curr, nxt)
		curr = nxt
	}
}

func (h *MaxHeap) Push(n *Node) {
	h.nodes = append(h.nodes, n)
	h.size++
	h.up(h.size - 1)
}

func (h *MaxHeap) Pop() *Node {
	if h.size == 0 {
		return nil
	}
	ret := h.nodes[0]
	h.swap(0, h.size-1)
	h.nodes = h.nodes[:h.size-1]
	h.size--
	h.down(0)
	return ret
}
