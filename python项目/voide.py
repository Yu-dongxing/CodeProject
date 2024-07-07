from email import header
import requests  
from bs4 import BeautifulSoup  
  
def fetch_download_list(url,headers):  
    
    # 发送GET请求到目标URL  
    response = requests.get(url,headers=headers)  
      
    # 确保请求成功  
    if response.status_code == 200:  
        # 使用BeautifulSoup解析HTML  
        soup = BeautifulSoup(response.text, 'html.parser')  
          
        # 查找ID为'download-list'的表格  
        download_list_table = soup.find('table')  
        title = soup.find('h2').text
          
        if download_list_table:  
            # 提取表格的所有行（<tr>）  
            rows = download_list_table.find_all('tr')  
              
            # 假设第一行是表头，我们将其单独处理  
            headers_row = rows[0]  
            head = [th.get_text(strip=True) for th in headers_row.find_all(['th', 'td'])]  # 使用['th', 'td']以处理没有<th>的情况  
              
            # 跳过表头行，处理数据行  
            data_rows = rows[1:]  
              
            # 存储每行的数据  
            data = []  
            for row in data_rows:  
                # 提取每行的列数据  
                cols = [td.get_text(strip=True) for td in row.find_all(['td', 'th'])]  # 同样，使用['td', 'th']以处理可能的异常  
                data.append(cols)  
              
            # 返回表头和数据  
            return head, data  ,title
        else:  
            print("未找到ID为'download-list'的表格")  
    else:  
        print(f"请求失败，状态码：{response.status_code}")  

def voide_url_play():
    print("we")

# 替换下面的URL为你需要请求的网站的URL  
url = 'https://www.yjys.top/guoju/24946.htm/'  
headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
}
# fetch_download_list(url)

table_headers,table_data,table_title= fetch_download_list(url,headers)  

if table_headers and table_data and table_title:  
    print(table_title)
    print("表头：", table_headers)  
    for row in table_data:  
        print("数据行：", row)  
else:  
    print("未能获取表格数据")