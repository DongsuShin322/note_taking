import os
import sys
import http.client
from xml.dom.minidom import parseString

client_id = ""
client_secret = ""

conn = http.client.HTTPSConnection("openapi.naver.com")
headers = {"X-Naver-Client-Id":client_id, "X-Naver-Client-Secret":client_secret}
encText = "love"
params = "?query="+encText+"&display=10&start=1"

conn.request("GET", "/v1/search/book.xml"+params, None, headers)
res = conn.getresponse()

if int(res.status) == 200 :
    print (parseString(res.read().decode('utf-8')).toprettyxml())
else :
    print ("HTTP Request is failed :"+res.reason)
    print (res.read().decode('utf-8'))

conn.close()     
