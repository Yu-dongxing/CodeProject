import requests
from logger import Logger


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
    # print(response.text)
    # Logger.info(response.text)