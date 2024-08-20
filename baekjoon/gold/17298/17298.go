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
	defer writer.Flush()

	var n int
	var A []int
	var result []int
	var stack [][]int

	fmt.Fscanf(reader, "%d\n", &n)

	for i := 0; i < n; i++ {
		var num int
		fmt.Fscanf(reader, "%d ", &num)
		A = append(A, num)
		result = append(result, -1)
	}
	for i := 0; i < n; i++ {
		if i == 0 {
			stack = append(stack, []int{A[i], i})
			continue
		}
		if len(stack) != 0 {
			for len(stack) != 0 {
				value, idx := stack[len(stack)-1][0], stack[len(stack)-1][1]
				if value < A[i] {
					result[idx] = A[i]
					stack = stack[:len(stack)-1]
				} else {
					break
				}
			}
			stack = append(stack, []int{A[i], i})
		}
		if i == n-1 {
			result[i] = -1
			continue
		}
	}
	for _, c := range result {
		fmt.Fprintf(writer, "%d ", c)
	}
}
