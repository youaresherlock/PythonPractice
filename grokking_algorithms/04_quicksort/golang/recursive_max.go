/*
* @Author: Clarence
* @Date:   2020-01-08 10:06:19
* @Last Modified by:   Clarence
* @Last Modified time: 2020-01-08 10:31:06
*/
package main 

import "fmt"

func max(list []int) int {
	if len(list) == 2 {
		if list[0] > list[1] {
			return list[0]
		}
		return list[1]
	} else if len(list) == 1 {
		return list[0]
	} else if len(list) == 0 {
		return -1 
	}

	subMax := max(list[1:])
	if list[0] > subMax {
		return list[0]
	}
	return subMax 
}

func main() {
	fmt.Println(max([]int{1, 5, 10, 25, 16, 1}))
}