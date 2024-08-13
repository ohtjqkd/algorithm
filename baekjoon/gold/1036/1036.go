package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

var (
	r = bufio.NewReader(os.Stdin)
	w = bufio.NewWriter(os.Stdout)
)

type Alphanumeric struct {
	alpha  rune
	degree [52]int
}

func compareAlphanumeric(a, b Alphanumeric) bool {
	for i := 51; i >= 0; i-- {
		if a.degree[i] < b.degree[i] {
			return true
		} else if a.degree[i] > b.degree[i] {
			return false
		}
	}
	return true
}

func atoi(c byte) int {
	if c >= '0' && c <= '9' {
		return int(c - '0')
	} else {
		return int(c - 'A' + 10)
	}
}

func itoa(a int) rune {
	if a >= 0 && a <= 9 {
		return rune(a + '0')
	} else {
		return rune(a - 10 + 'A')
	}
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func carry(a *[52]int) {
	for i := 0; i < len(a)-1; i++ {
		a[i+1] += a[i] / 36
		a[i] %= 36
	}
}

func main() {
	var n, k int
	var tmp string
	var nums [][]rune
	var alphanumerics [36]Alphanumeric

	defer w.Flush()

	fmt.Fscan(r, &n)

	for i := 0; i < n; i++ {
		fmt.Fscan(r, &tmp)
		nums = append(nums, []rune(tmp))
		for j := 1; j <= len(tmp); j++ {
			alphanumerics[atoi(tmp[len(tmp)-j])].alpha = rune(tmp[len(tmp)-j])
			alphanumerics[atoi(tmp[len(tmp)-j])].degree[j-1] += 35 - atoi(tmp[len(tmp)-j])
		}
	}

	for k, _ := range alphanumerics {
		carry(&alphanumerics[k].degree)
	}

	fmt.Fscan(r, &k)
	res := alphanumerics[:]
	sort.Slice(res, func(i, j int) bool {
		return !compareAlphanumeric(res[i], res[j])
	})

	res = res[:min(k, len(res))]
	for _, v := range res {
		for j := 0; j < len(nums); j++ {
			for k := 0; k < len(nums[j]); k++ {
				if nums[j][k] == v.alpha {
					nums[j][k] = 'Z'
				}
			}
		}
	}

	var totalSum [52]int
	for _, v := range nums {
		for i := 0; i < len(v); i++ {
			totalSum[i] += atoi(byte(v[len(v)-i-1]))
		}
	}
	carry(&totalSum)

	var ans string
	for i := len(totalSum) - 1; i >= 0; i-- {
		if totalSum[i] > 0 {
			for j := i; j >= 0; j-- {
				ans = ans + string(itoa(totalSum[j]))
			}
			break
		}
	}
	if ans == "" {
		ans = "0"
	}
	fmt.Fprintln(w, ans)
}
