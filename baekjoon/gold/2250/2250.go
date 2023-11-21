package main

import (
	"bufio"
	"fmt"
	"os"
)

var sc = bufio.NewScanner(os.Stdin)
var nodeMap map[int]*Node
var cntlr [10001][2]int

func main() {
	var arr []int

	n := nextInt()
	btree := &Btree{nodeMap: make(map[int]*Node)}
	for i := 0; i < n; i++ {
		arr = nextIntArr(3)
		btree.insert(arr[0], arr[1], arr[2])
	}

	btree.setRoot()
	btree.setLevel(btree.root)
	btree.setCountSubtree(btree.root)
	count(btree.root)
	solve(btree.root)
	max := 0
	ans := 0
	for i := 1; i <= 10000; i++ {
		if max < cntlr[i][1]+cntlr[i][0]-n+2 {
			max = cntlr[i][1] + cntlr[i][0] - n + 2
			ans = i
		}
	}
	fmt.Println(ans, max)
}

func solve(n *Node) {
	if cntlr[n.level][0] < n.leftCnt {
		cntlr[n.level][0] = n.leftCnt
	}
	if cntlr[n.level][1] < n.rightCnt {
		cntlr[n.level][1] = n.rightCnt
	}
	if n.left != nil {
		solve(n.left)
	}
	if n.right != nil {
		solve(n.right)
	}
}

func count(n *Node) {
	if n == nil {
		return
	}
	if n.parent != nil && n.parent.left == n {
		n.leftCnt = n.parent.leftCnt - n.rightSub - 1
		n.rightCnt = n.parent.rightCnt + n.rightSub + 1
	}
	if n.parent != nil && n.parent.right == n {
		n.leftCnt = n.parent.leftCnt + n.leftSub + 1
		n.rightCnt = n.parent.rightCnt - n.leftSub - 1
	}
	if n.parent == nil {
		n.leftCnt = n.leftSub
		n.rightCnt = n.rightSub
	}
	count(n.left)
	count(n.right)
}

func countSubtree(n *Node) {
	leftCnt(n)
	rightCnt(n)
}

func leftCnt(n *Node) {
	fmt.Println(n.level)
	cntlr[n.level][0] = n.leftSub
	if n.left != nil {
		leftCnt(n.left)
	} else if n.right != nil {
		leftCnt(n.right)
	}
}

func rightCnt(n *Node) {
	cntlr[n.level][1] = n.rightSub
	if n.right != nil {
		rightCnt(n.right)
	} else if n.left != nil {
		rightCnt(n.left)
	}
}

func nextInt() int {
	ret := 0
	sc.Scan()
	for _, v := range sc.Bytes() {
		ret = ret*10 + int(v-'0')
	}
	return ret
}

func nextIntArr(size int) []int {
	if size == 0 {
		return nil
	}
	sc.Scan()
	ret := make([]int, size)
	idx := 0
	i := 0
	sign := 1
	for _, v := range sc.Bytes() {
		if v == ' ' {
			ret[idx] = i * sign
			i = 0
			sign = 1
			idx++
		} else if v >= '0' && v <= '9' {
			i = i*10 + int(v-'0')
		} else if v == '-' {
			sign *= -1
		}
	}
	ret[idx] = i * sign
	return ret
}

type Node struct {
	value             int
	level             int
	left, right       *Node
	parent            *Node
	leftSub, rightSub int
	leftCnt, rightCnt int
}

type Btree struct {
	root    *Node
	nodeMap map[int]*Node
}

func (b *Btree) insert(value, left, right int) {
	node, ok := b.nodeMap[value]
	if !ok {
		node = &Node{value: value}
		b.nodeMap[value] = node
	}
	if left != -1 {
		leftNode, ok := b.nodeMap[left]
		if !ok {
			leftNode = &Node{value: left}
			b.nodeMap[left] = leftNode
		}
		node.left = leftNode
		leftNode.parent = node
	}
	if right != -1 {
		rightNode, ok := b.nodeMap[right]
		if !ok {
			rightNode = &Node{value: right}
			b.nodeMap[right] = rightNode
		}
		node.right = rightNode
		rightNode.parent = node
	}
}

func (b *Btree) setRoot() {
	if b.root != nil {
		return
	}
	for _, v := range b.nodeMap {
		for v.parent != nil {
			v = v.parent
		}
		b.root = v
		break
	}
}

func (b *Btree) setLevel(n *Node) {
	if n == b.root {
		n.level = 1
	} else {
		n.level = n.parent.level + 1
	}
	if n.left != nil {
		b.setLevel(n.left)
	}
	if n.right != nil {
		b.setLevel(n.right)
	}
}

func (b *Btree) setCountSubtree(n *Node) {
	if n.left != nil {
		b.setCountSubtree(n.left)
		n.leftSub = n.left.leftSub + n.left.rightSub + 1
	}
	if n.right != nil {
		b.setCountSubtree(n.right)
		n.rightSub = n.right.leftSub + n.right.rightSub + 1
	}
}
