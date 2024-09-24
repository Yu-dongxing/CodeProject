import requests
from lxml import etree
import pandas as pd
# 保存的excel文件名
excelFileName = 'douban_movies_top250.xlsx'
# 请求头
headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0"}
# 
def clean_text(text):
    # 替换 / 和 /\xa0 为逗号
    return text.replace('/\xa0', ',').replace('/', ',')
# 字符串过滤-1
def clean_text_1(text):
# 确保 text 是一个字符串
    if isinstance(text, list):
        text = ' '.join(text)  # 将列表元素用空格连接成字符串
    else:
        text = str(text)  # 将其他类型转换为字符串
    tt = text.replace('[', ' ').replace(']', ' ')
    return tt.strip()
# 字符串过滤-1-首字段
def get_first_text(list_of_elements):
    try:
        return list_of_elements[0].strip() if list_of_elements else ""
    except:
        return ""
# 创建空excel文件
def create_empty_excel(filename):
    df = pd.DataFrame()
    with pd.ExcelWriter(filename, engine='openpyxl') as writer:
        df.to_excel(writer, index=False)
# 电影详情页面信息获取
def link_get(url):
    try:
        res = requests.get(url, headers=headers)
        res.raise_for_status()  # 检查请求是否成功
        text = res.text
        parser = etree.HTMLParser(encoding='utf-8')  # 指定编码
        tree = etree.fromstring(text, parser)
        # 
        anot = tree.xpath("//span[@class='pl' and text()='导演']/following-sibling::span[@class='attrs']//a/text()")
        bj = tree.xpath("//span[@class='pl' and text()='编剧']/following-sibling::span[@class='attrs']//a/text()")
        zy = tree.xpath("//span[@class='pl' and text()='主演']/following-sibling::span[@class='attrs']//a/text()")
        lx = tree.xpath('//span[@property="v:genre"]/text()')
        duration_xpath = '//span[@property="v:runtime"]/text()'
        language_xpath = '//span[@property="v:initialReleaseDate"]/text()'
        desc =tree.xpath('//span[@property="v:summary"]//text()')
        pc = get_first_text(tree.xpath(duration_xpath))
        syrq = get_first_text(tree.xpath(language_xpath))
        # print(desc) #调试-2
        return anot,bj,zy,pc,syrq,lx,desc
    except requests.RequestException as e:
        print(f"请求错误: {e}")
    except etree.XMLSyntaxError as e:
        print(f"解析错误: {e}")
    except Exception as e:
        print(f"其他错误: {e}")

def start():
    create_empty_excel(excelFileName)  # 创建一个空的Excel文件
    data_list = []  # 用于存储所有电影数据的列表
    for i in range(0, 250, 25):
        url = 'https://movie.douban.com/top250?start=' + str(i) + '&filter='
        response = requests.get(url, headers=headers)
        text = response.text
        # 解析HTML
        parser = etree.HTMLParser()
        tree = etree.fromstring(text, parser)
        # 找到所有电影项
        items = tree.xpath('//div[@class="item"]')
        for item in items:
            # 提取电影信息
            rank = item.xpath('.//div[@class="pic"]//em/text()')
            image_url = item.xpath('.//div[@class="pic"]//img/@src')
            link = item.xpath('.//div[@class="pic"]//a/@href')
            title = item.xpath('.//div[@class="info"]//span[@class="title"]/text()')
            other_info = item.xpath('.//div[@class="info"]//span[@class="other"]/text()')
            rating = item.xpath('.//span[@class="rating_num"]/text()')
            anot,bj,zy,pc,syrq,lx,desc= link_get(link[0]) if link else None
            # print(link[0])
            #print(anot,bj,zy,pc,syrq,lx,laun) #调试-1
            # 检查是否找到信息并构建字典
            if rank and image_url  and title and rating and anot and bj and zy and pc and syrq and lx  and desc:
                rank = rank[0]
                image_url = image_url[0] if image_url else ''
                title = title[0] if title else ''
                other_info = other_info[0] if other_info else ''
                rating = rating[0] if rating else ''
                dic = {
                    # '电影名称': clean_text_1(clean_text(title + '' + other_info.strip())),
                    '电影名称': clean_text_1(clean_text(title)),
                    '链接':clean_text_1(link),
                    '电影图片': image_url,
                    '导演': clean_text_1(anot),
                    '编剧':clean_text_1(bj),
                    '主演':clean_text_1(zy),
                    '片长':pc,
                    '类型':clean_text_1(lx),
                    '评分': rating + '分',
                    '排名': rank,
                    '上映日期':syrq,
                    '简介':clean_text_1(desc)
                }
                # print(clean_text_1(clean_text(title)))
                data_list.append(dic)  # 将字典添加到列表中
                if data_list:
                    df = pd.DataFrame(data_list)
                    with pd.ExcelWriter(excelFileName, mode='a', engine='openpyxl', if_sheet_exists='overlay') as writer:
                        df.to_excel(writer, index=False)
                        print((clean_text(title))+"已保存到Excel文件中。")
                # print(dic)

if __name__ == '__main__':
    start()

