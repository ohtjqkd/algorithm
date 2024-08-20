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
	N      int
	gears  []*Deque
	deque  []*Deque
)

func main() {
	defer writer.Flush()
	answer := 0

	gears = make([]*Deque, 4)
	for i := 0; i < 4; i++ {
		line, _, _ := reader.ReadLine()
		gears[i] = NewDeque()
		for _, c := range line {
			gears[i].PushBack(c)
		}
	}

	fmt.Fscanf(reader, "%d\n", &N)

	for i := 0; i < N; i++ {
		var start, dir int
		fmt.Fscanf(reader, "%d %d\n", &start, &dir)
		start--
		cmd := [][]int{{start, dir}}
		tmpDir := dir
		for j := start - 1; j > -1; j-- {
			if gears[j].GetFromFront(2) == gears[j+1].GetFromBack(1) {
				break
			}
			tmpDir = -tmpDir
			cmd = append(cmd, []int{j, tmpDir})
		}
		tmpDir = dir
		for j := start + 1; j < 4; j++ {
			if gears[j-1].GetFromFront(2) == gears[j].GetFromBack(1) {
				break
			}
			tmpDir = -tmpDir
			cmd = append(cmd, []int{j, tmpDir})
		}

		for _, c := range cmd {
			rotate(gears[c[0]], c[1])
		}
	}

	for i, g := range gears {
		if g.GetFromFront(0) == '1' {
			answer += int(math.Pow(2, float64(i)))
		}
	}
	fmt.Fprintln(writer, answer)
}

func rotate(gear *Deque, dir int) {
	if dir == -1 {
		gear.PushBack(gear.PopFront())
	} else {
		gear.PushFront(gear.PopBack())
	}
}

type Node struct {
	value byte
	next  *Node
	prev  *Node
}

func NewNode(value byte) *Node {
	return &Node{value: value}
}

type Deque struct {
	head *Node
	tail *Node
	size int
}

func NewDeque() *Deque {
	return &Deque{}
}

func (d *Deque) PushFront(value byte) {
	node := NewNode(value)
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

func (d *Deque) PushBack(value byte) {
	node := NewNode(value)
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

func (d *Deque) PopFront() byte {
	if d.size == 0 {
		return 0
	}
	value := d.head.value
	d.head = d.head.next
	if d.head != nil {
		d.head.prev = nil
	}
	d.size--
	return value
}

func (d *Deque) PopBack() byte {
	if d.size == 0 {
		return 0
	}
	value := d.tail.value
	d.tail = d.tail.prev
	if d.tail != nil {
		d.tail.next = nil
	}
	d.size--
	return value
}

func (d *Deque) GetFromFront(idx int) byte {
	if d.size == 0 {
		return 0
	}
	node := d.head
	for i := 0; i < idx; i++ {
		node = node.next
	}
	return node.value
}

func (d *Deque) GetFromBack(idx int) byte {
	if d.size == 0 {
		return 0
	}
	node := d.tail
	for i := 0; i < idx; i++ {
		node = node.prev
	}
	return node.value
}
