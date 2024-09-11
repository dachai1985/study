# -*- coding: utf-8 -*-

import os
import sys
import pandas as pd
import win32com.client as win32
import shutil
import psutil
import config

bts_link_flag = False
error_file_count = 0

# 获取当前folder内所有excel文件名
def get_excel_name_from_floder(folder_path):
    file_name = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if os.path.splitext(file)[1] == '.xlsx':
                file_name.append(os.path.join(root, file))
    return file_name

# 撤销当前Excel保护
def unlock_excel(file_name, password):  
    # 创建Excel应用程序实例  
    excel = win32.gencache.EnsureDispatch('Excel.Application')  
    excel.Visible = False  # 设置为不可见
    excel.DisplayAlerts = False  # 关闭警告提示
    try:  
        # 打开工作簿  
        workbook = excel.Workbooks.Open(file_name, Password=password)    
        # 如果有工作表保护，解除保护  
        for sheet in workbook.Sheets:  
            if sheet.ProtectContents:
                sheet.Unprotect(Password=password)  
                # 保存工作簿
                workbook.Save()
        workbook.Close()
    except Exception as e:  
        print(f"Error unlocking or reading the file: {e}", '\n')

# 移动文件到pass folder文件夹
def move_to_pass_folder(file_name):
    pass_folder = os.path.join(os.path.dirname(file_name), "pass folder")
    if not os.path.exists(pass_folder):
        # 如果不存在，则创建文件夹  
        os.makedirs(pass_folder)
    # 获取源文件的基本名称和扩展名  
    base_name, extension = os.path.splitext(os.path.basename(file_name))
    # 构建目标文件的初始路径  
    target_file = os.path.join(pass_folder, base_name + extension)
    # 检查目标文件是否存在,如果存在，生成一个新的文件名   
    if os.path.exists(file_name):
        counter = 1 
        while os.path.exists(target_file):  
            # 在基本名称后添加序号以生成新文件名  
            new_base_name = f"{base_name}_{counter}"  
            target_file = os.path.join(pass_folder, new_base_name + extension)  
            counter += 1
    shutil.move(file_name, target_file)

# 获取当前Excel所有sheet列表
def get_excel_sheet_list(file_name):
    try:
        df_excel = pd.read_excel(file_name, sheet_name=None, engine='openpyxl')
        # print("df_excel.keys()========", df_excel.keys())
        return df_excel.keys()
    #except IndexError as e:  
        #print(f"发生IndexError: {e}")
    except Exception as e:  
        error_message = str(e).encode('utf-8').decode(sys.getdefaultencoding(), 'ignore')
        print(f"Failed to read {file_name}")  
        print(f"Error: {error_message}")
        #print(f"Failed to read {file_name}. Moving to {error_folder}...")  
        #shutil.move(file_name, error_folder)

# 定义函数来执行查找操作  
def find_value_in_row(df, row_number, value_to_find):
    # 使用iloc定位指定行
    if row_number in df.index:    
        row = df.iloc[row_number] 
        for column in row.index:
            if row[column] == value_to_find:  
                return column  
        return None
    
# 定义函数来执行列查找操作
def find_value_in_column(df, column_number, value_to_find):
    # 使用iloc定位指定列
    if 0 <= column_number < df.shape[1]:  
        column = df.iloc[:, column_number]
        for index, value in enumerate(column):
            if value == value_to_find:  
                return index
        return None

# 获取当前sheet BTS Link列非空数值
def get_bts_count_sheet(file_name, sheet_name):
    df = pd.read_excel(file_name, sheet_name=sheet_name)
    row_to_check = 8 #指定BTS Link查找行号
    column_name_to_check = 'BTS Link'  
    position = find_value_in_row(df, row_to_check, column_name_to_check)
    global bts_link_flag
    if position is not None:  
        print(f"BTS Link found in the sheet {sheet_name} of column: {position}")  
        #bts_count = df[position].count() - 1
        bts_count_sheet = df[position].apply(  
            lambda x: not pd.isnull(x) and (  
            isinstance(x, str) and x.strip() != '' or  
            isinstance(x, (int, float))
            )
        ).sum() - 1
        print(f"{sheet_name} sheet bts count========== {bts_count_sheet}")
        bts_link_flag = True
    else:  
        print(f"BTS Link not found in the sheet {sheet_name}")  
        bts_count_sheet = 0
    return bts_count_sheet

