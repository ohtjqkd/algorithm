// input
// MKKMMK
// output
// 505500
// 155105
package main

import (
	"fmt"
)

func main() {
	var s string
	fmt.Scanln(&s)
	mnr := make([]rune, len(s))
	mxr := make([]rune, len(s))
	m := 0
	for i := 0; i < len(s); i++ {
		if s[i] == 'K' {
			for j := i; j > i-m-1; j-- {
				switch j {
				case i:
					mnr[j] = '5'
					mxr[j-m] = '5'
				case i - m:
					mnr[j] = '1'
					mxr[j+m] = '0'
				default:
					mnr[j] = '0'
					mxr[j] = '0'
				}
			}
			m = 0
		} else if i == len(s)-1 {
			for j := i; j > i-m-1; j-- {
				if j == i-m {
					mnr[j] = '1'
					mxr[j] = '1'
				} else {
					mnr[j] = '0'
					mxr[j] = '1'
				}
			}
		} else {
			m++
		}
	}
	fmt.Println(string(mxr))
	fmt.Println(string(mnr))
}
