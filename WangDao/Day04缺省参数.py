"""
缺省参数
"""
#name是位置参数，title=""是确实参数
def print_info(name, title="", gender=True):
    """

    :param name: 同学名字
    :param title: 职位
    :param gender:
    :return:
    """
    gender_text = "男生"
    if not gender:
        gender_text = "女生"
    print("%s%s 是 %s"%(title,name,gender_text))

if __name__ == "__main__":
    print_info("小明",'学生')