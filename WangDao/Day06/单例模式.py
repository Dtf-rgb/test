"""
单例模式
"""
class MusicPlayer:
    instance = None  # 保存对象
    def __new__(cls, *args, **kwargs):
        # 1.创建对象，分配空间
        if cls.instance is None:
            cls.instance=super().__new__(cls) # 父亲的new类似于C语言的malloc
        return cls.instance
    def __init__(self,name):
        self.name = name
if __name__ == '__main__':
   play1 = MusicPlayer('七里香')
   play2 = MusicPlayer('天下')
   print(play1.name)
   print(play2.name)
