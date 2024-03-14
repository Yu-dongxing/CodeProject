import requests  
  
url = "https://mesh.if.iqiyi.com/portal/videolib/pcw/data?scale=150&channel_id=1&ret_num=100&page_id=1"  
classurl = "https://api.yuxs.top/class_id/index.json"
# 发送GET请求  
response = requests.get(classurl)  
  
# # 检查请求是否成功  
# if response.status_code == 200:  
#     # 解析JSON数据  
#     data_json = response.json()  
#     # 班级学生信息完整版数组
#     # 尝试获取data数组  
#     if 'data' in data_json:  
#         data_list = data_json['data']  
          
#         # 遍历data数组中的display_name字段  
#         for item in data_list:  
#             # if 'display_name' in item:  
#             print(item['display_name'], item['dq_updatestatus'],item['page_url'])

#     else:  
#         print("JSON数据中没有找到'data'字段")  
# else:  
#     print(f"请求失败，状态码：{response.status_code}")
if response.status_code==200:
    data_json = response.json()
    if 'classid' in data_json:
        data_list = data_json['classid']
        for item in data_list:
            print(item['STUID'],item['NAME'])
    else:
        print("error")
else:
    print("请求失败")
