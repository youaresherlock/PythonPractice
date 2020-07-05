#!usr/bin/python
# -*- coding:utf8 -*-
"""
修改列表单个元素,修改列表多个元素(不改变id)
"""
nums = [1,2,3]
nums[2] = 4
print(nums)
# nums[:] = [2, 5, 9]
nums[:] = 2, 5, 9
print(nums)