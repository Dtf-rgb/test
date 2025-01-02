#判断语句
# age =9;
# if age > 20:
#     print("不可以")
# elif age<20:
#     print("可以")

import random
# def usr_random():
#     player = int(input("请出拳 石头（1）/剪刀（2）/布（3）"))
#     computer = random.randint(1,3)#生成的随机数的范围
#     print(f"{computer}")
#     if player>computer:
#         print("你赢了")
#     elif player == computer:
#         print("平局")
#     else:
#         print("你输了")
#
# usr_random()

# def usr_print():
#     print("HELLO PYTHON",end="")#end保证不换行
#
# usr_print()
# def usr_for():
#     myList = [1,2,3]
#     #for循环中in后要放一个可以迭代对象
#     for i in myList:
#         print(i)
#     print("-"*20)
# usr_for()
# def ues_for_else():
#     for i in range(10):
#         if i == 15:
#             print("你找到了")
#             break
#     else:
#         print("失败")
# ues_for_else()


#带参数的函数
def sum_2(num1,num2):
    print(f'求和函数{num1+num2}')

sum_2(20,50)