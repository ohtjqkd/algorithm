package main

import "fmt"

func main() {
	var x int

	fmt.Scan(&x)

	i := 0
	for {
		if i*(i+1)/2 >= x && i*(i-1)/2 < x {
			break
		}
		i++
	}
	step := x - i*(i-1)/2
	if i%2 == 0 {
		fmt.Printf("%d/%d\n", step, i-step+1)
	} else {
		fmt.Printf("%d/%d\n", i-step+1, step)
	}
}
