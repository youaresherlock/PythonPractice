/*
* @Author: Clarence
* @Date:   2020-01-19 11:46:52
* @Last Modified by:   Clarence
* @Last Modified time: 2020-01-19 11:48:40
*/
package main 

import "fmt"

var book map[string]float64

func main() {
	book = make(map[string]float64)
	book["apple"] = 0.67 
	book["milk"] = 1.49 
	book["avocado"] = 1.49 
	fmt.Println(book)
}