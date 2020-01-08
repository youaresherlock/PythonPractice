/*
* @Author: Clarence
* @Date:   2020-01-08 10:05:54
* @Last Modified by:   Clarence
* @Last Modified time: 2020-01-08 10:21:08
*/
package main 

import "fmt"

func sum(arr []int) int {
	total := 0 
	for _, num := range arr {
		total += num 
	}

	return total 
}

func main() {
	fmt.Println(sum([]int{0, 10, 20, 9}))
}