# -*- coding: utf-8 -*-
# @Python Version : Python3.6.5 x86_64
# @CreateTime     : 2021/6/13  22:45
# @Author         : liyc@hsmap.cn
# @File           : match16.py
# @Software       : PyCharm 2019.3
# @UpdateTime     : 
# @Describe       : 猿人学题16 webpack初体验
import requests
import execjs
import time
from Utils.baseUtils import *


with open("anti_ast_btoa.js","r") as f:
    code = f.read()
    f.close()
ctx = execjs.compile(code)

def main():
    headers = {
        'authority': 'match.yuanrenxue.com',
        'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'x-requested-with': 'XMLHttpRequest',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'yuanrenxue.project',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://match.yuanrenxue.com/match/16',
        'accept-language': 'zh-CN,zh;q=0.9',
    }
    sum = 0
    for page in range(1,6):
        page = str(page)
        m, t = ctx.call("get_m")
        print(m, t)
        params = (
            ('page', str(page)),
            ('m', m),
            ('t', t),
        )
        response = request('https://match.yuanrenxue.com/api/match/16', headers=headers, params=params)
        print(response.text)

        data = response.json()
        for item in data.get("data"):
            sum+=item.get("value")
    print(sum)

if __name__ == '__main__':
    main()