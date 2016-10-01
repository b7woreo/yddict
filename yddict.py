#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from urllib import request
from urllib import parse
import os
import sys

class yddict(object):
    base_url = "http://fanyi.youdao.com/openapi.do?keyfrom=%s&key=%s&type=data&doctype=json&version=1.1&q=%s"
    error = {0:'正常', 20:'要翻译的文本过长',30:'无法进行有效的翻译',40:'不支持的语言类型',50:'无效的key',60:'无词典结果，仅在获取词典结果生效'}
    
    def __init__(self, keyfrom, key):
        self.keyfrom = keyfrom
        self.key = key

    def query(self,txt):
        query_url = yddict.base_url % (self.keyfrom, self.key, parse.quote(txt)) 
        result = request.urlopen(query_url).read().decode('utf-8')
        return json.loads(result)

def read_config():
    try:
        config = open('%s/config.json' % os.path.dirname(__file__), encoding='utf-8').read()
        config = json.loads(config)
        return config['keyfrom'], config['key']
    except:
        print('\n错误：\nconfig.json 不存在或有误')
        sys.exit(0)

def read_txt():
    try:
        return sys.argv[1]
    except:
        print('\n错误：\n翻译单词为空')
        sys.exit(0)
  
def print_result(result):
    print()
    errorCode = result.get('errorCode')
    if errorCode != 0:
        print('错误：')
        print(yddict.error.get(errorCode))
        return
    
    basic = result.get('basic')
    if not basic:
        print('翻译：')
        for translation in result.get('translation'):
            print(translation)
    else:
        print('释义：')
        for explain in basic.get('explains'):
            print(explain) 
    
if __name__ == '__main__':
    keyfrom, key = read_config()
    yd = yddict(keyfrom, key)
    
    txt = read_txt()
    result = yd.query(txt)
    print_result(result)
