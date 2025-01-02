#从1到100之间的奇数求和
# sum_of_odds = 0
# for i in range(1, 101, 2):
#
#     sum_of_odds += i
#
# print(sum_of_odds)

#打印九九乘法表
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(f"{j} x {i} = {i * j}", end="\t")
#     print()

#统计一个整数对应的二进制数的1的个数。输入一个整数（可正可负，负数就按64位去遍历即可）， 输出该整数的二进制包含1的个数（使用位运算）
def count_ones(n):

    if (n<0):
        n = n & 0xFFFFFFFFFFFFFFFF
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count
num = int(input("请输入一个整数："))
print(f"该整数的二进制中1的个数为: {count_ones(num)}")