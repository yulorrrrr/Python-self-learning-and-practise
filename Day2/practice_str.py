
my_str = "itheima itcast bouxuegu"
my_str_2 = my_str.replace(" ","|")
print(my_str_2)
my_str_3 = my_str.split("|")
print(my_str_3)

mylist = [0,1,2,3,4,5,6,7]
result1 = mylist[1:4]
print(result1)

mystr = "01234567"
result2 = mystr[0:4:2]
print(result2)
result3 = mystr[::-1]
print(result3)

#set{} tuple() list[] str""
myset = {"a","b","c","d","a","a","b"}
print(myset) # no order
myset.add("f")
print(myset)

#pick an element randomly
element = myset.pop()
print({element})

#find the difference for two set, don't change the origin set
set1 = {1,2,3}
set2 = {1,4,5}
set3 = set1.difference(set2)
print(set3)

#delete the same element 
set1.difference_update(set2)
print(set1)
print(set2)

#turn two set to one
set4 = set1.union(set2)
print(set4)

num = len(set4)
print(num)

#dict find value through key, key can't repeat
my_dict = {"christine" : 100, "aven" : 99, "aria" : 98} 

#empty dict
my_dict2 = {}
my_dict3 = dict()
score = my_dict["christine"]
print(score)

stu_score_dict = {
    "christine" : {
        "Chinese" : 77,
        "Math" : 66,
        "English" : 55
    },
    "aven" : {
        "Chinese" : 76,
        "Math" : 65,
        "English" : 54
    },
    "aria" : {
        "Chinese" : 75,
        "Math" : 64,
        "English" : 54
    }
}
score = stu_score_dict["aven"]["Chinese"]
print(score)

#add element
my_dict["judy"] = 66
print(my_dict)

#update element
my_dict["christine"] = 33
print(my_dict)

#delete element
score = my_dict.pop("aven")
print(my_dict)

#take keys
keys = my_dict.keys()
print(keys)

#for 
for key in keys:
    print(key)
    print([my_dict[key]])

#method2
for key in my_dict:
    print(key)
    print(my_dict[key])


my_dict = {
    "aa" : {
        "apartment" : "technical",
        "salary" : 3000,
        "level" : 1
    },
    "bb" : {
        "apartment" : "market",
        "salary" : 5000,
        "level" : 2
    },
    "cc" : {
        "apartment" : "market",
        "salary" : 7000,
        "level" : 3
    },
    "dd" : {
        "apartment" : "technical",
        "salary" : 4000,
        "level" : 1
    },
    "ee" : {
        "apartment" : "market",
        "salary" : 6000,
        "level" : 2
    },

}

for name in my_dict:
    if my_dict[name]["level"]==1:
        my_dict[name]["salary"] += 1000
        my_dict[name]["level"] += 1

print(my_dict)