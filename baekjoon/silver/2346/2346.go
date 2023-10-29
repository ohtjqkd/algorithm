package main

import (
	"fmt"
	"strconv"
	"strings"
)

type Deque struct {
	head *Node
	tail *Node
	size int
}

type Node struct {
	value int
	idx   string
	prev  *Node
	next  *Node
}

func NewDeque() *Deque {
	return &Deque{head: nil, tail: nil, size: 0}
}

func (d *Deque) PushFront(node *Node) {
	if d.size == 0 {
		d.head = node
		d.tail = node
	} else {
		node.next = d.head
		d.head.prev = node
		d.head = node
	}
	d.size++
}

func (d *Deque) PushBack(node *Node) {
	if d.size == 0 {
		d.head = node
		d.tail = node
	} else {
		node.prev = d.tail
		d.tail.next = node
		d.tail = node
	}
	d.size++
}

func (d *Deque) PopFront() (*Node, int) {
	if d.size == 0 {
		return nil, -1
	}
	node := d.head
	d.head = d.head.next
	if d.head != nil {
		d.head.prev = nil
	} else {
		d.tail = nil
	}
	d.size--
	return node, node.value
}

func (d *Deque) PopBack() (*Node, int) {
	if d.size == 0 {
		return nil, -1
	}
	node := d.tail
	d.tail = d.tail.prev
	if d.tail != nil {
		d.tail.next = nil
	} else {
		d.head = nil
	}
	d.size--
	return node, node.value
}

func (d *Deque) Print() {
	node := d.head
	for node != nil {
		fmt.Print(node.value, " ")
		node = node.next
	}
	fmt.Println()
}

func main() {
	var n int
	var x int
	var ans []string

	fmt.Scan(&n)
	deque := NewDeque()
	for i := 1; i <= n; i++ {
		fmt.Scan(&x)
		deque.PushBack(&Node{value: x, idx: strconv.Itoa(i)})
	}

	target, _ := deque.PopFront()
	ans = append(ans, target.idx)
	cnt := target.value
	for deque.size > 0 {
		if cnt < 0 {
			cnt = -cnt
			for ; cnt > 1; cnt-- {
				node, _ := deque.PopBack()
				if node != nil {
					deque.PushFront(node)
				}
			}
			target, _ = deque.PopBack()
			cnt = target.value
			ans = append(ans, target.idx)
		} else {
			for ; cnt > 1; cnt-- {
				node, _ := deque.PopFront()
				if node != nil {
					deque.PushBack(node)
				}
			}
			target, _ = deque.PopFront()
			cnt = target.value
			ans = append(ans, target.idx)
		}
	}
	fmt.Println(strings.Join(ans, " "))
}
