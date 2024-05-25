import requests  
import json  
  
def fetch_data_from_iqiyi():  
    url = "https://mesh.if.iqiyi.com/portal/videolib/pcw/data?scale=150&channel_id=2&ret_num=60&page_id=1&market_release_date_level=2024"  
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
if data:  
    print(json.dumps(data, indent=4))  # 以格式化的方式打印 JSON 数据