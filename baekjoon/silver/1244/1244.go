package main

import (
	"bufio"
	"fmt"
	"os"
)

func min(a, b int) int {
	if a > b {
		return b
	}
	return a
}

func main() {
	var N, M int
	var iv, g, k int
	var s []int

	reader := bufio.NewReaderSize(os.Stdin, 10000)
	fmt.Fscan(reader, &N)
	for i := 0; i < N; i++ {
		fmt.Fscan(reader, &iv)
		s = append(s, iv)
	}
	fmt.Fscan(reader, &M)
	for i := 0; i < M; i++ {
		fmt.Fscan(reader, &g, &k)
		if g == 1 {
			for j := k - 1; j < N; j += k {
				s[j] ^= 1
			}
		} else {
			s[k-1] ^= 1
			for j := 0; j < min(N+1-k, k); j++ {
				if s[k-1-j] == s[k-1+j] {
					s[k-1-j] ^= 1
					s[k-1+j] ^= 1
				} else {
					break
				}
			}
		}
	}
	for i := 0; i < N; i += 20 {
		for j := i; j < min(i+20, N); j++ {
			if j != min(i+20, N)-1 {
				fmt.Print(s[j], " ")
			} else {
				fmt.Println(s[j])
			}
		}
	}
}
