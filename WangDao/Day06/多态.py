"""
多态：同一条指令，有不同的结果
"""
class Dog():
    def __init__(self,name):
        self.name = name
    def game(self):
        print("%s 在地上玩耍" % self.name)
class xiaotian(Dog):
    def game(self):
        print("%s 飞到天上玩耍" % self.name)

class Person():
    def __init__(self,name):
        self.name = name
    def game_with_dog(self,dog:Dog):
        pass

if __name__ == '__main__':
    man = Person('老大')
    man.game_with_dog("旺财")