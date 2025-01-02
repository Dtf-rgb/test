"""
高级变量类型：元组、字典、字符串

"""
#元组


info_tuple=("wangdao",18,1.75)#定义元组
# for i in info_tuple:
#     print(i)
#
# print(info_tuple.index("wangdao"))#输出元组中元素的索引
#统计计数
print(info_tuple.count("wangdao"))
#统计元组中个元素的个数
print(len(info_tuple))
def use_str():
    # 格式化字符串
    print("%s年龄是 %d %.2f" % info_tuple)
    info_str = "%s年龄是 %d %.2f" % info_tuple
    print(info_str)
    print(f'使用{info_tuple}')

if __name__ == '__main__':
    use_str()