// input
// 6
// output
// 8 2
package main

import (
	"bufio"
	"fmt"
	"os"
)

var sc = bufio.NewScanner(os.Stdin)

func main() {
	var d int

	k := nextInt()
	n := 1
	flag := false
	for n < k {
		if k&n == n && flag == false {
			flag = true
		}
		if flag == true {
			d++
		}
		n <<= 1
	}
	fmt.Println(n, d)
}

func nextInt() int {
	sc.Scan()
	r := 0
	for i := range sc.Bytes() {
		r = r*10 + int(sc.Bytes()[i]-'0')
	}
	return r
}
