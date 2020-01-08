/*
* @Author: Clarence
* @Date:   2020-01-08 10:06:15
* @Last Modified by:   Clarence
* @Last Modified time: 2020-01-08 10:25:28
*/
package main 

import "fmt"

func count(arr []int) int {
	if len(arr) == 0 {
		return 0 
	}
	return 1 + count(arr[1:])
}

func main() {
	fmt.Println(count([]int{1, 2, 3, 4}))
}