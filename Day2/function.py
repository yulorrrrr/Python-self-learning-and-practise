def user_info (name, age, gender):
    print(f"name: {name}, age: {age}, gender: {gender}")
user_info('christine', 20, 'female')

#Variable-length parameter -> turn into tuple
def user_info2 (*args):
    print(args)

user_info2('TOM', 18 , True)

#turn into key
def user_info3 (**kwargs):
    print(kwargs)

user_info3(name= 'TOm', age = 18, gender = 'male')

#anonymous function lambda
def test_func(compute):
    result = compute(1,2)
    print (result)

test_func(lambda x,y: x+y)