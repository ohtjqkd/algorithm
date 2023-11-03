// 다시 풀어보기

// package main

// import (
// 	"bufio"
// 	"fmt"
// 	"os"
// 	"sort"
// )

// var (
// 	reader *bufio.Reader = bufio.NewReaderSize(os.Stdin, 1000000)
// 	writer *bufio.Writer = bufio.NewWriterSize(os.Stdout, 1000000)
// )

// func main() {
// 	var n, v int
// 	var keys []int
// 	var candPerm [][]int

// 	defer writer.Flush()

// 	fmt.Fscan(reader, &n)
// 	cand := make(map[int][]int)

// 	for i := 0; i < n; i++ {
// 		fmt.Fscan(reader, &v)
// 		cand[v] = append(cand[v], i)
// 	}
// 	fmt.Fprintln(writer, cand)
// 	for k, _ := range cand {
// 		keys = append(keys, k)
// 	}
// 	sort.Slice(keys, func(i, j int) bool {
// 		return keys[i] < keys[j]
// 	})
// 	for i := 0; i < len(keys); i++ {
// 		if keys[i] != 0 {
// 			for j := i + 1; j < len(keys); j++ {
// 				if keys[j] != 0 {
// 					candPerm = append(candPerm, []int{cand[keys[i]][0], cand[keys[j]][0]})
// 				}
// 			}
// 		}
// 	}
// 	if cand[0] != nil {
// 		for
// 	}
// }
