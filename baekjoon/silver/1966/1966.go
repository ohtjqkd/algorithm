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

func main() {
	defer w.Flush()

	var t, n, m, v int

	fmt.Fscanf(r, "%d\n", &t)

	for i := 0; i < t; i++ {
		fmt.Fscan(r, &n, &m)
		heap := NewHeap()
		deq := NewDeq()
		for j := 0; j < n; j++ {
			fmt.Fscan(r, &v)
			heap.Push(NewNode(v, j))
			deq.PushBack(NewNode(v, j))
		}
		cnt := 1
		for heap.size > 0 && deq.size > 0 {
			if heap.Top().val == deq.Front().val {
				if deq.Front().order == m {
					fmt.Fprintln(w, cnt)
					break
				} else {
					deq.PopFront()
					heap.Pop()
					cnt++
				}
			} else {
				deq.PushBack(deq.PopFront())
			}
		}
	}
}

type Node struct {
	val   int
	order int
}

func NewNode(val, order int) *Node {
	return &Node{val: val, order: order}
}

func (n *Node) Less(o *Node) bool {
	if n.val < o.val {
		return true
	}
	if n.val == o.val && n.order < o.order {
		return true
	}
	return false
}

func (n *Node) Greater(o *Node) bool {
	if n.val > o.val {
		return true
	}
	if n.val == o.val && n.order < o.order {
		return true
	}
	return false
}

type Heap struct {
	arr  []*Node
	size int
}

func NewHeap() *Heap {
	return &Heap{}
}

func (h *Heap) swap(i, j int) {
	h.arr[i], h.arr[j] = h.arr[j], h.arr[i]
}

func (h *Heap) up(i int) {
	for i > 0 {
		if h.arr[i].Greater(h.arr[(i-1)/2]) {
			h.swap((i-1)/2, i)
		}
		i = (i - 1) / 2
	}
}

func (h *Heap) down(i int) {
	for 2*i+1 < h.size {
		child := 2*i + 1
		if child+1 < h.size && h.arr[child].Less(h.arr[child+1]) {
			child++
		}
		if h.arr[i].Greater(h.arr[child]) {
			break
		}
		h.swap(i, child)
		i = child
	}
}

func (h *Heap) Top() *Node {
	if h.size == 0 {
		return nil
	}
	return h.arr[0]
}

func (h *Heap) Push(n *Node) {
	h.arr = append(h.arr, n)
	h.up(h.size)
	h.size++
}

func (h *Heap) Pop() *Node {
	if h.size == 0 {
		return nil
	}
	n := h.arr[0]
	h.arr[0] = h.arr[h.size-1]
	h.arr[h.size-1] = nil
	h.size--
	h.down(0)
	return n
}

type Deq struct {
	arr  []*Node
	size int
}

func NewDeq() *Deq {
	return &Deq{}
}

func (d *Deq) PushFront(n *Node) {
	d.arr = append([]*Node{n}, d.arr...)
	d.size++
}

func (d *Deq) PushBack(n *Node) {
	d.arr = append(d.arr, n)
	d.size++
}

func (d *Deq) PopFront() *Node {
	if d.size == 0 {
		return nil
	}
	n := d.arr[0]
	d.arr[0] = nil
	d.arr = d.arr[1:]
	d.size--
	return n
}

func (d *Deq) PopBack() *Node {
	if d.size == 0 {
		return nil
	}
	n := d.arr[d.size-1]
	d.arr[d.size-1] = nil
	d.arr = d.arr[:d.size-1]
	d.size--
	return n
}

func (d *Deq) Front() *Node {
	if d.size == 0 {
		return nil
	}
	return d.arr[0]
}

func (d *Deq) Back() *Node {
	if d.size == 0 {
		return nil
	}
	return d.arr[d.size-1]
}
