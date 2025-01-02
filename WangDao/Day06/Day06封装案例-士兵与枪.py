class Gun:
    def __init__(self,model):
        self.model = model
        self.bullet_count = 0
    def add_bullet(self,count):
        self.bullet_count += count
    def shoot(self):
        # 判断是否有子弹
        if self.bullet_count <= 0:
            print("没有子弹了")
            return
        # 发射子弹
        self.bullet_count -= 1
        print("%s 发射子弹[%d] " % (self.model,self.bullet_count))

class Soldier:
    def __init__(self,name,gun : Gun=None):
        self.name = name
        self.gun = None
    def fire(self):
        # 1.判断士兵是否有枪
        if self.gun is None:
            print('[%s] 还没有枪' % ( self.name))
            return
        print('[%s]冲锋' % (self.name))
        # 3.装子弹
        self.gun.add_bullet(50)

        self.gun.shoot()

if __name__ =='__main__':
    ak47 = Gun("AK47")
    xisanduo = Soldier('许三多')
    xisanduo.gun = ak47
    xisanduo.fire()
