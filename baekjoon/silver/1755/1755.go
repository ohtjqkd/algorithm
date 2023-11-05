package main

import (
	"fmt"
	"strconv"
	"strings"
)

var alph = map[rune]string{'0': "zero", '1': "one", '2': "two", '3': "three", '4': "four", '5': "five", '6': "six", '7': "seven", '8': "eight", '9': "nine"}

func main() {
	var m, n int
	var str []string

	fmt.Scan(&m, &n)

	for i := m; i < n+1; i++ {
		str = append(str, strconv.Itoa(i))
	}

	for i := 0; i < len(str)-1; i++ {
		for j := 0; j < len(str)-1-i; j++ {
			if !compareNumberPlay(str[j], str[j+1]) {
				str[j], str[j+1] = str[j+1], str[j]
			}
		}
	}

	for i := 0; i < len(str); i += 10 {
		fmt.Println(strings.Join(str[i:min(len(str), i+10)], " "))
	}
}

func compareNumberPlay(a, b string) bool {
	var aStr, bStr []string
	for _, v := range a {
		aStr = append(aStr, alph[v])
	}
	for _, v := range b {
		bStr = append(bStr, alph[v])
	}
	aa := strings.Join(aStr, " ")
	bb := strings.Join(bStr, " ")

	if aa < bb {
		return true
	}
	return false
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
