"""
异常
"""
def use_exception1():
    try:
        num = int(input("请输入整数："))
        result = 8 / num
        print(result)
    except ValueError:
        print("请输入正确的整数")
    except Exception as e:
        print(e)

if __name__ == '__main__':
    use_exception1()
# while True:
#     try:
#         num = int(input("请输入整数："))
#         print(num)
#         break
#     except:
#         print("输入的必须是整型数字")