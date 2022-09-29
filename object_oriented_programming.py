# OOP in python

class User:
    person_count = 0
    # local variable
    # tied to a class(User) -> static or class property

    def __init__(self, name, location='nowhere', fav_color="blue"):
        self.name = name
        self.location = location
        self.favorite_color = fav_color
        self.is_alive = True
        User.person_count += 1
    
    def greet(self):
        print(f'Hi! {self.name}')
    # person_count += 1
    # class instance

    # def increment_user():
    #     person_count += 1

ian = User('Ian McBee')
ian2 = User('Dingus')
ian3 = User('Ian Howard')

#print("new instance", ian.name) # new instance Ian McBee
#print("current user count", User.person_count) # current user count 3
#ian3.greet() # Hi! Ian Howard

# WE DO

class Account:

    balance = 0

    def __init__(self, type, balance=0, ):
        self.type = type
        self.balance = balance
    
    def deposit(self, num):
        return f'{num} was deposited.', num + self.balance

    def withdraw(self, num):
        return f'{num} was withdrawed.', num - self.balance

savings = Account('savings', 500)
checkings = Account('checkings', 200)

# print("new savings account", savings.type, savings.balance)
# print("new savings account", checkings.type, checkings.balance)

# print(savings.deposit(100))
# print(savings.withdraw(100))

#! Class answer
class Account:
    def __init__(self, type):
        self.type = type
        # def __init__(): is like the constructor -> new() __init__()
        # sets up self-references
        self.balance = 100 # doing this because literally interpretation

        # if we did Account.balance >> static property / class property

    def withdrawal(self, num):
        # base function - withdraw x value (num)
        # modify instance value
        self.balance -= num
        # return new balance
        return num

    def deposit(self, num):
        self.balance += num
        return self.balance

test = Account('checking')
print("testing instance", test.type)
print(test.withdrawal(2)) # 2; returning what was withdrawn
print(test.deposit(4)) # 102; returning the new balance
        