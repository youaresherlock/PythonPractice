/*
* @Author: Clarence
* @Date:   2020-01-19 11:46:52
* @Last Modified by:   Clarence
* @Last Modified time: 2020-01-19 11:51:04
*/
package main 

import "fmt"

var voted map[string]bool 

func main()  {
	voted = make(map[string]bool)
	check_voter("tom")
	check_voter("mike")
	check_voter("mike")
}

func check_voter(name string) {
	if voted[name] {
		fmt.Println("kick them out!")
	} else {
		voted[name] = true 
		fmt.Println("let them vote!")
	}
}