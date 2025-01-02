"""
字典
存储多个数据，通常描述一个物体的相关信息，键值对类型
"""
student = {"name":"小明",
               "age":20,
               "gender":"men"}
def use_dict_base():
    print(student['age'])#取值
    print(len(student))#打印字典长度
    print(student.values())
    print(student.keys())
    print(student.items())#所有元组列表
    #2.增加修改
    student['分数']=18#增加
    print(student)
    #如果键存在就是改变
    student['age']=18
    print(student)
    print(id(student))
    #3.删除
    student1 = {"name":"小明",
               "age":20,
               "gender":"men"}
    student.pop('name')#pop删除的是对应的值
    del student1['name']
    print(student1)
    print(student)
    #4.合并字典
    temp_dict={"height":1.76,
               "weight":180}
    student.update(temp_dict)
    print(student)
#5.循环字典
def usr_for():
    for k in student:
        print(k,student[k])

def usr_dict_for():
    for k,v in student.items():
        print(f'键{k}值{v}')

#6.列表化字典
def list_dict():
    card_list=[{"name":"慕斯",
               "age":40,
               "gender":"men"}]
    for card in card_list:
        print(card)

if __name__ =='__main__':
    # usr_for()
    # print('-'*50)
    # usr_dict_for()
    # list_dict()
    use_dict_base()

