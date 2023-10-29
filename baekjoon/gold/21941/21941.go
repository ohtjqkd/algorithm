// input
// abcxyzxabc
// 2
// abc 10
// xyz 5

// output
// 26

package main

import (
	"fmt"
)

type StringInfo struct {
	value  string
	Weight float32
	Score  int
}

type A []StringInfo

func (a A) Len() int           { return len(a) }
func (a A) Less(i, j int) bool { return a[i].Weight > a[j].Weight }
func (a A) Swap(i, j int)      { a[i], a[j] = a[j], a[i] }

func main() {
	fmt.Println("21941")
	var S string
	var M int
	var scoreDict = make(map[string]int)
	var dp []int

	fmt.Scan(&S)
	fmt.Scan(&M)

	for i := 0; i < len(S); i++ {
		dp = append(dp, 0)
	}
	fmt.Println(dp)
	for i := 0; i < M; i++ {
		var str string
		var score int

		fmt.Scan(&str, &score)
		scoreDict[str] = score
	}

	for i := 0; i < len(S); i++ {
		for j := i; j >= 0; j-- {
			var s = S[j : i+1]
			var d int

			if val, ok := scoreDict[s]; ok {
				d = val
			} else {
				d = len(s)
			}

			if j == 0 {
				dp[i] = max(dp[i], d)
			} else {
				dp[i] = max(dp[i], d+dp[j-1])
			}
		}
	}
	fmt.Println(dp[len(S)-1])
}
