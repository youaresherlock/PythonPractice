#!usr/bin/python
# -*- coding:utf8 -*-

class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __getitem__(self, item):
        return self.employee[item]

company = Company(["tom", "bob", "jane"])

for each in company:
    print(each)