import os

def use_dir_func():
    file_list = os.listdir() # 目录列表
    print(file_list)
    # os.mkdir('dir2') # 创建目录
    # os.rmdir('dir1') # 删除目录
    print(os.getcwd())# 获得当前目录的绝对路径
    os.chdir('dir2') # 改变文件路径
    file = open('file2.txt','w',encoding='utf-8')
    file.close()

if __name__ == '__main__':
    use_dir_func()