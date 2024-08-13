package main

import "fmt"

func main() {
	var n, num, ans int
	var nums []int

	fmt.Scan(&n)
	for i := 0; i < n; i++ {
		fmt.Scan(&num)
		if i == 0 {
			continue
		}
		nums = append(nums, num-1)
	}

	for i := 0; i < len(nums); i++ {
		if nums[i] == 0 {
			continue
		}
		ans++
		for j := i + 1; j < len(nums); j++ {
			if nums[j]%nums[i] == 0 {
				nums[j] = 0
			}
		}
		nums[i] = 0
	}
	fmt.Println(ans)
}
