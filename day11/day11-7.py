# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     day11-7
   Description :
   Author :        Robert Xu
   date：          2020/1/26
-------------------------------------------------
   Change Activity:
                   2020/1/26:
-------------------------------------------------
"""
__author__ = 'Robert Xu'

import requests
import json


def main():
    resp = requests.get('http://api.tianapi.com/guonei/?key=APIKey&num=10')
    data_model = json.loads(resp.text)
    print(data_model['code'])


if __name__ == '__main__':
    main()
