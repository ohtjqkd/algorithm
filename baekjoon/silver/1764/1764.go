package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

var (
	reader *bufio.Reader = bufio.NewReader(os.Stdin)
	writer *bufio.Writer = bufio.NewWriter(os.Stdout)
)

func main() {
	var n, m int
	var hear, see string
	var ans []string

	defer writer.Flush()
	fmt.Fscanf(reader, "%d %d\n", &n, &m)

	tri := NewTri()
	for i := 0; i < n; i++ {
		fmt.Fscanf(reader, "%s\n", &hear)
		tri.insert(hear)
	}
	for i := 0; i < m; i++ {
		fmt.Fscanf(reader, "%s\n", &see)
		if tri.in(see) {
			ans = append(ans, see)
		}
	}
	sort.Slice(ans, func(i, j int) bool {
		return ans[i] < ans[j]
	})
	fmt.Fprintln(writer, len(ans))
	for _, v := range ans {
		fmt.Fprintln(writer, v)
	}
}

type Node struct {
	isEnd bool
	next  map[rune]*Node
}

func NewNode() *Node {
	return &Node{false, make(map[rune]*Node, 26)}
}

type Tri struct {
	root *Node
}

func NewTri() *Tri {
	return &Tri{root: NewNode()}
}

func (t *Tri) insert(s string) {
	node := t.root

	for _, c := range s {
		if node.next[c] == nil {
			node.next[c] = NewNode()
		}
		node = node.next[c]
	}
	node.isEnd = true
}

func (t *Tri) in(s string) bool {
	node := t.root

	for _, c := range s {
		if node.next[c] == nil {
			return false
		}
		node = node.next[c]
	}
	return node.isEnd
}
