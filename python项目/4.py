import requests  
  
url = "https://mesh.if.iqiyi.com/portal/videolib/pcw/data?scale=150&channel_id=1&ret_num=100&page_id=1"  
  
# 发送GET请求  
response = requests.get(url)  
  
# 检查请求是否成功  
if response.status_code == 200:  
    # 解析JSON数据  
    data_json = response.json()  
      
    # 尝试获取data数组  
    if 'data' in data_json:  
        data_list = data_json['data']  
          
        # 遍历data数组中的display_name字段  
        for item in data_list:  
            # if 'display_name' in item:  
            print(item['display_name'], item['dq_updatestatus'],item['page_url'])

    else:  
        print("JSON数据中没有找到'data'字段")  
else:  
    print(f"请求失败，状态码：{response.status_code}")