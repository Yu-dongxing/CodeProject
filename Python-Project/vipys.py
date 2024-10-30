import json
import requests
from lxml import etree
import pandas as pd
import time
import os

# 保存的excel文件名
excelFileName = 'dy.xlsx'
link_url='https://www.yjys.top'

# 请求头
headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0"}
# 
def clean_text(text):
    # 替换 / 和 /\xa0 为逗号
    return text.replace('/\xa0', ',').replace('/', ',')

def clean_text_d(text):
    # 替换 
    return text.replace("'", ',').replace('/', ',')

# 字符串过滤-1
def clean_text_1(text):
# 确保 text 是一个字符串
    if isinstance(text, list):
        text = ' '.join(text)  # 将列表元素用空格连接成字符串
    else:
        text = str(text)  # 将其他类型转换为字符串
    tt = text.replace('[', ' ').replace("'", ' ').replace("'", ' ').replace(']', ' ')
    return tt.strip()


# 字符串过滤-1-首字段
def get_first_text(list_of_elements):
    try:
        return list_of_elements[0].strip() if list_of_elements else ""
    except:
        return ""
    

def fg_link(link):
    # 分割URL
    parts =  str(link).split(';')
    # 取第一个部分，即不含jsessionid的部分
    return parts[0]


# 创建空excel文件
def create_empty_excel(filename):
    # 检查文件是否存在
    if os.path.exists(filename):
        # 如果文件存在，则删除原文件
        os.remove(filename)
    # 创建一个空的DataFrame
    df = pd.DataFrame()
    # 使用ExcelWriter写入空的DataFrame到Excel文件
    with pd.ExcelWriter(filename, engine='openpyxl') as writer:
        df.to_excel(writer, index=False)

def down_link_get(items):
    for item in items:
        rank = item.xpath("//tr[td/input[@name='check-download']]/td[2]/text()")
        link = item.xpath("//tr[td/input[@name='check-download']]/td[3]/a/@href")
    return rank,link

def link_get(url):
    # 初始化一个全局字典来存储所有下载信息
    all_downloads = []  
    all_play_list = []
    all_tor_list=[]

    try:
        res = requests.get(url, headers=headers)
        res.raise_for_status()  # 检查请求是否成功
        text = res.text
        parser = etree.HTMLParser(encoding='utf-8')  # 指定编码
        tree = etree.fromstring(text, parser)
        dy=tree.xpath(".//p[strong='导演：']/a/text()")
        bj=tree.xpath(".//p[strong='编剧：']/a/text()")
        zy=tree.xpath(".//p[strong='主演：']/a/text()")
        lx=tree.xpath(".//p[strong='类型：']/a/text()")
        gj=tree.xpath(".//p[strong='制片国家/地区：']/text()")
        laun=tree.xpath(".//p[strong='语言：']/text()")
        jj=tree.xpath(".//p[strong='集数：']/text()")
        sc=tree.xpath(".//p[strong='单集片长：']/text()")
        desc=tree.xpath('.//div[@id="synopsis"]//div[@class="card"]//div[@class="card-body"]/text()')
        # 找到下载链接项
        downs = tree.xpath('.//tbody[@id="download-list"]/tr')
        for down in downs:
            js = down.xpath(".//td[2]/text()")
            lj = down.xpath(".//td[3]/a/@href")
            for i in range(len(js)):
                    down_data={
                        "剧集":js[i],
                        "链接":lj[i]
                    }
                    all_downloads.append(down_data)
        all_down_json=json.dumps(all_downloads, ensure_ascii=False, indent=4)
        # 找到播放列表项
        plays = tree.xpath('.//div[@id="play-list"]//div[@class="d-flex"]/a')
        for play in plays:
            js = play.xpath("./text()")
            lj = play.xpath("./@href")
            for i in range(len(js)):
                    play_data={
                        "剧集":js[i],
                        "链接":link_url+lj[i]
                    }
                    all_play_list.append(play_data)
        all_play_json=json.dumps(all_play_list, ensure_ascii=False, indent=4)
        # 找到种子链接文件
        torrents = tree.xpath('.//div[@id="torrent-list"]/ul[@class="list-group scroll-y"]/li/div[@class="row align-items-center"]')
        for torrent in torrents:
            tor_link = torrent.xpath('.//div[@class="col"]/a/@href')
            tor_name = torrent.xpath('.//div[@class="col"]/a/code/text()')
            tor_size = torrent.xpath(".//div[@class='col-auto'][1]/code[@class='text-muted']/text()")
            tor_time = torrent.xpath(".//div[@class='col-auto'][2]/code[@class='text-muted']/text()")
            for i in range(len(tor_link)):
                    tor_data = {
                        "链接":link_url+tor_link[i],
                        "文件名":tor_name[i],
                        "文件大小":tor_size[i],
                        "文件日期":tor_time[i]
                    }
                    all_tor_list.append(tor_data)  # 使用列表来存储每个data字典
        all_tor_json=json.dumps(all_tor_list, ensure_ascii=False, indent=4)
        # print(all_tor_json)
        return dy,bj,zy,lx,gj,laun,jj,sc,all_down_json,all_play_json,desc,all_tor_json
    except requests.RequestException as e:
        print(f"请求错误: {e}")
    except etree.XMLSyntaxError as e:
        print(f"解析错误: {e}")
    except Exception as e:
        print(f"其他错误: {e}")

