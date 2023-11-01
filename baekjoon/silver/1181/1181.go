package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strings"
)

var (
	reader *bufio.Reader = bufio.NewReader(os.Stdin)
	writer *bufio.Writer = bufio.NewWriter(os.Stdout)
)

func main() {
	var n int
	var s string
	var arr []string

	defer writer.Flush()

	dict := make(map[string]bool)
	fmt.Fscan(reader, &n)
	for i := 0; i < n; i++ {
		fmt.Fscan(reader, &s)
		if dict[s] == false {
			arr = append(arr, s)
			dict[s] = true
		}
	}
	sort.Slice(arr, func(i, j int) bool {
		if len(arr[i]) == len(arr[j]) {
			return arr[i] < arr[j]
		}
		return len(arr[i]) < len(arr[j])
	})
	fmt.Fprintln(writer, strings.Join(arr, "\n"))
}
