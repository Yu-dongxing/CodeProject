# import os  
# import requests  
# import json  
  
# # 假设data变量包含了你提供的JSON数据  
# data = [  
#     {
#             "title": "天行健",
#             "desc": "秦俊杰刘宇宁寻宝",
#             "showdate": "2024-5-8",
#             "hp_img_url": "http://pic5.iqiyipic.com/image/20240508/6c/87/a_100573575_m_601_m8_592_333.webp",
#             "img_url": "https://pic5.iqiyipic.com/image/20240508/6c/87/a_100573575_m_601_m8_579_772.webp",
#             "page_url": "https://www.iqiyi.com/v_1hvxbrsdlj8.html",
#             "description": "晚清末年，深宫之中，文渊阁里净坛密藏宝图失窃，为争夺这份几乎能改天换地的宝藏，各方势力蠢蠢欲动。身份各异的一行人卷入一场离奇的寻宝之旅，并在恢弘激荡的历史浪潮中，逐步坚定救国的理想。"
#         },
#         {
#             "title": "不可告人",
#             "desc": "欧豪李一桐探寻真相",
#             "showdate": "2024-5-8",
#             "hp_img_url": "http://pic2.iqiyipic.com/image/20240508/77/2f/a_100545294_m_601_m9_592_333.webp",
#             "img_url": "https://pic2.iqiyipic.com/image/20240508/77/2f/a_100545294_m_601_m9_579_772.webp",
#             "page_url": "https://www.iqiyi.com/v_1snwv9tqxvg.html",
#             "description": "一次既成功又失败的抓捕行动，改变了所有人的命运，痛苦中的等待意味着从未放弃，而那些不可告人的罪恶也在伺机重来，这一次，是正与邪之间最终的较量！"
#         }  
# ]  
  
# # 遍历data列表中的每个字典  
# for item in data:  
#     # 创建标题命名的文件夹（如果尚不存在）  
#     title = item['title']  
#     folder_path = os.path.join('./IMG', title)  # 假设在当前目录下创建文件夹  
#     if not os.path.exists(folder_path):  
#         os.makedirs(folder_path)  
      
#     # 下载图片并保存到对应的文件夹中  
#     img_url = item['img_url']  
#     img_filename = os.path.join(folder_path, f"{title}.webp")  # 使用title作为文件名  
#     response = requests.get(img_url, stream=True)  
      
#     if response.status_code == 200:  
#         with open(img_filename, 'wb') as f:  
#             for chunk in response.iter_content(1024):  
#                 f.write(chunk)  
#     else:  
#         print(f"Failed to download {img_url}, status code: {response.status_code}")  
  
# # 如果你的data是从JSON字符串或文件中读取的，你可能需要先解析它  
# # 例如：  
# # json_data = '''你的JSON字符串'''  
# # data = json.loads(json_data)  
# # 或者从文件中读取  
# # with open('data.json', 'r') as f:  
# #     data = json.load(f)
import requests  
import json  
import os
  
def fetch_data_from_iqiyi():  
    
    url="http://192.168.0.101:4545/arr"
    #url = "https://mesh.if.iqiyi.com/portal/videolib/pcw/data?scale=150&channel_id=2&ret_num=60&page_id=1&market_release_date_level=2024"  
    headers = {  
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0',  # 替换为你的 User-Agent，这有助于避免被服务器拒绝  
        # 可以添加其他必要的 headers  
    }  
      
    try:  
        response = requests.get(url, headers=headers)  
        response.raise_for_status()  # 如果请求失败，这里会抛出异常  
        data = response.json()  # 将响应内容解析为 JSON 格式  
        return data['data']
    except requests.RequestException as e:  
        print(f"请求失败: {e}")  
        return None  
    except json.JSONDecodeError as e:  
        print(f"解析 JSON 失败: {e}")  
        return None  
  
# 调用函数并打印返回的数据  
data = fetch_data_from_iqiyi()  
#if data:  
#    print(json.dumps(data, indent=4))  # 以格式化的方式打印 JSON 数据
# 遍历data列表中的每个字典  
for item in data:  
    # 创建标题命名的文件夹（如果尚不存在）  
    title = item['title']  
    folder_path = os.path.join('./IMG', title)  # 假设在当前目录下创建文件夹  
    if not os.path.exists(folder_path):  
        os.makedirs(folder_path)  
      
    # 下载图片并保存到对应的文件夹中  
    img_url = item['img_url']  
    img_filename = os.path.join(folder_path, f"{title}.webp")  # 使用title作为文件名  
    response = requests.get(img_url, stream=True)  
      
    if response.status_code == 200:  
        with open(img_filename, 'wb') as f:  
            for chunk in response.iter_content(1024):  
                f.write(chunk)  
    else:  
        print(f"Failed to download {img_url}, status code: {response.status_code}") 
