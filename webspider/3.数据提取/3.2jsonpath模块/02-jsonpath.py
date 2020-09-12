#!usr/bin/python
# -*- coding:utf8 -*-
book_dict = {
  "store": {
    "book": [
      { "category": "reference",
        "author": "Nigel Rees",
        "title": "Sayings of the Century",
        "price": 8.95
      },
      { "category": "fiction",
        "author": "Evelyn Waugh",
        "title": "Sword of Honour",
        "price": 12.99
      },
      { "category": "fiction",
        "author": "Herman Melville",
        "title": "Moby Dick",
        "isbn": "0-553-21311-3",
        "price": 8.99
      },
      { "category": "fiction",
        "author": "J. R. R. Tolkien",
        "title": "The Lord of the Rings",
        "isbn": "0-395-19395-8",
        "price": 22.99
      }
    ],
    "bicycle": {
      "color": "red",
      "price": 19.95
    }
  }
}

from jsonpath import jsonpath

# 获取所有的作者
# res = jsonpath(book_dict, '$.store.book[*].author')
# res = jsonpath(book_dict, '$..author')

# 获取第一本书的作者
# res = jsonpath(book_dict, '$.store.book[1].author')

res = jsonpath(book_dict, '$..book')
print(res)

















