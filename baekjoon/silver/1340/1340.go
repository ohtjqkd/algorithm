package main

import "fmt"

func main() {
	var month map[string]int = map[string]int{
		"January":   1,
		"February":  2,
		"March":     3,
		"April":     4,
		"May":       5,
		"June":      6,
		"July":      7,
		"August":    8,
		"September": 9,
		"October":   10,
		"November":  11,
		"December":  12,
	}
	var leapYear []int = []int{0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31}
	var nonLeapYear []int = []int{0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31}
	var y, m, d, h, mm, now int
	var ms string
	for i := 1; i < 13; i++ {
		leapYear[i] += leapYear[i-1]
		nonLeapYear[i] += nonLeapYear[i-1]
	}
	fmt.Scanf("%s %d, %d %d:%d", &ms, &d, &y, &h, &mm)
	m = month[ms]

	totalTime := getTotalDay(y) * 24 * 60
	if isLeapYear(y) {
		now = leapYear[m-1]*24*60 + (d-1)*24*60 + h*60 + mm
	} else {
		now = nonLeapYear[m-1]*24*60 + (d-1)*24*60 + h*60 + mm
	}

	fmt.Println(float64(now) / float64(totalTime) * 100)
}

func isLeapYear(year int) bool {
	return year%400 == 0 || (year%4 == 0 && year%100 != 0)
}

func getTotalDay(year int) int {
	if isLeapYear(year) {
		return 366
	}
	return 365
}
