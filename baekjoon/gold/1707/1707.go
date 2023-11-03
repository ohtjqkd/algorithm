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
	var k, v, e, n1, n2 int

	defer writer.Flush()
	fmt.Fscanf(reader, "%d\n", &k)

	for i := 0; i < k; i++ {
		fmt.Fscanf(reader, "%d %d\n", &v, &e)
		edges := make([][]int, v)
		for j := 0; j < e; j++ {
			fmt.Fscanf(reader, "%d %d\n", &n1, &n2)
			edges[n1-1] = append(edges[n1-1], n2-1)
			edges[n2-1] = append(edges[n2-1], n1-1)
		}
		visited := make([]int, v)
		for i := 0; i < v; i++ {
			if visited[i] == 0 && !solution(edges, visited, i) {
				goto NO
			}
		}
		fmt.Fprintln(writer, "YES")
		continue
	NO:
		fmt.Fprintln(writer, "NO")
	}

}

func solution(e [][]int, v []int, s int) bool {
	var stack [][]int
	color := 1
	v[s] = color
	stack = append(stack, []int{s, v[s]})
	for len(stack) > 0 {
		p := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		currNode, currColor := p[0], p[1]
		adj := e[currNode]
		for _, ae := range adj {
			if v[ae] == currColor {
				return false
			} else if v[ae] == 0 {
				v[ae] = -currColor
				stack = append(stack, []int{ae, v[ae]})
			}
		}
	}
	return true
}
