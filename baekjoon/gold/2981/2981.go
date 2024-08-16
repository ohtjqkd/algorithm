package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"sort"
)

var (
	reader *bufio.Reader = bufio.NewReader(os.Stdin)
	writer *bufio.Writer = bufio.NewWriter(os.Stdout)
)

func main() {
	defer writer.Flush()
	var n int
	var result, answerList []int

	answer := make(map[int]bool)

	fmt.Fscanf(reader, "%d\n", &n)
	arr := make([]int, n)

	for i := 0; i < n; i++ {
		fmt.Fscanf(reader, "%d\n", &arr[i])
	}

	sort.Slice(arr, func(i, j int) bool {
		return arr[i] < arr[j]
	})

	m := arr[n-1] - arr[0]
	msqrt := math.Sqrt(float64(m))

	for i := 2; i <= int(msqrt)+1; i++ {
		if m%i == 0 {
			result = append(result, i)
			result = append(result, m/i)
		}
	}
	result = append(result, m)

	for _, v1 := range result {
		tmp := arr[0] % v1
		check := true
		for _, v2 := range arr {
			if v2%v1 == tmp {
				continue
			} else {
				check = false
				break
			}
		}
		if check && !answer[v1] {
			answer[v1] = true
		}
	}
	for k, _ := range answer {
		answerList = append(answerList, k)
	}
	sort.Slice(answerList, func(i, j int) bool {
		return answerList[i] < answerList[j]
	})
	for i := 0; i < len(answerList); i++ {
		fmt.Fprintf(writer, "%d", answerList[i])
		if i != len(answerList)-1 {
			fmt.Fprintf(writer, " ")
		} else {
			fmt.Fprintf(writer, "\n")
		}
	}
}
