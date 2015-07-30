#-*-coding:utf-8-*-
__author__ = 'xdy'

import hmac
import hashlib
import base64

TOKEN = "SecretKey"

def signature(data):
    return hmac.new(TOKEN, data, hashlib.sha1).hexdigest().encode("base64")


data = "appId=2882303761517239138&cpOrderId=9786bffc-996d-4553-aa33-f7e92c0b29d5&orderConsumeType=10&orderId=21140990160359583390&orderStatus=TRADE_SUCCESS&payFee=1&payTime=2014-09-05 15:20:27&productCode=com.demo_1&productCount=1&productName=银子1两&uid=100010"
result = signature(data)
print(result)
result = "1388720d978021c20aa885d9b3e1b70cec751496"
