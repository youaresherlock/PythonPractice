e = 1
try:
    1/0
except ZeroDivisionError as e:
    pass
print(e)
"""
NameError: name 'e' is not defined
如果你在异常处理的 except block 中，把异常赋予了一个变量，
那么这个变量会在 except block 执行结束时被删除
When an exception has been assigned using as target, it is cleared 
at the end of the except clause.
"""