mylist = [1,2,3,4]

index = mylist.index(1)
print ({index}) #find the index

#add new element
mylist.insert(2,5)

#add new element to the tail
mylist.append(6)

#add another list
mylist2 = [7,8,9]
mylist.extend(mylist2)

#delete
del mylist[2]
element = mylist.pop(2)
mylist.remove(1)
print(mylist)
print({element})

#clear list
mylist.clear()

#count specific data
count = mylist.count(1)

#count total data
count = len(mylist)

#print cycle
my_list = [1,2,3,4,5,6,7,8,9,10]
'''for element in my_list:
    if element%2 ==0:
        print({element})'''

index=0
while index < len(my_list) :
    element = my_list[index]
    index += 1
    if element%2 ==0:
        print({element})
        

