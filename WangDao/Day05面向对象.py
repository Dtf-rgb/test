"""
面向对象
对象.方法
"""
#Person叫类，里面的叫方法
class Person:
    def __init__(self,name,age,height):
        self.name = name
        self.age = age
        self.height = height
    def run(self):
        print("跑步")
    def eat(self):
        print("吃饭")
# 实例化,对象.方法
elephant =Person('大象',18,175)
print(elephant.name,elephant.age,elephant.height)
elephant.run()
tiger =Person('大象',18,175)
tiger.eat()
print(dir(elephant))