// input
// 8808 8880
// output
// 2
package main

import "fmt"

func main() {
	var l, r int

	fmt.Scan(&l, &r)
	ans := 0
	_, ans = rec(l, r)
	fmt.Println(ans)
}

func rec(l, r int) (bool, int) {
	if r == 0 {
		return true, 0
	}
	b, v := rec(l/10, r/10)
	if b {
		if l%10 == 8 && r%10 == 8 {
			return true, v + 1
		} else if l%10 == r%10 {
			return true, v
		}
		return false, v
	} else {
		return false, v
	}
}
