package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	sc = bufio.NewScanner(os.Stdin)
	wr = bufio.NewWriter(os.Stdout)
)

func main() {
	n := nextInt()
	lines := make([][]int, n)
	dp := make([]int, n)
	defer wr.Flush()

	for i := 0; i < n; i++ {
		dp[i] = 1
		line := nextIntArr(2)
		lines[i] = line
	}

	sort(lines)

	for i := 0; i < n; i++ {
		for j := i - 1; j >= 0; j-- {
			if lines[i][1] > lines[j][1] {
				dp[i] = max(dp[i], dp[j]+1)
			}
		}
	}
	fmt.Fprintln(wr, n-max(dp...))
}

func max(arr ...int) int {
	ret := arr[0]
	for _, v := range arr {
		if ret < v {
			ret = v
		}
	}
	return ret
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

func sort(arr [][]int) {
	for i := 0; i < len(arr); i++ {
		for j := i + 1; j < len(arr); j++ {
			if arr[i][0] > arr[j][0] {
				arr[i], arr[j] = arr[j], arr[i]
			}
		}
	}
}
