// package main

// import (
// 	"bufio"
// 	"os"
// 	"strconv"
// 	"strings"
// )

// type Collections interface {
// 	AppendLeft(int)
// 	Append(int)
// 	PopLeft() int
// 	Pop() int
// 	Size() int
// 	IsEmpty() bool
// 	Head() int
// 	Tail() int
// }

// type Deque struct {
// 	head   *Node
// 	tail   *Node
// 	size   int
// 	method Collections
// }

// type Node struct {
// 	value int
// 	prev  *Node
// 	next  *Node
// }

// func (d *Deque) IsEmpty() bool {
// 	return d.size == 0
// }

// func (d *Deque) AppendLeft(value int) {
// 	node := &Node{value: value}
// 	if d.IsEmpty() {
// 		d.head = node
// 		d.tail = node
// 	} else {
// 		node.next = d.head
// 		d.head.prev = node
// 		d.head = node
// 	}
// 	d.size++
// }

// func (d *Deque) Append(value int) {
// 	node := &Node{value: value}
// 	if d.IsEmpty() {
// 		d.head = node
// 		d.tail = node
// 	} else {
// 		node.prev = d.tail
// 		d.tail.next = node
// 		d.tail = node
// 	}
// 	d.size++
// }

// func (d *Deque) PopLeft() int {
// 	if d.IsEmpty() {
// 		return -1
// 	}
// 	value := d.head.value
// 	if d.size == 1 {
// 		d.head = nil
// 		d.tail = nil
// 		d.size--
// 		return value
// 	}
// 	d.head = d.head.next
// 	d.head.prev = nil
// 	d.size--
// 	return value
// }

// func (d *Deque) Pop() int {
// 	if d.IsEmpty() {
// 		return -1
// 	}
// 	value := d.tail.value
// 	if d.size == 1 {
// 		d.head = nil
// 		d.tail = nil
// 		d.size--
// 		return value
// 	}
// 	d.tail = d.tail.prev
// 	d.tail.next = nil
// 	d.size--
// 	return value
// }

// func (d *Deque) Size() int {
// 	return d.size
// }

// func (d *Deque) Head() int {
// 	if d.IsEmpty() {
// 		return -1
// 	}
// 	return d.head.value
// }

// func (d *Deque) Tail() int {
// 	if d.IsEmpty() {
// 		return -1
// 	}
// 	return d.tail.value
// }

// func main() {
// 	d := &Deque{}

// 	scanner := bufio.NewScanner(os.Stdin)
// 	writer := bufio.NewWriter(os.Stdout)

// 	scanner.Scan()
// 	n, _ := strconv.Atoi(scanner.Text())
// 	for i := 0; i < int(n); i++ {
// 		scanner.Scan()
// 		cmd := strings.Split(scanner.Text(), " ")
// 		c, _ := strconv.Atoi(cmd[0])
// 		switch c {
// 		case 1:
// 			v, _ := strconv.Atoi(cmd[1])
// 			d.AppendLeft(v)
// 		case 2:
// 			v, _ := strconv.Atoi(cmd[1])
// 			d.Append(v)
// 		case 3:
// 			writer.WriteString(strconv.Itoa(d.PopLeft()) + "\n")
// 		case 4:
// 			writer.WriteString(strconv.Itoa(d.Pop()) + "\n")
// 		case 5:
// 			writer.WriteString(strconv.Itoa(d.Size()) + "\n")
// 		case 6:
// 			if d.IsEmpty() {
// 				writer.WriteString("1\n")
// 			} else {
// 				writer.WriteString("0\n")
// 			}
// 		case 7:
// 			writer.WriteString(strconv.Itoa(d.Head()) + "\n")
// 		case 8:
// 			writer.WriteString(strconv.Itoa(d.Tail()) + "\n")
// 		}
// 		writer.Flush()
// 	}
// }

package main

import (
	"bufio"
	"fmt"
	"os"
)

type Deque struct {
	data [1000000]int
	head int
	tail int
	size int
}

func (d *Deque) NewDeque() *Deque {
	return &Deque{
		data: [1000000]int{},
		head: 0,
		tail: 0,
		size: 0,
	}
}

func (d *Deque) IsEmpty() bool {
	return d.size == 0
}

func (d *Deque) AppendLeft(value int) {
	d.head = (d.head - 1 + len(d.data)) % len(d.data)
	d.data[d.head] = value
	d.size++
}

func (d *Deque) Append(value int) {
	d.data[d.tail] = value
	d.tail = (d.tail + 1) % len(d.data)
	d.size++
}

func (d *Deque) PopLeft() int {
	if d.IsEmpty() {
		return -1
	}
	value := d.data[d.head]
	d.head = (d.head + 1) % len(d.data)
	d.size--
	return value
}

func (d *Deque) Pop() int {
	if d.IsEmpty() {
		return -1
	}
	value := d.data[(d.tail-1+len(d.data))%len(d.data)]
	d.tail = (d.tail - 1 + len(d.data)) % len(d.data)
	d.size--
	return value
}

func (d *Deque) Head() int {
	if d.IsEmpty() {
		return -1
	}
	return d.data[d.head]
}

func (d *Deque) Tail() int {
	if d.IsEmpty() {
		return -1
	}
	return d.data[(d.tail-1+len(d.data))%len(d.data)]
}

func (d *Deque) Size() int {
	return d.size
}

func parseInt(s []byte) [2]int {
	var ret [2]int
	idx := 0
	n := 0

	for _, v := range s {
		if v == ' ' {
			ret[idx] = n
			idx++
			n = 0
			continue
		}
		n = n*10 + int(v-'0')
	}
	ret[idx] = n
	return ret
}

func main() {
	d := &Deque{}
	d = d.NewDeque()

	reader := bufio.NewReaderSize(os.Stdin, 1000)
	writer := bufio.NewWriter(os.Stdout)

	defer writer.Flush()

	line, _, _ := reader.ReadLine()
	n := parseInt(line)[0]
	for i := 0; i < n; i++ {
		line, _, _ := reader.ReadLine()
		cmd := parseInt(line)
		switch cmd[0] {
		case 1:
			d.AppendLeft(cmd[1])
		case 2:
			d.Append(cmd[1])
		case 3:
			fmt.Fprintln(writer, d.PopLeft())
		case 4:
			fmt.Fprintln(writer, d.Pop())
		case 5:
			fmt.Fprintln(writer, d.Size())
		case 6:
			if d.IsEmpty() {
				fmt.Fprintln(writer, 1)
			} else {
				fmt.Fprintln(writer, 0)
			}
		case 7:
			fmt.Fprintln(writer, d.Head())
		case 8:
			fmt.Fprintln(writer, d.Tail())
		}
	}
}
