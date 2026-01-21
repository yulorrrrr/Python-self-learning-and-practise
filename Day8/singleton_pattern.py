#The Singleton Pattern ensures that a class has only one 
#instance and provides a global point of access to that instance.

class StrTools:
    pass

s1 = StrTools()
s2 = StrTools()
print(id(s1))
print(id(s2)) #these two are differnet object, their address is different



from singleton_patten_str_tool import str_tool2
s3 = str_tool2
s4 = str_tool2
print(id(s3))
print(id(s4))