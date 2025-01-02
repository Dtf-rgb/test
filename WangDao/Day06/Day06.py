"""
没有init方法不能传参数
"""
class cat():
    def drink(self):
        print("小猫喝水")

    def eat(self):
        print("小猫喝水")
    # 内置方法
    def __init__(self,newname):
        self.name = newname
        print('初始化对象')
    def __del__(self):
        print(f'{self.name}猫对象被销毁')
    def __str__(self):
        """
        对象描述信息
        :return:
        """

# 实例化类
tom =cat('tom')
# 调用方法
tom.eat()
tom.drink()
