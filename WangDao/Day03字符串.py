"""
字符串:不可变数据类型
"""
import string

str1 = 'Hello Pythonll'
def str_find():
    """
    字符串查找与替换
    """
    print(str1.find(('e')))
    str2 = str1.replace('ll','CD',1)#替换,第三个参数是控制替换次数的
    print(str2)
def str_for():
    for c in str1:
        print(c,end='')


#字符串分割切片
def str_split_join():
    str2='ab,cde,f'
    print(str2.split(','))
    print(str2.splitlines())
    str_list = ['a','b''c']
    print(','.join(str_list))
def study_r():
    """
    \r和\n区别
    \r让光标回到开头
    :return:
    """
    s="abc\rd"
    print(s)
num_str = "8123456789"
def str_slice():
    print(num_str[2:6])
    print(num_str[2:])#2到末尾
    print(num_str[:6])#开头到第六个
    print(num_str[:])#全去
    print(num_str[::2])#步长为2，隔一个取一个
    print(num_str[1::2])#
    print(num_str[2::-1])#截取2到末尾-1字符串
    print(num_str[-2:])#截取末尾2个字符串
    print(num_str[::-1])#字符串逆序
def list_slice():
    my_list = list('12344566')
    print(my_list)
    #强制转换为int
    print([int(x) for x in my_list])


if __name__ == '__main__':
    # str_for()
    # str_find()
    # str_split_join()
    # study_r()
    # str_slice()
    list_slice()