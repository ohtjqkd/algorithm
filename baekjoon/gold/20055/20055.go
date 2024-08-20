package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	reader *bufio.Reader = bufio.NewReader(os.Stdin)
	writer *bufio.Writer = bufio.NewWriter(os.Stdout)
	n, k   int
)

func main() {
	defer writer.Flush()
	var conv []int
	var robotLocation []int

	broken := 0
	answer := 0

	fmt.Fscanf(reader, "%d %d\n", &n, &k)

	for i := 0; i < 2*n; i++ {
		var tmp int
		fmt.Fscanf(reader, "%d ", &tmp)
		conv = append(conv, tmp)
	}

	for broken < k {
		answer++
		conv = append([]int{conv[len(conv)-1]}, conv[:len(conv)-1]...)
		for i := 0; i < len(robotLocation); i++ {
			robotLocation[i]++
		}
		robotLocation = unloadRobot(robotLocation)

		for i := 0; i < len(robotLocation); i++ {
			if conv[robotLocation[len(robotLocation)-i-1]+1] > 0 && (i == 0 || robotLocation[len(robotLocation)-i-1]+1 != robotLocation[len(robotLocation)-i]) {
				robotLocation[len(robotLocation)-i-1]++
				conv[robotLocation[len(robotLocation)-i-1]]--
				if conv[robotLocation[len(robotLocation)-i-1]] == 0 {
					broken++
				}
			}
		}
		robotLocation = unloadRobot(robotLocation)

		if conv[0] > 0 {
			robotLocation = append([]int{0}, robotLocation...)
			conv[0]--
			if conv[0] == 0 {
				broken++
			}
		}
		robotLocation = unloadRobot(robotLocation)
	}

	fmt.Fprintln(writer, answer)
}

func unloadRobot(robotLocation []int) []int {
	if len(robotLocation) != 0 && robotLocation[len(robotLocation)-1] == n-1 {
		robotLocation = robotLocation[:len(robotLocation)-1]
	}
	return robotLocation
}
