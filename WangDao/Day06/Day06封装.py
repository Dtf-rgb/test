"""
封装 属性+方法
优先设计被依赖的类
"""
class Person():
    def __init__(self,name,weight):
        self.name = name
        self.weight = weight
    def run(self):
        self.weight-=0.5
        print(f'{self.name}跑步了，体重减去0.5,现有体重{self.weight}')
    def eat(self):
        self.weight += 0.5
        print(f'{self.name}吃饭，体重增加0.5，现有体重{self.weight}')

    def __str__(self):
        print(f'名字是{self.name}')
if __name__ == '__main__':
    elephant = Person('大象',80)
    elephant.run()
    elephant.eat()
    elephant.__str__()


