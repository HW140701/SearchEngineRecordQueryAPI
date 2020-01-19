# -*- coding:utf-8 -*-
'''
author:StubbornHuang
email:stubbornhuang@qq.com
LastUpdate:2020/01/19
'''

from flask import Flask, request
import BaiduRecordQuery

baidu = BaiduRecordQuery()

app = Flask(__name__)

@app.route('/BaiduRecordQuery/',methods=['GET'])
def Baidu_Record_Query():
    url = request.args.get('url')
    return url

if __name__ == "__main__":
    app.run()