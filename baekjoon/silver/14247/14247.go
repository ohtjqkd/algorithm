// // input
// // 5
// // 1 3 2 4 6
// // 2 7 3 4 1
// // output
// // 64

// success code
// package main

// import (
// 	"bufio"
// 	"fmt"
// 	"os"
// 	"sort"
// )

// var r = bufio.NewReader(os.Stdin)

// func main() {
// 	var n, v int
// 	var a, b []int

// 	ans := 0
// 	fmt.Fscan(r, &n)
// 	for i := 0; i < n; i++ {
// 		fmt.Fscan(r, &v)
// 		a = append(a, v)
// 	}
// 	for i := 0; i < n; i++ {
// 		fmt.Fscan(r, &v)
// 		b = append(b, v)
// 	}
// 	sort.Slice(b, func(i, j int) bool {
// 		return b[i] < b[j]
// 	})
// 	for i := 0; i < n; i++ {
// 		ans += a[i] + b[i]*i
// 	}
// 	fmt.Println(ans)
// }

// fail code
package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

var sc = bufio.NewScanner(os.Stdin)

func main() {
	n := nextInt()
	a := nextIntArr(n)
	b := nextIntArr(n)
	ans := 0
	sort.Slice(b, func(i, j int) bool {
		return b[i] < b[j]
	})
	for i := 0; i < n; i++ {
		ans += a[i] + b[i]*i
	}
	fmt.Println(ans)
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
	for _, v := range sc.Bytes() {
		if v == ' ' {
			ret[idx] = i
			i = 0
			idx++
		} else if v >= '0' && v <= '9' {
			i = i*10 + int(v-'0')
		}
	}
	ret[idx] = i
	return ret
}
