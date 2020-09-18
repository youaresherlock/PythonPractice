def my_generater(n):

    for i in range(n):
        print("开始生成数据...")
        yield i
        print("生成了一个数据...")

if __name__ == '__main__':
    for i in my_generater(4):
        print(i)
