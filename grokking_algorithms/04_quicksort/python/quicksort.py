# -*- coding: utf-8 -*-
# @Author: Clarence
# @Date:   2020-01-08 09:57:49
# @Last Modified by:   Clarence
# @Last Modified time: 2020-01-08 10:36:04

def quicksort(array):
	if len(array) < 2:
		# base case, arrays with 0 or 1 element are already "sorted"
		return array 
	else : 
		# recursive case 
		pivot = array[0]
		# sub-array of all the elements less than the pivot 
		less = [i for i in array[1:] if i <= pivot]
		# sub-array of all the elements greater than the pivot 
		greater = [i for i in array[1:] if i > pivot]
		return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([1,0,20,9]))