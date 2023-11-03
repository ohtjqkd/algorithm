package main

import "fmt"

func main() {
	var n int

	fmt.Scan(&n)

}

func mergeSort(arr []string) []string {
	if len(arr) == 1 {
		return arr
	}
	ret := make([]string, len(arr))
	a, b := 0, 0
	for i := 0; i < len(arr); i++ {

	}
}

func compareSerial(a, b string) bool {
	switch {
	case len(a) < len(b):
		return true
	case len(a) > len(b):
		return false
	}
	sa, sb := serialNumSum(a), serialNumSum(b)
	switch {
	case sa < sb:
		return true
	case sa > sb:
		return false
	}
	if a < b {
		return true
	}
	return false
}

func serialNumSum(serial string) int {
	s := 0
	for c := range serial {
		fmt.Println(c)
	}
	return s
}