# 获取当前Excel file BTS Link列非空数值
def get_bts_count_file(file_name):
    bts_count_file = 0
    global error_file_count
    global bts_link_flag
    try:
        print('filename==========', file_name)
        unlock_excel(file_name,'')
        sheet_names = get_excel_sheet_list(file_name)
        print("sheet_names=======", sheet_names)
        bts_link_flag = False
        for sheet_name in sheet_names:
            bts_count_file = bts_count_file + get_bts_count_sheet(file_name, sheet_name)
        print(f"{file_name} file bts count========== {bts_count_file}", '\n')
        if bts_link_flag:
            move_to_pass_folder(file_name)    
        else:
            error_file_count += 1
    except Exception as e:
        #print(f"Failed to read {file_name}. Moving to {error_folder}...") 
        #shutil.move(file_name, error_folder)    
        print(f"Error: {e}", '\n')
        error_file_count += 1
    return bts_count_file

# 遍历目录下的所有game文件夹,统计各文件的BTS count
def get_bts_count_game(reading_folder):
    # 字典用于存储每个文件夹的数据  
    bts_count_game = {}
    # 要跳过的子文件夹名称  
    skip_folder_name = "pass folder" 

    for folder_name, subfolders, filenames in os.walk(reading_folder):
        # 检查当前文件夹是否是我们要跳过的文件夹  
        if skip_folder_name in folder_name:
            continue  # 如果是，跳过当前循环，即不处理该文件夹  
        
        # 过滤出Excel文件（假设文件扩展名为.xlsx
        excel_files = [f for f in filenames if f.endswith('.xlsx')]
        # 如果文件夹中有Excel文件  
        if excel_files:
            # 初始化该文件夹的数据列表
            bts_count_game[folder_name] = []
            # 遍历该文件夹下的所有Excel文件  
            for excel_file in excel_files:  
                file_path = os.path.join(folder_name, excel_file)
                try:
                    #如果是JBI文件，直接移动到pass folder文件夹
                    if "JBI" in file_path:
                        move_to_pass_folder(file_path)
                        continue
                    # 读取Excel文件  
                    bts_count_file = get_bts_count_file(file_path)
                    
                    # 将统计结果添加到文件夹的数据列表中  
                    bts_count_game[folder_name].append((excel_file, bts_count_file))  
                except Exception as e:  
                    print(f"Error reading {file_path}: {e}", '\n')
    return bts_count_game

# 遍历TC Key,统计该Game的各TC Key所对应的BTS count
def get_bts_count_game_tc_key(tc_key, reading_folder):
    bts_count_game = get_bts_count_game(reading_folder)
    print ('bts_count_game==========', bts_count_game, '\n')

    bts_count_game_tc_key = []

    # 初始化一个字典来存储每个key的累加结果  
    results = {k:0 for k in tc_key}  
    
    # 遍历bts_count字典
    for path, files in bts_count_game.items():  
        # 遍历每个路径下的文件列表  
        for file, value in files:  
            # 遍历key列表，检查文件名是否包含当前key，如果找到，累加值到对应key的结果中
            for k in tc_key:  
                if k in file:  
                    results[k] += value

    # 获取当前Game文件夹名  
    #folder_name = os.path.basename(reading_folder)
    #bts_count_game_tc_key[folder_name] = []
    # 统计每个tc_key的累加结果  
    for k, total_bts_tc in results.items():
        bts_count_game_tc_key.append(total_bts_tc)
        #bts_count_game_tc_key[folder_name].append(total_bts_tc)
        #print(f"Key '{k}' total sum: {total_bts_tc}")
    return bts_count_game_tc_key

# 文件夹内所有Excel file的所有sheet，BTS Link列非空数值
def get_bts_count_all(file_names):
    bts_count_file_list = {}
    bts_count_all = 0
    print('all filenames==========', file_names, '\n')
    for file_name in file_names:
        bts_count_file = get_bts_count_file(file_name)
        bts_count_file_list[file_name] = bts_count_file
        bts_count_all = bts_count_all + bts_count_file
    return bts_count_all, bts_count_file_list

# if __name__=='__main__':
#     reading_folder = r'C:\\Users\\win\\Desktop\\RAW'
#     bts_count_game_tc_key = get_bts_count_game_tc_key(config.TC, reading_folder)
#     print ('bts_count_game_tc_key==========', bts_count_game_tc_key)
#     print ('error_file_count========', error_file_count)


    '''
    output_file = 'E:\\test excel file folder\Common TC Import&BTS Count.xlsx'
    game_name = "Bloodline TC Imported"
    df = pd.read_excel(output_file, sheet_name='2024')
    print(type(df))
    column = find_value_in_column(df, 0, game_name)
    print("999999999=",column)
    '''
    #pass_folder = 'E:\\test excel file folder\pass excel file'
    #error_folder = 'E:\\test excel file folder\error excel file'
    #excel_file_names = get_excel_name_from_floder(reading_folder)
    #bts_count_all = get_bts_count_all(excel_file_names, pass_folder)
    
    
