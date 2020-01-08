/*
* @Author: Clarence
* @Date:   2020-01-08 10:06:09
* @Last Modified by:   Clarence
* @Last Modified time: 2020-01-08 10:23:11
*/
package main 

import "fmt"

func sum(arr []int) int {
	if len(arr) == 0 {
		return 0 
	}
	return arr[0] + sum(arr[1:])
}

func main() {
	fmt.Println(sum([]int{1, 2, 3, 4}))
}