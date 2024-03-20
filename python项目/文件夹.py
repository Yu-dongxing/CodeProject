import os
from datetime import datetime, timedelta

# 定义要创建的文件夹数量
num_folders = 5

# 指定要创建文件夹的目录路径
base_path = 'D:\桌面\新建文件夹'  # 将此处替换为你想要创建文件夹的目录路径

# 初始日期
start_date = datetime.strptime('3-18', '%m-%d')

# 遍历指定数量的文件夹并创建
for i in range(1, num_folders + 1):
    
    # 计算日期
    folder_date = start_date + timedelta(days=i-1)
    folder_name = f'计算机235查寝情况_{folder_date.strftime("%m-%d")}'  # 生成文件夹名称
    
    folder_path = os.path.join(base_path, folder_name)
    
    try:
        os.mkdir(folder_path)
        print(f"文件夹 {folder_path} 创建成功！")
    except FileExistsError:
        print(f"文件夹 {folder_path} 已经存在！")