def start():
    # a=0
    batch_size = 50  # 定义批量大小
    create_empty_excel(excelFileName)  # 创建一个空的Excel文件
    data_list = []  # 用于存储所有电影数据的列表
    data_down_list = {}
    data_play_list = {}
    data_tor_list={}
    
    for i in range(1, 790):
        dsj_url = 'https://www.yjys.top/s/juqing/' + str(i)
        dy_url = 'https://www.yjys.top/s/all/'+str(i)+'?type=0'
        # 电影https://www.yjys.top/s/all?type=0   795
        response = requests.get(dy_url, headers=headers)
        text = response.text
        # 解析HTML
        parser = etree.HTMLParser()
        tree = etree.fromstring(text, parser)
        # 找到所有电影项
        items = tree.xpath('//div[@class="col-lg-8 col-4"]')
        for item  in items:
            # 提取电影信息
            title = item.xpath(".//div[@class='card card-sm card-link']//h3[@class='mb-0 card-title text-truncate']/text()")
            img_url = item.xpath(".//div[@class='card card-sm card-link']//a//img/@src")
            link = item.xpath(".//div[@class='card card-sm card-link']//a/@href")
            fb_data=item.xpath(".//div[@class='card-body p-2']//p[@class='mb-0 text-muted']/text()")
            update_js=item.xpath(".//span[@class='badge bg-pink position-absolute top-0 start-0 text-red-fg']/text()")
            vid = int(time.time())
            result=link_get(link_url+clean_text_1(fg_link(link)))
            if result is None:
                print("Error: link_get function returned None")
            else:
                dy,bj,zy,lx,gj,laun,jj,sc,data_down_list,data_play_list,desc,data_tor_list = result
            # 检查是否找到信息并构建字典
            if title and img_url and link :
                dic = {
                    'vid':vid,
                    '电影名称': clean_text_1(title),
                    '简介':clean_text_1(desc),
                    '链接':link_url+clean_text_1(fg_link(link)),
                    '电影图片': clean_text_1(img_url),
                    '发布日期':clean_text_1(fb_data),
                    '最近更新':clean_text_1(update_js),
                    '导演': clean_text_1(dy),
                    '编剧':clean_text_1(bj),
                    '主演':clean_text_1(zy),
                    '片长':clean_text_1(sc),
                    '类型':clean_text_1(lx),
                    '剧集':clean_text_1(jj),
                    '国家':clean_text_1(gj),
                    '语言':clean_text_1(laun),
                    '播放链接':data_play_list,
                    '剧集下载链接':data_down_list,
                    '种子链接':data_tor_list
                }
                # 将字典添加到列表中
                # print(dic)
                data_list.append(dic)  
                # 打印当前列表长度
                # print("已获取第"+str(len(data_list))+"个，达到50重新计数")
                # 如果列表中有数据
                if len(data_list) >= batch_size:
                    # 将列表转换为DataFrame
                    df = pd.DataFrame(data_list)
                    # 读取现有的Excel文件
                    try:
                        existing_df = pd.read_excel(excelFileName, engine='openpyxl')
                    except FileNotFoundError:
                        # 如果文件不存在，创建一个新的DataFrame
                        existing_df = pd.DataFrame()
                    # 将新数据追加到现有数据后面
                    new_df = pd.concat([existing_df, df], ignore_index=True)
                    # 使用ExcelWriter写入数据，如果sheet存在则追加
                    with pd.ExcelWriter(excelFileName, mode='a', engine='openpyxl', if_sheet_exists='overlay') as writer:
                        new_df.to_excel(writer, index=False)
                    # 打印保存信息
                    print("50个数据已保存到Excel文件中,当前第" + str(i) + "页。")
                    data_list = []  # 清空列表
                    data_down_list = {}
                    data_play_list = {}
                    data_tor_list={}
                    # print("list数据清除")

if __name__ == '__main__':
    start()

