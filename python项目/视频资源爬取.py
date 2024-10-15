import requests  
from bs4 import BeautifulSoup  

# 目标网页URL  
url = 'https://www.iqiyi.com/list/电视剧'  
  
# 发送HTTP请求  
response = requests.get(url)  
  
# 检查请求是否成功  
if response.status_code == 200:  
    # 使用BeautifulSoup解析HTML内容  
    soup = BeautifulSoup(response.text, 'html.parser')  
  
    # 找到所有的<p>标签并打印其内容  
    p_tags = soup.find_all('p')  
    for p in p_tags:  
        print(p.get_text(strip=True))  

    span_tags = soup.find_all('span') 
    for span in span_tags:  
        print(span.get_text(strip=True))  
    
    # 找到所有的<a>标签并打印其href属性  
    a_tags = soup.find_all('a')  
    for a in a_tags:  
        href = a.get('href')  
        if href:  
            print(href)  
else:  
    print(f'请求失败，状态码：{response.status_code}')
