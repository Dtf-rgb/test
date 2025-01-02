"""
不可变类型
int，bool,float
字符串str
元组tuple
"""
def no_change(num):
    num=10

i = 10;
print(f'调用之前{i}')
no_change(i)
print(f"调用之后{i}")
"""
可变类型
list列表、dict字典、set集合
"""
def change(new_list):
    new_list[0]=10
my_list=[1,2,3]
print(f"调用之前{my_list}")
print(f"调用之前地址{id(my_list)}")
change(my_list)
print(f"调用之后{my_list}")
print(f"调用之后地址{id(my_list)}")