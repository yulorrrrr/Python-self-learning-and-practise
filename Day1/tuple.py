#can't change after define
t1 = (1,'Hello', True)
t2 = ()
t3 = tuple() #empty

#for only one element tuple, should add , at the tail
t4 = (1,)
print({t1})

#index(), count(), len()
index=0
while index < len(t1):
    print({t1[index]})
    index +=1

t5 = (2,True,['football', 'music'])
t5[2][1] = 'coding'
print(t5)

#string can't add new variable
my_str = "you and me"
value = my_str[2]
print({value})
value = my_str.index("and")
print({value})

#replace
new_str = my_str.replace("y","b")
print(new_str)

#split
my_str_list = my_str.split(" ")
print(my_str_list)

#strip
my_str2 = "12hello world21"
new_str2 = my_str2.strip("12")
count = my_str2.count("o")
print(new_str2)
print(count)
