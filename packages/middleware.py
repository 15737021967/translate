#!/usr/bin/python3
# -*- coding: utf-8 -*- 
# @Time : 2019/3/2 10:28 
# @Author : Tan 
# @Email : 1531391246@qq.com
# @File : middleware.py
# @Software: PyCharm

import requests
import time
import random
import hashlib


class Translate:
    def __init__(self, froms, to, words):
        self.froms = froms
        self.to = to
        self.words = words

    def get_translate(self):
        path = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
        cookie_url = "http://fanyi.youdao.com/"
        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Content-Length": "264",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Cookie": 'OUTFOX_SEARCH_USER_ID_NCOO=1740805400.2970326; OUTFOX_SEARCH_USER_ID="1604896103@10.168.11.144"; P_INFO=15737029167|1556459610|2|epay|00&99|null&null&null#hen&410400#10#0#0|&0|null|15737029167; _ga=GA1.2.226816585.1556460811; JSESSIONID=aaa913p2IYtjCcdA0-WQw; ___rl__test__cookies=1557806201620',
            "Host": "fanyi.youdao.com",
            "Origin": "http://fanyi.youdao.com",
            "Referer": "http://fanyi.youdao.com/",
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Mobile Safari/537.36",
            'X-Requested-With': 'XMLHttpRequest',
        }
        user_agent = "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Mobile Safari/537.36"

        session = requests.Session()
        session.headers.update(headers)
        u = 'fanyideskweb'
        f = str(int(time.time() * 1000 + random.randint(1, 10)))
        c = '@6f#X3=cCuncYssPsuRUE'
        sign = hashlib.md5((u + self.words + f + c).encode('utf-8')).hexdigest()
        Form_Data = {
            'i': self.words,
            'from': self.froms,
            'to': self.to,
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': f,
            'sign': sign,
            'ts': '1557804639198',
            'bv': '33a62fdcf6913d2da91495dad54778d1',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_CLICKBUTTION',
        }
        try:
            response = session.post(path, data=Form_Data)
            res = response.json()
            resword = res['translateResult'][0][0]['tgt']

        except:
            resword = ''
        return resword


