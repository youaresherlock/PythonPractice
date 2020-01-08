/*
* @Author: Clarence
* @Date:   2020-01-08 10:06:15
* @Last Modified by:   Clarence
* @Last Modified time: 2020-01-08 10:41:55
*/
package main 

import "fmt"

func quicksort(list []int) []int {
	if len(list) < 2 {
		return list 
	} else {
		pivot := list[0]

		var less = []int{}
		var greater = []int{}
		for _, num := range list[1:] {
			if pivot > num {
				less = append(less, num)
			} else {
				greater = append(greater, num)
			}
		}
		less = append(quicksort(less), pivot)
		greater = quicksort(greater)
		return append(less, greater...)
	}
}

func main() {
	fmt.Println(quicksort([]int{10, 5, 2, 3}))
}