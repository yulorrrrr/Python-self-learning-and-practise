'''
f = open('python.txt','w')
f. write('helloworld')
f.flush()

#追加
f = open('python2.txt','a', encoding="UTF-8")
f.write('aven\n')
f.flush()
f.close

f1 = open('bill.txt', 'r', encoding = "UTF-8")
f2 = open('bill.txt', 'a', encoding = "UTF-8")
for line in f1:
    line = line.strip() # remove \n and space 
    if line.split(",")[4] == "test":
        continue
    f2.write(line)
    f2.write("\n")
f1.close()
f2.close()


#try
try:
    f = open("christine.txt", "r", encoding = "UTF-8")

except:
    print("file not found")
    f = open("christine.txt", "w", encoding = "UTF-8")

#捕获指定的异常
try:
    #1/0
    print (name)
except NameError as e:
    print("variable is not defined")
    print(e)

#capture multiple error
try:
    1/0
    print(name)
except (NameError, ZeroDivisionError) as e1:
    print(e1)

#capture all error
try:
    print(name)
    3/0
    f = open ("aven.txt", "r")
except Exception as e3:
    print(e3)

#model
#general
import time
print("hello")
time.sleep(5)
print("Hi")

#model
from time import sleep
print("start")
sleep(1)
print("end")

#*
from time import *
sleep(5)

#as
from time import sleep as sl
import time as t
t.sleep(5)
sl(5)
'''

#define model
from my_model import *
test_A(1,2)