#!usr/bin/python
# -*- coding:utf8 -*-
import requests


url = 'https://httpbin.org/post'

"""
request.request(method, url, **kwargs):
url: url for the new request object 
params: (optional)dictionary, list of tuples or bytes to send in the 
query string for the request 
data: (optional)dictionary, list of tuples or bytes to send int the
body of the request 
json: (option)a json serializable python object to send in the body of the 
request 
headers: (optional)dictionary of http headers to send with the request 

class requests.Response:
content: content of the response, in bytes 
encoding: encoding to decode with when accessing r.text 
text : content of the response, in unicode 
"""
response = requests.post(url, data={'username': 'clarence'})
print(response.json())
response.close()