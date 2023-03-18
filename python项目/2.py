# python
import requests

# 图片链接列表
img_urls = [
    'https://www.example.com/image1.jpg',
    'https://www.example.com/image2.jpg',
    'https://www.example.com/image3.jpg',
    'https://www.example.com/image4.jpg',
    'https://www.example.com/image5.jpg'
]

# 遍历图片链接列表，依次下载图片
for i, img_url in enumerate(img_urls):
    response = requests.get(img_url)
    filename = f'image{i+1}.jpg'
    with open(filename, 'wb') as f:
        f.write(response.content)
    print(f'{filename} 下载完成')

# import requests

# 读取txt文件中的链接
#with open('links.txt', 'r') as f:
 #   links = f.readlines()

# 遍历链接列表，依次下载链接指向的文件
#for i, link in enumerate(links):
 #   response = requests.get(link.strip())
  #  filename = f'file{i+1}.txt'
   # with open(filename, 'wb') as f:
    #    f.write(response.content)
   # print(f'{filename} 下载完成')