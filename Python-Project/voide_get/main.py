import json
import requests
from lxml import etree
import pandas as pd
import time
import os
# 保存的excel文件名
excelFileName = 'dy.xlsx'
link_url='https://bbs.zgogc.com/2048'
# https://bbs.zgogc.com/2048/
# https://bbs.zgogc.com/2048/thread.php?fid=15&page=1
# 传入fid为15，pageid为0-112页面，传入页面提取数据，数据保存的excel文件中
# 请求头
headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0"}
# 

import requests
from lxml import etree

def fetch_data(url):
    response = requests.get(url, headers=headers)
    print(response)
    if response.status_code == 200:
        parser = etree.HTMLParser()  # 创建HTML解析器
        tree = etree.fromstring(response.text, parser)  # 使用解析器解析文本
        # 使用XPath查找特定的tr元素
        tr_elements = tree.xpath(".//div[@class='t z']/table[@id='ajaxtable']/table[2]/tr[@class='tr3 t_one']")
        print(tr_elements)
    else:
        return "Failed to retrieve data"  # 如果状态码不是200，返回错误信息

# 函数用于将数据保存到Excel文件中
def save_to_excel(data, filename):

    df = pd.DataFrame(data, columns=['Content'])
    df.to_excel(filename, index=False)

# 主函数
def main():
    for i in range(1,3):
        base_url = link_url+"/thread.php?fid=15&page="+str(i)
        print(base_url)
        data = fetch_data(base_url)
        # if data is not None and len(data) > 0:
        print(data)
        # print(base_url)
    
    # 创建一个空的DataFrame用于存储所有数据
    # all_data = pd.DataFrame(columns=['Content'])
    
    # for pageid in range(0, 113):
    #     page_url = base_url + str(pageid)
    #     data = fetch_data(page_url)
    #     if data:
    #         # 将提取的数据添加到DataFrame中
    #         df = pd.DataFrame(data, columns=['Content'])
    #         all_data = pd.concat([all_data, df], ignore_index=True)
    
    # # 将所有数据保存到Excel文件中
    # save_to_excel(all_data, 'output.xlsx')

if __name__ == "__main__":
    main()