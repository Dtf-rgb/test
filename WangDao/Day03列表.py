"""
列表：里面可以存不同类型的数据，也可以嵌套定义
"""


# 列表定义
my_list = ['god',999,'azd']

# 按下标索引取元素,正向反向取元素
print(my_list[1])
print(my_list[-1])

# 取出嵌套列表的元素
my_list1 = [[222,'azd'],['tjy',2333]]
print(my_list1[0][0])

# index方法,查找元素在列表中的下表索引
print(my_list.index(999))

# 修改特定下标索引的值：列表名[] = 赋值
my_list1[1][0] = "dtb"
print(my_list1)
print("-"*50)
# 在指定索引位置插入新元素:列表名.insert(下标,元素)
my_list.insert(1,257)
print(my_list)
# 在尾部追加单个新元素:列表.append(元素)
my_list2 = [1,2,3,4,5,6]
my_list2.append('dtb')
print(my_list2)
# 在尾部追加一批新元素:列表.extend(其他数据容器)
my_list1.extend(my_list2)
print(my_list1)
print('-*'*50)
# 删除指定下标索引的元素
del my_list2[0]
print(my_list2)
e = my_list.pop(1)
print(e)

# 删除某个元素在列表中第一个匹配项:列表.remove(元素)
my_list3 = [2,'ppp','saier',2]
my_list3.remove(2)
print(my_list3)

# 清空列表
my_list3.clear()
print(f"列表被清空了{my_list3}")