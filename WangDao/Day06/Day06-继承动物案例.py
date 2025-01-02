"""
super().__init__(self)子类对象执行了父类的__init__的方法
"""
class Animal:
    def __init__(self, name):
        self.name = name
    def eat(self):
        print('吃饭')
    def drink(self):
        print('喝水')
    def sleep(self):
        print('睡觉')
class Dog(Animal):
    # 重写父类中的init
    def __init__(self, name, color):
        super().__init__(name)  # 子类对象调用父类init
        self.color = color
    def bark(self):
        print(f'{self.name}旺旺叫{self.color}')
class Cat (Animal):
    def __init__(self,name,jump):
        self.name = name
        self.jump = jump
        super().__init__(name)
    def bark(self):
        print(f'小猫叫{self.name},跳{self.jump}米')


class xiaotianqian(Dog):
    def __init__(self,name,age,color):
        super().__init__(name,color)
        self.age = age

    def fly(self):
        print(f'{self.name}我会飞--{self.age}')


if __name__ == '__main__':
    wangca = Dog('旺财', '黄色')
    wangca.sleep()
    xiaotianquan = xiaotianqian('哮天犬', '20','黑色')
    xiaotianquan.bark()
    xiaotianquan.fly()
    cat = Cat('小花猫',60)
    cat.bark()
