// input
// 4 2
// 4 2 3 1
// output
// 19

package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	r = bufio.NewReader(os.Stdin)
)

func main() {
	var n, m, tmp int

	fmt.Scan(&n, &m)
	h := NewHeap()

	for i := 0; i < n; i++ {
		fmt.Fscan(r, &tmp)
		h.Push(NewNode(tmp))
	}
	for i := 0; i < m; i++ {
		a := h.Pop()
		b := h.Pop()
		h.Push(NewNode(a.v + b.v))
		h.Push(NewNode(a.v + b.v))
	}
	fmt.Println(h.sum)
}

type Node struct {
	v int
}

func NewNode(v int) *Node {
	return &Node{v: v}
}

func (n *Node) Less(o *Node) bool {
	return n.v < o.v
}

type Heap struct {
	nodes []*Node
	size  int
	sum   int
}

func NewHeap() *Heap {
	return &Heap{}
}

func (h *Heap) swap(a, b int) {
	if a > h.size || b > h.size {
		return
	}
	h.nodes[a], h.nodes[b] = h.nodes[b], h.nodes[a]
}

func (h *Heap) up(i int) {
	curr := i
	for curr > 0 {
		parent := (curr - 1) / 2
		if h.nodes[curr].v < h.nodes[parent].v {
			h.swap(curr, parent)
			curr = parent
		} else {
			break
		}
	}
}

func (h *Heap) down(i int) {
	for 2*i+1 < h.size {
		child := 2*i + 1
		if child+1 < h.size && h.nodes[child+1].Less(h.nodes[child]) {
			child++
		}
		if h.nodes[i].Less(h.nodes[child]) {
			break
		}
		h.swap(i, child)
		i = child
	}
}

func (h *Heap) Push(n *Node) {
	h.nodes = append(h.nodes, n)
	h.size++
	h.up(h.size - 1)
	h.sum += n.v
}

func (h *Heap) Pop() *Node {
	ret := h.nodes[0]
	h.nodes[0] = h.nodes[h.size-1]
	h.nodes = h.nodes[:h.size-1]
	h.size--
	h.down(0)
	h.sum -= ret.v
	return ret
}
