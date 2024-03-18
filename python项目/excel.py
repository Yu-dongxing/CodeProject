# import pandas as pd
# import glob

# # 获取所有Excel文件的文件名
# excel_files = glob.glob('D:/桌面/学校文件/计算机235查寝情况/*.xlsx')

# # 循环读取每个Excel文件的表格内容
# for file in excel_files:
#     print(f"Processing file: {file}")
    
#     # 读取Excel文件
#     df = pd.read_excel(file)
    
#     # 选择指定单元格范围的数据
#     selected_data = df.iloc[2:14, 4]   # iloc[行范围, 列范围]
    
#     # 打印选定的数据
#     print(selected_data)
    
#     # 在这里可以对表格内容进行处理，如修改、筛选等操作
    
#     # 处理后保存文件（可选）
#     # df.to_excel('path/to/save/processed/file.xlsx', index=False)

# import pandas as pd
# import glob

# # 获取所有Excel文件的文件名
# excel_files = glob.glob('D:/桌面/学校文件/计算机235查寝情况/*.xlsx')

# # 循环读取每个Excel文件的表格内容
# for file in excel_files:
#     print(f"Processing file: {file}")

#     # 读取Excel文件
#     df = pd.read_excel(file)

#     # 选择指定单元格范围的数据
#     selected_data = df.iloc[2:14, 4]  # iloc[行范围, 列范围]

#     # 打印选定的数据
#     print(selected_data)

#     # # 获取用户输入的数据
#     # user_input = input("请输入要修改的数据：")

#     # # 将用户输入的值赋给选定的单元格
#     # df.iloc[2:14, 4] = user_input
#     # 循环逐行获取用户输入的数据并赋值给DataFrame
#     for i in range(1, 14):  # 遍历行索引从2到14（不包括14）
#         user_input = input(f"请输入第{i}行要修改的数据：")
#         df.iloc[i, 4] = user_input  # 将用户输入的值赋给选定的单元格


#     # 打印修改后的数据
#     print(df.iloc[2:14, 4])
#     # 保存当前文件
#     df.to_excel(file, index=False)
#     print(f"处理后的数据已保存至 {file}")

#     # 在这里可以对表格内容进行其他处理

#     # 处理后保存文件（可选）
#     # df.to_excel('path/to/save/processed/file.xlsx', index=False)

import pandas as pd
from openpyxl import load_workbook
import glob
file_url=""
while(1):
    file_url=input(f"请输入excel文件列表地址(例如：D:/桌面/学校文件/计算机235查寝情况)：")

    # 获取所有Excel文件的文件名
    excel_files = glob.glob(file_url+"\*.xlsx")

    # 循环读取每个Excel文件的表格内容
    for file in excel_files:
        print(f"文件名称为: {file}")
        # 读取Excel文件
        wb = load_workbook(file)
        sheet = wb.active

        for i in range(3, 16):  # 遍历行索引从3到15（不包括15）
            user_input = input(f"请输入第{i}行要修改的数据：")
            try:
                user_input = int(user_input)  # 将用户输入的内容转换为浮点数
            except ValueError:
                print("输入的内容无法转换为数值")
                continue
            sheet.cell(row=i, column=5, value=user_input)  # 将转换后的值赋给指定的单元格


        wb.save(file)
        print(f"处理后的数据已保存至 {file}")