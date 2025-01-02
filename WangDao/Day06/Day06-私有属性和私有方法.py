"""
私有属性和私有方法只能在类内部访问
"""
class Women:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __secret(self):
        print(f'{self.name}年龄{self.age}')
    def boy_friend(self):
        self.__secret()


if __name__ == '__main__':
    xiaohong = Women('小红',20)
    xiaohong.boy_friend()
