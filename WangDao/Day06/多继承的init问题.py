class Parent():
    def __init__(self,height):
        self.height = height

class Son1(Parent):
    def __init__(self,age,*args):
        self.age = age
        super().__init__(*args)


class Son2(Parent):
    def __init__(self,score,*args):
        self.score = score
        super().__init__(*args)


class Grandson(Son1,Son2):
    def __init__(self,name,*args):
        self.name = name
        super().__init__(*args)

if __name__ == '__main__':
    x = Grandson('小明',18,98.5,60)
    print(x.name)
    print(x.age)
    print(x.score)
    print(x.height)
