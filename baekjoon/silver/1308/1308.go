package main

import "fmt"

func main() {
	var leapYear []int = []int{31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31}
	var normYear []int = []int{31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31}

	var sy, sm, sd, ey, em, ed, ans int
	fmt.Scanf("%d %d %d", &sy, &sm, &sd)
	fmt.Scanf("%d %d %d", &ey, &em, &ed)

	for i := 1; i < 12; i++ {
		leapYear[i] += leapYear[i-1]
		normYear[i] += normYear[i-1]
	}

	if isGG(sy, sm, sd, ey, em, ed) {
		fmt.Println("gg")
		return
	}

	for i := sy; i < ey; i++ {
		if isLeapYear(i) {
			ans += 366
		} else {
			ans += 365
		}
	}
	if sm != 1 {
		if isLeapYear(sy) {
			ans -= leapYear[sm-2]
		} else {
			ans -= normYear[sm-2]
		}
	}
	if em != 1 {
		if isLeapYear(ey) {
			ans += leapYear[em-2]
		} else {
			ans += normYear[em-2]
		}
	}
	fmt.Printf("D-%v\n", ans-sd+ed)
}

func isLeapYear(year int) bool {
	return year%4 == 0 && year%100 != 0 || year%400 == 0
}

func isGG(sy, sm, sd, ey, em, ed int) bool {
	if sy+1000 < ey {
		return true
	} else if sy+1000 == ey && sm < em {
		return true
	} else if sy+1000 == ey && sm == em && sd <= ed {
		return true
	}
	return false
}
