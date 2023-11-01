package main

import (
	"fmt"
)

func main() {
	var n, m int

	fmt.Scan(&n, &m)

	ans := 0
	initBoard := make([][]rune, n)
	targetBoard := make([][]rune, n)

	for i := 0; i < n; i++ {
		initBoard[i] = make([]rune, m)
		for j := 0; j < m; j++ {
			if j == m-1 {
				fmt.Scanf("%c\n", &initBoard[i][j])
			} else {
				fmt.Scanf("%c", &initBoard[i][j])
			}
			initBoard[i][j] -= '0'
		}
	}
	for i := 0; i < n; i++ {
		targetBoard[i] = make([]rune, m)
		for j := 0; j < m; j++ {
			if j == m-1 {
				fmt.Scanf("%c\n", &targetBoard[i][j])
			} else {
				fmt.Scanf("%c", &targetBoard[i][j])
			}
			targetBoard[i][j] -= '0'
		}
	}
	for i := 0; i < n-2; i++ {
		for j := 0; j < m-2; j++ {
			if initBoard[i][j] != targetBoard[i][j] {
				reverse(&initBoard, i, j)
				ans++
			}
		}
	}

	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			if initBoard[i][j] != targetBoard[i][j] {
				ans = -1
				break
			}
		}
	}
	fmt.Println(ans)
}

func reverse(start *[][]rune, x, y int) {
	for i := 0; i < 3; i++ {
		for j := 0; j < 3; j++ {
			(*start)[x+i][y+j] = (*start)[x+i][y+j] ^ 1
		}
	}
}
