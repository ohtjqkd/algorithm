package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	reader = bufio.NewReader(os.Stdin)
	writer = bufio.NewWriter(os.Stdout)
)

func main() {
	var N, M int
	fmt.Fscanf(reader, "%d %d\n", &N, &M)

	for i := 1; i <= N; i++ {
		pick(N, M-1, []int{i})
	}
}

func pick(n, m int, arr []int) {
	if m == 0 {
		for i := 0; i < len(arr); i++ {
			if i == len(arr)-1 {
				fmt.Println(arr[i])
			} else {
				fmt.Print(arr[i], " ")
			}
		}
	} else {
		for i := 1; i <= n; i++ {
			if arr[len(arr)-1] <= i {
				pick(n, m-1, append(arr, i))
			}
		}
	}
}
