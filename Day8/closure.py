#A closure is a function that remembers the variables from the scope 
#in which it was created, even after that scope has finished executing.
def outer(logo):
    def inner(msg):
        print(f"<{logo}>{msg}<{logo}>")
    
    return inner

fn1 = outer("UW")
fn2 = fn1("Hello")
fn3 = fn1("Welcome to UW")

def account_create(init_amount = 0):
    def atm(num, deposit = True):
        nonlocal init_amount
        if deposit:
            init_amount += num
            print(f"deposit: {num}, balance: {init_amount}")

        else:
            init_amount -= num
            print(f"withdrawal: {num}, balance: {init_amount}")
        
    return atm

atm = account_create()
atm(100)
atm(300)
atm(200, deposit=False)
