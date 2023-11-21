package main

import (
	"errors"
	"fmt"
)

func max(i ...interface{}) (int, error) {
	if i == nil {
		return -1, errors.New("max: no arguments")
	}
	if len(i) == 2 {
		switch i[0].(type) {
		case int:
			switch i[1].(type) {
			case int:
				if i[0].(int) > i[1].(int) {
					return i[0].(int), error(nil)
				}
				return i[1].(int), error(nil)
			default:
				return -1, errors.New("max: invalid type")
			}
		default:
			return -1, errors.New("max: invalid type")
		}
	} else if len(i) == 1 {
		switch i[0].(type) {
		case []int:
			max := -1
			for _, v := range i[0].([]int) {
				if v > max {
					max = v
				}
			}
			return max, error(nil)
		default:
			return -1, errors.New("max: invalid type")
		}
	}
	return -1, error(nil)
}

func main() {

	fmt.Println(max(1, 2))

}
