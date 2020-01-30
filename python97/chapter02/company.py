#!usr/bin/python
# -*- coding:utf8 -*-

class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __getitem__(self, item):
        return self.employee[item]

    def __len__(self):
        return len(self.employee)

    # print(company)打印的时候调用此方法
    def __str__(self):
        return ','.join(self.employee)

    # 开发模式中company调用
    def __repr__(self):
        return ','.join(self.employee)

company = Company(["tom", "bob", "jane"])

company1 = company[1:]

print(len(company1))

for each in company1:
    print(each)