# import re
# import requests
# m3u8_url = "https://muiplayer.js.org/media/media.m3u8"
# # 获取M3U8文件内容
# response = requests.get(m3u8_url)
# content = response.text
# # 解析M3U8文件，获取视频链接列表
# video_urls = [line.strip() for line in content.split('\n') if line and not line.startswith('#')]
# # 打印视频链接列表
# for url in video_urls:
#     print(url)
# 
# 
import re
import os
import requests

m3u8_url = "https://muiplayer.js.org/media/media.m3u8"
output_folder = "video_folder"
output_file = "output.ts"

# 获取M3U8文件内容
response = requests.get(m3u8_url)
content = response.text

# 解析M3U8文件，获取视频链接列表
video_urls = [line.strip() for line in content.split('\n') if line and not line.startswith('#')]

# 创建保存视频的文件夹
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 下载视频并保存
for index, url in enumerate(video_urls):
    response = requests.get(url)
    video_data = response.content
    video_filename = f"video_{index}.ts"
    video_filepath = os.path.join(output_folder, video_filename)
    with open(video_filepath, 'wb') as file:
        file.write(video_data)
    print(f"Downloaded video {index+1}/{len(video_urls)}")

# 合并为单个TS文件
output_filepath = os.path.join(output_folder, output_file)
with open(output_filepath, 'wb') as output_file:
    for index, url in enumerate(video_urls):
        video_filename = f"video_{index}.ts"
        video_filepath = os.path.join(output_folder, video_filename)
        with open(video_filepath, 'rb') as video_file:
            output_file.write(video_file.read())
        print(f"Merged video {index+1}/{len(video_urls)}")

# 删除临时的TS文件
for index, url in enumerate(video_urls):
    video_filename = f"video_{index}.ts"
    video_filepath = os.path.join(output_folder, video_filename)
    os.remove(video_filepath)

print("All videos downloaded, merged and temporary files deleted.")
