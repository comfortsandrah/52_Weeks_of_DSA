package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strconv"
	"strings"
)

/*
 * Complete the 'equalStacks' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER_ARRAY h1
 *  2. INTEGER_ARRAY h2
 *  3. INTEGER_ARRAY h3
 */

// This is the Function I implemented Hacker Rank provided the rest of the code
// Equal Stacks

func equalStacks(h1 []int32, h2 []int32, h3 []int32) int32 {
	// Write your code here

	sumH1 := sumOfArray(h1)
	sumH2 := sumOfArray(h2)
	sumH3 := sumOfArray(h3)

	i, j, k := 0, 0, 0

	for !(sumH1 == sumH2 && sumH2 == sumH3) {
		if len(h1) == 0 || len(h2) == 0 || len(h3) == 0 {
			return 0
		}

		if sumH1 > sumH2 && sumH1 > sumH3 {
			h1 = dequeue(h1)
			sumH1 = sumOfArray(h1)
			i++
		} else if sumH2 > sumH1 && sumH2 > sumH3 {
			h2 = dequeue(h2)
			sumH2 = sumOfArray(h2)
			j++
		} else {
			h3 = dequeue(h3)
			sumH3 = sumOfArray(h3)
			k++
		}
	}

	return sumH1

}

func sumOfArray(h1 []int32) int32 {
	var sum int32
	for i := 0; i < len(h1); i++ {
		sum += h1[i]
	}

	return sum
}

func dequeue(arr []int32) (arr1 []int32) {
	newQueue := (arr)[1:]
	return newQueue
}

func main() {
	reader := bufio.NewReaderSize(os.Stdin, 16*1024*1024)

	stdout, err := os.Create(os.Getenv("OUTPUT_PATH"))
	checkError(err)

	defer stdout.Close()

	writer := bufio.NewWriterSize(stdout, 16*1024*1024)

	firstMultipleInput := strings.Split(strings.TrimSpace(readLine(reader)), " ")

	n1Temp, err := strconv.ParseInt(firstMultipleInput[0], 10, 64)
	checkError(err)
	n1 := int32(n1Temp)

	n2Temp, err := strconv.ParseInt(firstMultipleInput[1], 10, 64)
	checkError(err)
	n2 := int32(n2Temp)

	n3Temp, err := strconv.ParseInt(firstMultipleInput[2], 10, 64)
	checkError(err)
	n3 := int32(n3Temp)

	h1Temp := strings.Split(strings.TrimSpace(readLine(reader)), " ")

	var h1 []int32

	for i := 0; i < int(n1); i++ {
		h1ItemTemp, err := strconv.ParseInt(h1Temp[i], 10, 64)
		checkError(err)
		h1Item := int32(h1ItemTemp)
		h1 = append(h1, h1Item)
	}

	h2Temp := strings.Split(strings.TrimSpace(readLine(reader)), " ")

	var h2 []int32

	for i := 0; i < int(n2); i++ {
		h2ItemTemp, err := strconv.ParseInt(h2Temp[i], 10, 64)
		checkError(err)
		h2Item := int32(h2ItemTemp)
		h2 = append(h2, h2Item)
	}

	h3Temp := strings.Split(strings.TrimSpace(readLine(reader)), " ")

	var h3 []int32

	for i := 0; i < int(n3); i++ {
		h3ItemTemp, err := strconv.ParseInt(h3Temp[i], 10, 64)
		checkError(err)
		h3Item := int32(h3ItemTemp)
		h3 = append(h3, h3Item)
	}

	result := equalStacks(h1, h2, h3)

	fmt.Fprintf(writer, "%d\n", result)

	writer.Flush()
}

func readLine(reader *bufio.Reader) string {
	str, _, err := reader.ReadLine()
	if err == io.EOF {
		return ""
	}

	return strings.TrimRight(string(str), "\r\n")
}

func checkError(err error) {
	if err != nil {
		panic(err)
	}
}
