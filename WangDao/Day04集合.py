"""
集合 也是用哈希存储，使用场景目的是去重
不支持随机访问
"""
set1 = {"app","banana","cherry"}#集合初始化
#add()增加元素
set1.add("org")
print(set1)
#clear删除元素
set1.clear()
print(set1)
#copy()拷贝另一个集合
x = set1.copy()
print(x)
#求两个集合的差集difference()
set2 = {'a','b','c'}
set3 = {'c','s','p','w'}
z = set3.difference(set2)
print(z)
#直接在原来的集合中移除元素（差集）
# set3.difference_update(set2)
# print(set3)
#把集合中不重复的输出
p1 = set3.symmetric_difference(set2)
print(p1)
#删除集合中指定的元素
# set3.discard("c")
# print(set3)
print("-"*50)
#返回集合的交集
result = set3.intersection(set2)
print(result)
#判断是否有相同的元素
set4 = {'a','b','d'}
q = set3.isdisjoint(set4)
print(q)
#判断该集合是否为子集
q1 = set3.issubset(set3)
print(q1)
#求两个集合的并集
q2 = set3.union(set2)
print(q2)