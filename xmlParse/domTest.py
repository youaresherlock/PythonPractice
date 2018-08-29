# -*- coding: utf-8 -*-
# @Author: xiweibo
# @Date:   2018-08-29 15:07:51
# @Last Modified by:   Clarence
# @Last Modified time: 2018-08-29 22:57:50
"""
python2实现xml解析 python3实现模块相同，与示例代码相同(除了print)
使用xml.dom解析xml
文件对象模型(document Object Model, 简称DOM),处理可拓展置标语言的标准编程接口
一个DOM的解析器在解析一个XML文档时，一次性读取整个文档，把文档中所有元素保存在内存中的一个树结构里，
之后可以利用DOM提供的不同的函数来读取或修改文档的内容和结构，也可以把修改过得内容写入xml
"""
import xml.dom.minidom

#使用minidom解析器打开XML文档
DOMTree = xml.dom.minidom.parse("movies.xml")
# Document.documentElement
# The one and only root element of the document.
# Element.hasAttribute(name)
# Returns true if the element has an attribute named by name.
collection = DOMTree.documentElement
if collection.hasAttribute("shelf"):
	print "Root element: %s" %(collection.getAttribute("shelf"))

# 在集合中获取所有电影
# Document.getElementsByTagName(tagName)
# Search for all descendants (direct children, children’s children, etc.) with a particular element type name.
movies = collection.getElementsByTagName("movie")

# 打印每部电影的详细信息
for movie in movies:
	print "*****Movie*****"
	if movie.hasAttribute("title"):
		print "Title: %s" %(movie.getAttribute("title"))

	movieType = movie.getElementsByTagName('type')[0]
	# Node.childNodes
	# A list of nodes contained within this node. This is a read-only attribute.
	print "Type: %s" % (movieType.childNodes[0].data)
	format = movie.getElementsByTagName('format')[0]
	print "Format: %s" %(format.childNodes[0].data)
	rating = movie.getElementsByTagName('rating')[0]
	print "Rating: %s" %(rating.childNodes[0].data)
	description = movie.getElementsByTagName('description')[0]
	print "Description: %s" %(description.childNodes[0].data)

