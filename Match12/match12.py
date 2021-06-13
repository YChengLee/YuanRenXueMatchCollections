# -*- coding: utf-8 -*-
# @Python Version : Python3.6.5 x86_64
# @CreateTime     : 2021/6/12  11:27
# @Author         : liyc@hsmap.cn
# @File           : match12.py
# @Software       : PyCharm 2019.3
# @UpdateTime     : 
# @Describe       : 猿人学题12 入门级JS

import base64

import requests


def main():
    result = 0
    for page in range(1, 6):
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'User-Agent': 'yuanrenxue.project',
            'X-Requested-With': 'XMLHttpRequest',
            'Referer': 'http://match.yuanrenxue.com/match/12',
            'Accept-Language': 'zh-CN,zh;q=0.9'
        }
        m = base64.b64encode(f"yuanrenxue{page}".encode())
        params = (
            ('page', str(page)),
            ('m', m),
        )

        response = requests.get('http://match.yuanrenxue.com/api/match/12', headers=headers, params=params,
                                verify=False)
        # print(response.json())
        result += sum([i.get("value") for i in response.json().get("data")])

    print(result)


if __name__ == '__main__':
    main()
