package main

import (
	"bufio"
	"fmt"
	"os"
)

var sc = bufio.NewScanner(os.Stdin)

func main() {
	km := nextIntArr(2)

	arr := nextIntArr(km[0])
	heap := NewHeap()

	for i := 0; i < len(arr); i++ {
		heap.Push(arr[i])
	}
	m := km[1]
	var v int
	for m > 0 {
		v = heap.Pop()
		for heap.size > 0 && heap.arr[0] == v {
			heap.Pop()
		}
		for _, p := range arr {
			if v*p < 2147483647 {
				heap.Push(v * p)
			}
		}
		m--
	}
	fmt.Println(v)
}

func nextIntArr(size int) []int {
	if size == 0 {
		return nil
	}
	sc.Scan()
	ret, val, idx := make([]int, size), 0, 0
	for _, v := range sc.Bytes() {
		if v == ' ' {
			ret[idx] = val
			val = 0
			idx++
		} else if v >= '0' && v <= '9' {
			val = val*10 + int(v-'0')
		} else {
			panic("invalid input")
		}
	}
	ret[idx] = val
	return ret
}

type Heap struct {
	arr  []int
	size int
}

func NewHeap() *Heap {
	return &Heap{}
}

func (h *Heap) Less(i, j int) bool {
	return h.arr[i] < h.arr[j]
}

func (h *Heap) swap(i, j int) {
	if i > h.size || j > h.size {
		panic("invalid index")
	}
	h.arr[i], h.arr[j] = h.arr[j], h.arr[i]
}

func (h *Heap) up(i int) {
	for i > 0 {
		if h.Less(i, (i-1)/2) {
			h.swap((i-1)/2, i)
		}
		i = (i - 1) / 2
	}
}

func (h *Heap) down(i int) {
	for 2*i+1 < h.size {
		child := 2*i + 1
		if child+1 < h.size && h.Less(child+1, child) {
			child++
		}
		if h.Less(i, child) {
			break
		}
		h.swap(i, child)
		i = child
	}
}

func (h *Heap) Push(n int) {
	h.arr = append(h.arr, n)
	h.up(h.size)
	h.size++
}

func (h *Heap) Pop() int {
	if h.size == 0 {
		return -1
	}
	ret := h.arr[0]
	h.arr[0] = h.arr[h.size-1]
	h.arr = h.arr[:h.size-1]
	h.size--
	h.down(0)
	return ret
}
