unit test单元测试
Python unittest库

Python 单元测试的几个技巧，分别是 mock、side_effect 和 patch。
这三者用法不一样，但都是一个核心思想，即用虚假的实现，
来替换掉被测试函数的一些依赖项，让我们能把更多的精力放在需要被测试的功能上。

mockmock 是单元测试中最核心重要的一环。mock 的意思，便是通过一个虚假对象，
来代替被测试函数或模块需要的对象。举个例子，比如你要测一个后端 API 逻辑的
功能性，但一般后端 API 都依赖于数据库、文件系统、网络等。这样，你就需要通
过 mock，来创建一些虚假的数据库层、文件系统层、网络层对象，以便可以简单地
对核心后端逻辑单元进行测试。

Mock Side Effect第二个我们来看 Mock Side Effect，这个概念很好理解，就是
mock 的函数，属性是可以根据不同的输入，返回不同的数值，而不只是一个
return_value

patch至于 patch，给开发者提供了非常便利的函数 mock 方法。它可以应用 Python
的 decoration 模式或是 context manager 概念，快速自然地 mock 所需的函数。
它的用法也不难，我们来看代码：