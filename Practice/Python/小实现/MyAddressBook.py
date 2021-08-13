# coding=utf-8
# My Address Book
import os

# 指定目标文件夹，作为数据的存取地点
adb_dir = r"E:\Backup"

# 如果目标目录还不存在，则进行创建
if not os.path.exists(adb_dir):
    os.mkdir(adb_dir)

class Person:
    """ 这是一个·人·类 """

    def __init__(self, name = '(Empty)', address = '(Empty)', reship = '(Empty)', email = '(Empty)', tel = '(Empty)'):
        """ ·人·类的初始化函数，包含一个人的姓名等信息（共计5个） """
        self.__name    = str(name)                           # 姓名
        self.__address = str(address)                        # 住址
        self.__reship  = str(reship)                         # 关系
        self.__email   = str(email)                          # 电子邮箱地址
        self.__tel     = str(tel)                            # 电话号码
    # end

    def getName(self):
        """ 获取此人的姓名 """
        return self.__name
    # end

    def getAddress(self):
        """ 获取此人的住址 """
        return self.__address
    # end

    def getRelationship(self):
        """ 获取与此人的关系 """
        return self.__reship
    # end

    def getEmail(self):
        """ 获取此人的电子邮箱地址 """
        return self.__email
    # end

    def getTel(self):
        """ 获取此人的电话号码 """
        return self.__tel
    # end
# end

class Adbook:
    """ 这是一个·地址簿·类 """

    def __init__(self):
        """ ·地址簿·类的初始化函数，设定·此·地址簿现有的人数 """
        self.__now = 0
    # end

    def addPerson(self, num = 1):
        """ 向地址簿中加入联系人信息，可以是多个 """
        for i in range(num):
            print("Please follow my guidence to finish this task (end each one with 'Enter'): ")
            name    = str(input("Name: "))                         
            address = str(input("Address: "))
            reship  = str(input("Relationship: "))
            email   = str(input("E-mail: "))
            tel     = str(input("Telephone number: "))
            # 附加此地址簿所拥有的实体人对象
            self.__dict__[f"Person {self.__now+1}"] = Person(name, address, reship, email, tel)       
            self.__now += 1                        # 此地址簿人数增加：1  
            print("Added \"{0}\" successfully!".format(name))  
    # end

    def getSum(self):
        """ 获取此地址簿现存人数 """
        return self.__now           
    # end
# end      


myadbook = Adbook()         # 创建一个新的地址簿对象


myadbook.addPerson(2)
print("Now we have {0} people.".format(myadbook.getSum()))

# 读写
f = open("Address.txt", "a+")

addtext = """*
Name: {name}
Address: {address}
Relationship: {reship}
E-mail: {email}
Telephone number: {tel}
*\n""".format(name=myadbook.__dict__["Person 1"].getName(), 
              address=myadbook.__dict__["Person 1"].getAddress(),
              reship=myadbook.__dict__["Person 1"].getRelationship(),
              email=myadbook.__dict__["Person 1"].getEmail(),
              tel=myadbook.__dict__["Person 1"].getTel())

f.write(addtext)
f.close()
