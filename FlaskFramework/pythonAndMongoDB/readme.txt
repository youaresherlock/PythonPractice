Python操作MongoDB
1. pymongo安装
2. 连接数据库
3. CURD

文档:
pypi: https://pypi.org/project/pymongo/
doc: http://api.mongodb.com/python/current/#

安装:
安装 pip install pymongo==3.8.0
查看pymongo版本, shell->import pymongo,pymongo.__version__


连接数据库:
方式一: 简写
client = MongoClient()
The above code will connect on the default host and port. We can also specify the host and port explicitly, as follows:
方式二: 指定端口和地址
client = MongoClient("localhost", 27017)
方式三: 使用URI  <scheme>://<user>:<password>@<host>:<port>/<path>;<params>?<query>#<fragment>
client = MongoClient("mongodb://localhost:27017/")


Web应用程序中的常见任务是从请求URL获取ObjectId并找到匹配的文档。
在这种情况下，必须将ObjectId从一个字符串转换到find_one()

from bson.objectid import ObjectId

# The web framework gets post_id from the URL and passes it as a string
def get(post_id):
    # Convert from string to ObjectId:
    document = client.db.collection.find_one({'_id': ObjectId(post_id)})



