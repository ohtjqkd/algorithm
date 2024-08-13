package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

var (
	r = bufio.NewReader(os.Stdin)
	w = bufio.NewWriter(os.Stdout)
)

func makeUnderbarString(n int) string {
	ret := ""
	for i := 0; i < n; i++ {
		ret += "_"
	}
	return ret
}

func main() {
	var n, m, length int
	defer w.Flush()

	fmt.Fscan(r, &n, &m)
	words := make([]string, 2*n-1)
	for i := 0; i < n; i++ {
		fmt.Fscan(r, &words[2*i])
		length += len(words[2*i])
	}
	mod := (m - length) % (n - 1)
	for i := 0; i < n-1; i++ {
		if words[2*(i+1)][0] < 'a' || mod == 0 {
			words[2*(i+1)-1] = makeUnderbarString((m - length) / (n - 1))
		} else if words[2*(i+1)][0] >= 'a' {
			words[2*(i+1)-1] = makeUnderbarString((m-length)/(n-1) + 1)
			mod--
		}
	}
	if mod != 0 {
		for i := 2*n - 3; i >= 1; i -= 2 {
			if mod == 0 {
				break
			}
			if words[i+1][0] < 'a' {
				words[i] += "_"
				mod--
			}
		}
	}
	fmt.Fprintln(w, strings.Join(words, ""))
}
