"""
多值参数(可以传不同个数的参数）
"""
# 容器非空就是False
# 空的容器和None不相等
if[]:
    print("非空列表")
else:
    print("空列表")
if{}:
    print("非空字典")
else:
    print("空字典")

#*args代表多值参数
def demo1 (*args,**kwargs):
    print(f'demo1{args},demo1{kwargs}')
def demo(num,*args,**kwargs):
    print(num)
    print(args)
    print(kwargs)
    demo1(*args,**kwargs)
# name="xiaom"keyword类型
demo(1,23,3,4,5,name="小明")