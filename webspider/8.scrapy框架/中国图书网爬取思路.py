"""
中国图书网 上面的所有的图书的信息

起始页：  http://www.bookschina.com/books/kinder/
    抓取图书的大分类 还有小分类 小分类的url地址
    1. 确定起始页的url地址的响应中是有抓取的数据的
    2.  获取大分类 ： //div[@class='categoriesList']//h2
        获取每一个大分类的时候 遍历大分类的列表
        当前节点的下一个兄弟节点： following-sibling::下一个兄弟节点的标签名
    3. 获取小分类： /following-sibling::ul[1]/li
发送小分类url地址，请求小分类的图书的列表页
    4. 获取图书信息： //div[@class='bookList']//li
进入到列表页中 抓取列表页中的数据
    5. 翻页： //li[@class='next']/a/@href
        最后一个是没有下一页的那个标签，获取到的内容就是None
"""