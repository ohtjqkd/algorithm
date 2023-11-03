// I guess this problem could be solved by binary tree
// Only bin tree get tle
// With AVL Or Red-Black, it could be solved but, I should get some idea How to deal sub node count in rotating.
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

func main() {
	var n, v int

	defer writer.Flush()
	bt := NewBinTree()
	fmt.Fscanf(reader, "%d\n", &n)
	for i := 0; i < n; i++ {
		fmt.Fscanf(reader, "%d\n", &v)
		bt.Push(&Node{v, 0, nil, nil})
		fmt.Fprintln(writer, bt.getNth(i/2))
	}
}

type Node struct {
	v      int
	subCnt int
	left   *Node
	right  *Node
}

type BinTree struct {
	root *Node
	size int
}

func NewBinTree() *BinTree {
	return &BinTree{root: nil}
}

func (b *BinTree) Push(n *Node) {
	var target **Node
	curr := b.root
	if b.root == nil {
		b.root = n
		return
	}
	for {
		curr.subCnt++
		if curr.v < n.v {
			target = &curr.right
		} else {
			target = &curr.left
		}
		if *target == nil {
			*target = n
			break
		}
		curr = *target
	}
}

func (b *BinTree) getNth(n int) int {
	accumleftCnt := 0
	curr := b.root
	for curr != nil {
		currLeftCnt := b.getLeftSubTree(curr)
		if accumleftCnt+currLeftCnt == n {
			break
		}
		if accumleftCnt+currLeftCnt > n {
			curr = curr.left
		} else if curr.right != nil {
			accumleftCnt += (currLeftCnt + 1)
			curr = curr.right
		}
	}
	return curr.v
}

func (b *BinTree) getLeftSubTree(n *Node) int {
	if n != nil && n.left != nil {
		return n.left.subCnt + 1
	}
	return 0
}

// 			1
// -99						5
// 					2				10
// 						5		7
