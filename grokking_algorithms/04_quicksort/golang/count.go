package main 

import "fmt"

/*
默认情况下，数组的每个元素都被初始化为元素类型对应的零值, 
对于数字类型来说就是0.
我们也可以使用数组字面值语法用一组值来初始化数组 
var q [3]int = [3]int{1,2,3}
在数组字面值中，如果在数组的长度位置出现的是“...”，省略号，
则表示数组的长度是根据初始化值得个数来计算
q := [...]int{1,2,3}
*/

func main() {
	a := [...]string{"a", "b", "c", "d"}
	for i := range a {
    	fmt.Println("Array item", i, "is", a[i])
	}
}
