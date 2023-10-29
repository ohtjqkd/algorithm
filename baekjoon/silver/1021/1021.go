package main

import (
	"errors"
	"fmt"
)

func appendleft(d *[]int, i int) {
	*d = append([]int{i}, *d...)
}

func popleft(d *[]int) (int, error) {
	if len(*d) == 0 {
		return 0, errors.New("Empty")
	}
	ret := (*d)[0]
	*d = (*d)[1:]
	return ret, nil
}

func pop(d *[]int) (int, error) {
	if len(*d) == 0 {
		return 0, errors.New("Empty")
	}
	ret := (*d)[len(*d)-1]
	*d = (*d)[:len(*d)-1]
	return ret, nil
}

func main() {
	var n, m, iv int
	var t, d []int

	ans := 0
	fmt.Scan(&n, &m)
	for i := 0; i < n; i++ {
		fmt.Scan(&iv)
		t = append(t, iv-1)
		d = append(d, i)
	}
	for i := 0; i < m; i++ {
		target := t[i]
		mo := 0
		for j := 0; j < len(d); j++ {
			if d[j] == target {
				for k := 0; k < j; k++ {
					v, err := popleft(&d)
					if err == nil {
						d = append(d, v)
					}
				}
				mo = j
				break
			} else if d[(len(d)-j)%len(d)] == target {
				for k := 0; k < j; k++ {
					v, err := pop(&d)
					if err == nil {
						appendleft(&d, v)
					}
				}
				mo = j
				break
			}
		}
		_, err := popleft(&d)
		if err == nil {
			ans += mo
		}
	}
	fmt.Println(ans)
}
