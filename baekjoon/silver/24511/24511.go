package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	var t, v, r []string
	var n, m int

	reader := bufio.NewReaderSize(os.Stdin, 1000000)
	fmt.Fscan(reader, &n)
	for i := 0; i < n; i++ {
		var a string
		fmt.Fscan(reader, &a)
		t = append(t, a)
	}
	for i := 0; i < n; i++ {
		var a string
		fmt.Fscan(reader, &a)
		v = append(v, a)
	}
	for i := n - 1; i >= 0; i-- {
		if t[i] == "0" {
			r = append(r, v[i])
		}
	}
	fmt.Fscan(reader, &m)
	for i := 0; i < m; i++ {
		var a string
		fmt.Fscan(reader, &a)
		r = append(r, a)
	}
	fmt.Println(strings.Join(r[:m], " "))
	// line, _, _ := reader.ReadLine()
	// t, _, _ := reader.ReadLine()
	// v, _, _ := reader.ReadLine()
	// tArr := strings.Split(strings.TrimSpace(string(t)), " ")
	// vArr := strings.Split(strings.TrimSpace(string(v)), " ")
	// for i := len(tArr) - 1; i >= 0; i-- {
	// 	if tArr[i] == "0" {
	// 		r = append(r, vArr[i])
	// 	}
	// }
	// _, _, _ = reader.ReadLine()
	// line, _, _ = reader.ReadLine()
	// inputArr := strings.Split(strings.TrimSpace(string(line)), " ")
	// r = append(r, inputArr...)
	// fmt.Println(strings.Join(r[:len(inputArr)], " "))
}
