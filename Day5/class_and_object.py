
class Student:
    name = None
    gender = None
    nationality = None
    native_space = None
    age = None

    def say_hi(self,msg):
        print(f"Hi, my name is {self.name}, {msg}")

stu_1 = Student()

stu_1.name = "Chsitine"
stu_1.gender = "male"
stu_1.nationality = "China"
stu_1.native_space = "Guangdong"
stu_1.age = 19
stu_1.say_hi("thank you")

print(stu_1.name)

#function in class def name (self, variable)

#------------------------------------------------

#constructor __init___
class Student:
    name = None
    age = None
    tel = None
    
    def __init__(self,name,age,tel):
        self.name = name
        self.age = age
        self.tel = tel

    def __str__(self):
        return f"Student类对象, name:{self.name}, age:{self.age}"

#compare __lt__
    def __lt__(self, other):
        return self.age < other.age
    
#__le__ (<=)
    def __le__(self, other):
        return self.age <= other.age

#__eq__ (identify equal)
    def __eq__(self, value):
        return self.age == value.age

stu = Student("Christine",19,12345677)
stu2 = Student("Aven", 20, 12345999)
print(stu)
print(str(stu))
print (stu<stu2)
print (stu>=stu2)
print (stu==stu2)

#--------------------------------------------------

#private variable & function: __variable & function

class Phone:
    __current_voltage = 2

    def __keep_single_core(self):
        print("run CPU")

    def call_by_5G(self):
        if self.__current_voltage >= 1:
            print("start 5G call")
        else:
            print("error")

phone = Phone()
phone.call_by_5G()

#-------------practise----------------------------

class Phone2:
    __is_5G_enable = True

    def __check_5g(self):
        if self.__is_5G_enable:
            print("5g turn on")
        else:
            print("5g turn off, please use 4g")

    def call_by_5g(self):
        self.__check_5g()
        print("active call")

phone2 = Phone2()
phone2.call_by_5g()

#------------------------------------------------

#inheritance
class Phone3:
    IMEI = None
    producer = "HM"

    def call_by_4g(self):
        print("4g call")
    
class Phone2022(Phone3):
    face_id = "10001"
    def call_by_5g(self):
        print("5g call")
phone2022 = Phone2022
print(phone2022.producer)

#multi inheritance
class NFCReader:
    nfc_type = "5th generation"
    producer = "HM"
    
    def read_card(self):
        print("NFC read card")
    
    def write_card(self):
        print("NFC write card")

class Remote_Control:
    rc_type = "infrared control"

    def control(self):
        print("infrared control start")

class Myphone(Phone3, NFCReader, Remote_Control):
    '''pass #don't want to add new function'''
    producer = "Apple" #override

phone = Myphone()

# call a parent method
# method 1: parent name.variable / parent name.method(self)
# method 2: super().variable / super.method()

class MyPhone2(Myphone):
    def call_by_5g(self): 
        print(f"parent producer: {super().producer}")

myphone2 = MyPhone2()
myphone2.call_by_5g

#Type annotation: var: int=10 / my_list: list = [1,2,3] / my_list: list[int] = [1,2,3]