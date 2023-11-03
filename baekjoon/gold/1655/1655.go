// I guess this problem could be solved by binary tree

package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	reader *bufio.Reader = bufio.NewReader(os.Stdin)
	writer *bufio.Writer = bufio.NewWriter(os.Stdout)
)

// Heap
func main() {
	var n, v int

	defer writer.Flush()
	fmt.Fscanf(reader, "%d\n", &n)
	mxHeap := NewHeap()
	mnHeap := NewHeap()
	for i := 0; i < n; i++ {
		fmt.Fscanf(reader, "%d\n", &v)
		if mxHeap.Size() == 0 {
			mxHeap.Push(&Node{-v})
			fmt.Fprintln(writer, v)
			continue
		}
		if mxHeap.Size() == mnHeap.Size() {
			mxHeap.Push(&Node{-v})
		} else if mxHeap.Size()-mnHeap.Size() == 1 {
			mnHeap.Push(&Node{v})
		}
		if -mxHeap.Top() > mnHeap.Top() {
			xv := mxHeap.Pop()
			nv := mnHeap.Pop()
			mnHeap.Push(&Node{-xv.v})
			mxHeap.Push(&Node{-nv.v})
		}
		fmt.Fprintln(writer, -mxHeap.Top())
	}
}

type Node struct {
	v int
}

func (n *Node) Less(node *Node) bool {
	return n.v < node.v
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

func (h *Heap) Top() int {
	if h.Size() == 0 {
		return -1
	}
	return h.nodes[0].v
}
