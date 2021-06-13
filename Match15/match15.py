# -*- coding: utf-8 -*-
# @Python Version : Python3.6.5 x86_64
# @CreateTime     : 2021/6/13  20:37
# @Author         : liyc@hsmap.cn
# @File           : match15.py
# @Software       : PyCharm 2019.3
# @UpdateTime     : 
# @Describe       : 猿人学题15 备周则意怠-常见则不疑

import time

import pywasm
import requests

wasm = pywasm.load("main.wasm")


def get_m():
    t1 = int(time.time() / 2)
    t2 = t1 - 17
    sign = wasm.exec("encode", [t1, t2])
    m = f"{sign}|{t1}|{t2}"
    return m


def main():
    headers = {
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'User-Agent': 'yuanrenxue.project',
        'X-Requested-With': 'XMLHttpRequest',
        'Referer': 'http://match.yuanrenxue.com/match/15',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    }
    result = 0
    for page in range(1, 6):
        params = (
            ('m', get_m()),
            ('page', str(page)),
        )
        response = requests.get('http://match.yuanrenxue.com/api/match/15', headers=headers, params=params,
                                verify=False)
        result += sum([i.get("value") for i in response.json().get("data")])
    print(result)


if __name__ == '__main__':
    main()
