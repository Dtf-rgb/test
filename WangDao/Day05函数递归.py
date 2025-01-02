"""
函数递归:一个函数在函数内部调用自己
"""

def sum_numbers(num):
    if num >=100:
        return 100
    sum_numbers(num + 1)



print(sum_numbers(10))