""""
operater = input ("Enter an operater(+,-,*,/):")
num1=float(input("Enter the first number:"))
num2=float(input("Enter the second number:"))

if operater == "+":
    result = num1+num2
elif operater == "-":
    result = num1-num2
elif operater == "*":
    result = num1*num2
elif operater == "/":
    result = num1/num2
print (result) 
""" 
money = 500000
name = None

name = input (" please enter your name: ")

def query(show_header):
    if show_header:
        print("--------balance--------")
    print(f"{name}, your balance is {money} doller")

def saving(num):
    global money
    money += num
    print("--------deposit--------")
    print(f"{name}, deposit successfully")

    query(False)

def get_money(num):
    global money
    money -= num
    print("--------withdraw------")
    print(f"{name}, withdraw successfully")
    query(False)

def get_money_error():
    global money
    print("--------withdraw------")
    print(f"{name}, sorry you don't have enough balance")
    query(False)

def main():
    print("--------main----------")
    print(f"Hi {name}, welcome to ATM")
    print("check balance\t[enter1]")
    print("deposit\t\t[enter2]")
    print("withdraw\t[enter3]")
    print("exit\t\t[enter4]")
    return input("please enter your choice")

while True:
    keyboard_input = main()
    if keyboard_input == "1":
        query(True)
        continue
    elif keyboard_input == "2":
        num = int (input ("please enter the number of deposit: "))
        saving(num)
        continue
    elif keyboard_input == "3":
        num = int (input ("please enter the number of withdraw: "))
        if (money<num):
            get_money_error()
        else:
            get_money(num)
        continue
    else:
        print("exit")
        break

