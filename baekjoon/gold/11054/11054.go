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

	fmt.Fscanf(reader, "%d\n", &n)
	arr := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Fscanf(reader, "%d ", &arr[i])
	}

	dp1 := make([]int, n)
	dp2 := make([]int, n)
	for i := 0; i < n; i++ {
		dp1[i] = 1
		for j := 0; j < i; j++ {
			if arr[j] < arr[i] && dp1[i] < dp1[j]+1 {
				dp1[i] = dp1[j] + 1
			}
		}
	}

	for i := n - 1; i >= 0; i-- {
		dp2[i] = 1
		for j := n - 1; j > i; j-- {
			if arr[j] < arr[i] && dp2[i] < dp2[j]+1 {
				dp2[i] = dp2[j] + 1
			}
		}
	}

	max := 0
	for i := 0; i < n; i++ {
		if max < dp1[i]+dp2[i]-1 {
			max = dp1[i] + dp2[i] - 1
		}
	}

	fmt.Fprintln(writer, max)
}
