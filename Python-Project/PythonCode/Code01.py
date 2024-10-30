# Copyright (C) 2024 YUXS, Inc. All Rights Reserved 
#
# @Time    : 2024.9.18-13:35
# @Author  : YuDongXing
# @Email   : yuxs2022@163.com
# @File    : Code01.py
#
import requests

def Code01(a,b):
    print(f"a为{a},b为{b}")
    print(f"加法: {a + b}")
    print(f"减法: {a - b}")
    print(f"乘法: {a * b}")
    print(f"除法: {a / b}")
    print(f"取整: {a // b}")
    print(f"取余: {a % b}")
    print(f"乘方: {a ** b}")

def Code02(title,desc):
    url = "https://sctapi.ftqq.com/SCT257998Tio5v9YePkynyKL5SHXT5Cmgo.send"
    payload={
        'title': title,
        'desp': desc
    }
    files=[]
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
    }
    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    print(response.text)

if __name__ == '__main__':
    # Code01(4,8)
    Code02("测试2","wqeqe")