package main

import (
	"fmt"
	"strconv"
	"strings"
)

func main() {
	var n int

	fmt.Scan(&n)
	i := 666
	for {
		if strings.Contains(strconv.Itoa(i), "666") {
			n--
		}
		if n == 0 {
			fmt.Println(i)
			return
		}
		i++
	}
}
