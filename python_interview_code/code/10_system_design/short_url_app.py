"""
短网址生成代码。Flask 演示
依赖本地 mysql 和 redis
"""
import os

from flask import Flask, jsonify, render_template, request
from flask_mysqldb import MySQL
from flask.ext.redis import FlaskRedis

app = Flask(__name__)
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASS') # export your password
app.config['MYSQL_DB'] = 'test'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)
redis_store = FlaskRedis(app)


CHARS = "abcdefghijkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ0123456789"

def encode(num):
    if num == 0:
        return CHARS[0]
    res = []
    while num:
        num, rem = divmod(num, len(CHARS))  # 62
        res.append(CHARS[rem])
    return ''.join(reversed(res))

@app.route('/shorten', methods=['POST'])
def shorten_url():
    long_url = request.json['url']
    index = int(redis_store.incr('SHORT_CNT'))
    token = encode(index)
    sql = "INSERT INTO short_url(token, url) VALUES(%s, %s)"
    cur = mysql.connection.cursor()
    cur.execute(sql, (token, long_url))
    mysql.connection.commit()
    short_url = 'https://short.com/' + token
    return jsonify(url=short_url)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=1)
