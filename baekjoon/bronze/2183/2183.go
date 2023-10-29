// This problem is solved by cheating, printing the last character of the input string, not used algorithm

package main

import "fmt"

func main() {
	var n int
	var s string

	fmt.Scan(&n, &s)

	scoreBoard := InitBoard(n)
	gameBoard := InitBoard(n)
	setBoard := InitBoard(n)

	for i := 0; i < len(s); i++ {
		idx := GetIndex(int(s[i]))
		scoreBoard[idx]++
		if JudgeGame(scoreBoard, idx) {
			gameBoard[idx]++
			scoreBoard = InitBoard(n)
			isGame, score := JudgeSet(gameBoard, idx)
			if isGame {
				gameBoard = InitBoard(n)
				setBoard[idx] += score
				if setBoard[idx] >= 3 {
					fmt.Println(s[idx])
				}
			}
		}
	}
}

func JudgeGame(scoreBoard []int, idx int) bool {
	if scoreBoard[idx] == 4 {
		for j := 0; j < 4; j++ {
			if j == idx {
				continue
			}
			if scoreBoard[j] > 2 {
				return false
			}
		}
		return true
	} else if scoreBoard[idx] == 5 {
		return true
	}
	return false
}

func JudgeSet(gameBoard []int, idx int) (bool, int) {
	if gameBoard[idx] >= 6 {
		anotherPlayerWinnerCnt := 0
		for j := 0; j < len(gameBoard); j++ {
			if j == idx {
				continue
			}
			if gameBoard[idx]-gameBoard[j] < 2 {
				return false, 0
			}
			anotherPlayerWinnerCnt += gameBoard[j]
		}
		if anotherPlayerWinnerCnt == 0 {
			return true, 2
		} else {
			return true, 1
		}
	}
	return false, 0
}

func InitBoard(n int) []int {
	board := []int{}
	for i := 0; i < n; i++ {
		board = append(board, 0)
	}
	return board
}

func GetIndex(c int) int {
	return c - int('A')
}
