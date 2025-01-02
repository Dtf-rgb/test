def open_r():
    """
    读取文件
    :return:
    """
    file = open("F:/dev/production/file.txt", "r", encoding="utf-8")
    text = file.read()# 读出来的都是字符串
    print(text)
    # file.close()# 关闭文件
def open_2():
    """
    r+ : 读文件写文件
    :return:
    """
    file = open('F:/dev/production/file.txt', mode='r+', encoding='UTF-8')
    text = file.read()  # 读出来的都是字符串
    print(text)
    file.write("world")# 加到读文件的光标后
    file.close()  # 关闭文件

def open_w():
    file = open("F:/dev/production/file.txt", "w", encoding="utf-8")
    file.write('你好')# 没有文件会创建文件，如果文件已经存在则会重写文件
    file.close()



if __name__ == '__main__':
    # open_2()
    # open_r()
    open_w()
