package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

var (
	r = bufio.NewReader(os.Stdin)
	w = bufio.NewWriter(os.Stdout)
)

func sum(dice [6]int) int {
	ret := 0
	for _, v := range dice {
		ret += v
	}
	return ret
}

func min(dice [6]int) int {
	min := dice[0]
	for i := 1; i < 6; i++ {
		if dice[i] < min {
			min = dice[i]
		}
	}
	return min
}

func max(dice [6]int) int {
	max := dice[0]
	for i := 1; i < 6; i++ {
		if dice[i] > max {
			max = dice[i]
		}
	}
	return max
}

func maxInt(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func pow(a, b int) int {
	ret := 1
	for i := 0; i < b; i++ {
		ret *= a
	}
	return ret
}

func getMinCorner(dice [6]int) int {
	ret := math.MaxInt64
	for i := 0; i < 2; i++ {
		for j := 2; j < 4; j++ {
			for k := 4; k < 6; k++ {
				if dice[i]+dice[j]+dice[k] < ret {
					ret = dice[i] + dice[j] + dice[k]
				}
			}
		}
	}
	return ret
}

func getMinSide(dice [6]int) int {
	ret := math.MaxInt64
	for i := 0; i < 4; i++ {
		for j := i + (2 - i%2); j < 6; j++ {
			if dice[i]+dice[j] < ret {
				ret = dice[i] + dice[j]
			}
		}
	}
	return ret
}

func main() {
	defer w.Flush()
	var n, ans int
	var dice [6]int
	var newDice [6]int
	var minCorner, minSide, minDice int

	fmt.Fscan(r, &n)
	for i := 0; i < 6; i++ {
		fmt.Fscan(r, &dice[i])
	}
	newDice[0], newDice[1] = dice[0], dice[5]
	newDice[2], newDice[3] = dice[1], dice[4]
	newDice[4], newDice[5] = dice[2], dice[3]
	if n == 1 {
		fmt.Fprintln(w, sum(dice)-max(dice))
	} else {
		minCorner = getMinCorner(newDice)
		minSide = getMinSide(newDice)
		minDice = min(newDice)
		ans = 4*minCorner + (maxInt(n-2, 0)*8+4)*minSide + (pow(maxInt(0, n-2), 2)*5+maxInt(0, n-2)*4)*minDice
		fmt.Fprintln(w, ans)
	}
}
