import json
import requests
from lxml import etree
import pandas as pd
import time
import os
# 保存的excel文件名
excelFileName = 'dy.xlsx'
link_url='http://bbs.zgogc.com/2048'
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
    response = requests.get(url,headers)
    if response.status_code == 200:
        parser = etree.HTMLParser()
        tree = etree.fromstring(response.text, parser)
        # 使用 XPath 提取不包含广告的所有主题行
        threads = tree.xpath('.//*[@id="main"]/div[10]/div[1]')
        # Use XPath to find all tr elements with class "tr3 t_one"
        tr_elements = tree.xpath(".//table[@id='ajaxtable']//tr[@class='tr3 t_one']")
        
        # Iterate over each row and extract data
        for tr in threads:
            title = tr.xpath("./div[1]/div/a[1]/div[3]/span")
            link = tr.xpath(".//td[2]//a[@class='subject']/@href")
            author = tr.xpath(".//td[3]//a[@class='bl']/text()")
            replies = tr.xpath(".//td[4]//span[@class='s3']/text()")
            last_post = tr.xpath(".//td[5]//span[@class='f10 gray']/text()")
            
            link = link[0] if link else 'N/A'  # 如果没有链接，返回 'N/A'

            print(f"Title: {title[0] if title else 'N/A'}")
            print(f"Link: {link}")
            print(f"Author: {author[0] if author else 'N/A'}")
            print(f"Replies: {replies[0] if replies else 'N/A'}")
            print(f"Last Post: {last_post[0] if last_post else 'N/A'}")
            print('-' * 40)
    else:
        print("Failed to retrieve data")

# 函数用于将数据保存到Excel文件中
def save_to_excel(data, filename):

    df = pd.DataFrame(data, columns=['Content'])
    df.to_excel(filename, index=False)

# 主函数
def main():
    for i in range(1,3):
        # http://bbs.zgogc.com/thread.php?fid=291&woo=51cg1&po=L2NhdGVnb3J5L3dwY3ove3BhZ2V9Lw&page=3#c  thread.php?fid=291&page=1
        base_url = link_url+"/thread.php?fid=291&page="+str(i)
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