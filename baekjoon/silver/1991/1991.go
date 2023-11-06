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
	var n int

	defer w.Flush()

	fmt.Fscanf(r, "%d\n", &n)
	nodeMap := make(map[rune]*Node)

	for i := 0; i < n; i++ {
		var parnetNode, leftNode, rightNode rune
		fmt.Fscanf(r, "%c %c %c\n", &parnetNode, &leftNode, &rightNode)

		node, ok := nodeMap[parnetNode]
		if !ok {
			node = NewNode(parnetNode)
			nodeMap[parnetNode] = node
		}

		if leftNode != '.' {
			left, ok := nodeMap[leftNode]
			if !ok {
				left = NewNode(leftNode)
				nodeMap[leftNode] = left
			}
			node.left = left
		}

		if rightNode != '.' {
			right, ok := nodeMap[rightNode]
			if !ok {
				right = NewNode(rightNode)
				nodeMap[rightNode] = right
			}
			node.right = right
		}
	}
	PreOrder(nodeMap['A'])
	fmt.Fprintln(w)
	InOrder(nodeMap['A'])
	fmt.Fprintln(w)
	PostOrder(nodeMap['A'])
	fmt.Fprintln(w)
}

type Node struct {
	c     rune
	left  *Node
	right *Node
}

func NewNode(c rune) *Node {
	return &Node{c: c}
}

func PreOrder(n *Node) {
	fmt.Fprintf(w, "%c", n.c)
	if n.left != nil {
		PreOrder(n.left)
	}
	if n.right != nil {
		PreOrder(n.right)
	}
}

func InOrder(n *Node) {
	if n.left != nil {
		InOrder(n.left)
	}
	fmt.Fprintf(w, "%c", n.c)
	if n.right != nil {
		InOrder(n.right)
	}
}

func PostOrder(n *Node) {
	if n.left != nil {
		PostOrder(n.left)
	}
	if n.right != nil {
		PostOrder(n.right)
	}
	fmt.Fprintf(w, "%c", n.c)
}
