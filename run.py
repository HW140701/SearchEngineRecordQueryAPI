# -*- coding:utf-8 -*-
'''
author:StubbornHuang
email:stubbornhuang@qq.com
site:www.stubbornhuang.com
LastUpdate:2020/01/19
'''

from flask import Flask, request

from BaiduRecordQuery import BaiduRecordQuery
from GoogleRecordQuery import GoogleRecordQuery
from BiYingRecordQuery import BiYingRecordQuery
from QiHu360RecordQuery import QiHu360RecordQuery
from SougouRecordQuery import SougouRecordQuery

app = Flask(__name__)

class SearchEngineRecordQuery:
    baiduRecordQuery = BaiduRecordQuery()
    googleRecordQuery = GoogleRecordQuery()
    biyingReordQuery = BiYingRecordQuery()
    qihu360RecordQuery = QiHu360RecordQuery()
    sougouRecordQuery = SougouRecordQuery()

searchEngineRecordQuery = SearchEngineRecordQuery()

# 百度收录查询接口
@app.route('/BaiduRecordQuery/',methods=['GET'])
def Baidu_Record_Query():
    url = request.args.get('url')
    return searchEngineRecordQuery.baiduRecordQuery.QueryUrl(url)

# Google收录查询接口
@app.route('/GoogleRecordQuery/',methods=['GET'])
def Google_Record_Query():
    url = request.args.get('url')
    return searchEngineRecordQuery.googleRecordQuery.QueryUrl(url)

# 必应收录查询接口
@app.route('/BiyingRecordQuery/',methods=['GET'])
def BiYing_Record_Query():
    url = request.args.get('url')
    return searchEngineRecordQuery.biyingReordQuery.QueryUrl(url)

# 360收录查询接口
@app.route('/360RecordQuery/',methods=['GET'])
def QiHu360_Record_Query():
    url = request.args.get('url')
    return searchEngineRecordQuery.qihu360RecordQuery.QueryUrl(url)

# 搜狗收录查询接口
@app.route('/SougouRecordQuery/',methods=['GET'])
def Sougou_Record_Query():
    url = request.args.get('url')
    return searchEngineRecordQuery.sougouRecordQuery.QueryUrl(url)

if __name__ == "__main__":
    app.run()