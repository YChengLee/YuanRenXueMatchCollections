# -*- coding: utf-8 -*-
# @Python Version : Python3.6.5 x86_64
# @CreateTime     : 2021/6/12  21:58
# @Author         : liyc@hsmap.cn
# @File           : match13.py
# @Software       : PyCharm 2019.3
# @UpdateTime     : 
# @Describe       : 猿人学题12-入门级cookie
import re

import requests


def main():
    session = requests.session()
    headers = {
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'yuanrenxue.project',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Referer': 'http://match.yuanrenxue.com/match/13',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }
    response = session.get('http://match.yuanrenxue.com/match/13', headers=headers, verify=False)
    yuanrenxue_cookie = "".join(re.findall(r"\(\'(.)\'\)", response.text))
    k, v = tuple(yuanrenxue_cookie.split("="))
    session.cookies.update({k: v})
    result = 0
    for page in range(1, 6):
        response = session.get(f'http://match.yuanrenxue.com/api/match/13?page={page}', headers=headers, verify=False)
        # print(response.text)
        result += sum([i.get("value") for i in response.json().get("data")])
    print(result)

if __name__ == '__main__':
    main()
