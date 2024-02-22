import re
import requests
m3u8_url = "https://muiplayer.js.org/media/media.m3u8"
# 获取M3U8文件内容
response = requests.get(m3u8_url)
content = response.text
# 解析M3U8文件，获取视频链接列表
video_urls = [line.strip() for line in content.split('\n') if line and not line.startswith('#')]
# 打印视频链接列表
for url in video_urls:
    print(url)
# 
# 
