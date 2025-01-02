class HouseItem:
    def __init__(self,name,area):
        """
        初始化方法
        :param name:家具名字
        :param area: 家具占地面积
        """
        self.name = name
        self.area = area
    def __str__(self):
        return "[%s] 占地面积 %.2f" %(self.name,self.area)
class House():
    def __init__(self,house_type,area):
        """
        房子类初始化
        :param house_type:
        :param area:
        """
        self.house_type = house_type
        self.area = area
        self.free_area = area
        self.items_list = [] #家具列表
    def __str__(self):
        return ("户型：%s\n总面积：%.2f[剩余：%.2f]\n家具：%s"
                % (self.house_type,self.area,
                   self.free_area,self.items_list))
    def add_item(self,item:HouseItem):#通过（:对象类型）
        if item.area > self.free_area:
            print('房子没有空间\n放置失败')
            return
        self.free_area-=item.area # 计算剩余面积
        self.items_list.append(item.name)
if __name__ == '__main__':
    table = HouseItem('桌子',5.2)
    bed = HouseItem("西蒙斯",20)
    chest = HouseItem('衣柜',2)
    print(table)
    print(bed)
    print(chest)
    house = House('两市一厅', 50  )
    house.add_item(bed)
    house.add_item(table)
    house.add_item(chest)
    print(house)
