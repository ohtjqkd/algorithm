package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

var (
	reader *bufio.Reader = bufio.NewReader(os.Stdin)
	writer *bufio.Writer = bufio.NewWriter(os.Stdout)
)

func main() {
	var na, nb, v int
	var ans []int

	defer writer.Flush()

	fmt.Fscanf(reader, "%d %d\n", &na, &nb)

	dic := make(map[int]bool, 500_000)
	for i := 0; i < na; i++ {
		fmt.Fscan(reader, &v)
		dic[v] = true
	}

	for i := 0; i < nb; i++ {
		fmt.Fscan(reader, &v)
		delete(dic, v)
	}

	for k := range dic {
		ans = append(ans, k)
	}

	sort.Slice(ans, func(i, j int) bool {
		return ans[i] < ans[j]
	})

	//It is slower than upper case
	// ans = solution(na, nb)

	fmt.Fprintln(writer, len(ans))
	for i, v := range ans {
		if i+1 == len(ans) {
			fmt.Fprintln(writer, v)
		} else {
			fmt.Fprintf(writer, "%d ", v)
		}
	}
}

func solution(na, nb int) []int {
	var aArr, bArr []int
	var v int

	for i := 0; i < na; i++ {
		fmt.Fscan(reader, &v)
		aArr = append(aArr, v)
	}
	for i := 0; i < nb; i++ {
		fmt.Fscan(reader, &v)
		bArr = append(bArr, v)
	}

	sort.Slice(aArr, func(i, j int) bool {
		return aArr[i] < aArr[j]
	})
	sort.Slice(bArr, func(i, j int) bool {
		return bArr[i] < bArr[j]
	})

	var ans []int
	for len(aArr) > 0 && len(bArr) > 0 {
		if aArr[0] == bArr[0] {
			aArr = aArr[1:]
			bArr = bArr[1:]
		} else if aArr[0] > bArr[0] {
			bArr = bArr[1:]
		} else {
			ans = append(ans, aArr[0])
			aArr = aArr[1:]
		}
	}
	for _, v := range aArr {
		ans = append(ans, v)
	}
	return ans
}
