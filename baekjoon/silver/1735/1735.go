package main

import "fmt"

func main() {
	var o1, u1, o2, u2 int

	fmt.Scanf("%d %d\n", &o1, &u1)
	fmt.Scanf("%d %d\n", &o2, &u2)
	g1 := gcd(u1, u2)
	o3 := ((o1 * u2) + (o2 * u1)) / g1
	u3 := (u1 * u2) / g1
	g2 := gcd(o3, u3)
	fmt.Println(o3/g2, u3/g2)
}

func gcd(a, b int) int {
	if b == 0 {
		return a
	}
	return gcd(b, a%b)
}
