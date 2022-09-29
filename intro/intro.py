# comments with hash
# print with 'print'
# print('hello world')

# let instructors = ['troy', 'eric', 'josh'];
#instructors = ['troy', 'eric', 'josh'] # these are called lists instead of arrays
# {} are dictionaries

# meaningful whitespace
# for instructor in instructors:
#     print(instructor)

# Snake Case
# sei_students = [1,2,3,4,5]

NUMBER_OF_DAYS_IN_A_WEEK = 7
DAYS_IN_A_WEEK = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# variables can be reassigned/redeclared, use uppercase as a convention

# print(DAYS_IN_A_WEEK)

is_monday = True # needs to be capital

# Logical Operators
    # &&
#print(is_monday and False) # False
    #| |
#print(is_monday or False) # True
    # !
#print(not is_monday) # ! in JS

# Relational Operators
#print(is_monday == False) # comparison operator ===
    # there is no triple equals 
#print(is_monday != False) # makes it True

# > < >= <= all the same as JS

# Arthimetic Operators
# + - * / % These are all the same again
# exponent ^ = (**)
#print(3**3) # 3 * 3 * 3 = 27

# division
#print(9//2) # this floors the number
    # 14.5 / 3    # => 4.833333
    # 14.5 // 3   # => 4.0

# float => int
#print(int(14.75)) # floors the decimal, also gets rid of it completely

# int => float
#print(float(14))

#Strings
# no difference in '' or ""
#escape characters
#print('This is \n new line.') # this makes a paragraph

# String Interpolation
thing_to_do = "Take it"
way_to_do_it = "easy"
pronoun = "dude"

#print('{} {} {}. But {}!'.format(thing_to_do, way_to_do_it, pronoun, thing_to_do))
    # or...

# version 3.6 and up
#print(f'{thing_to_do} {way_to_do_it} {pronoun}. But {thing_to_do}')

num_tacos = 25
# msg = 'There are ' + num_tacos + 'tacos!' # you can't do this, only concat strings and not integers
# # 
msg = 'There are ' + str(num_tacos) + ' tacos!' # this will toString()
# 
# print(msg)

#!  Conversion Methods
# str(item)        # Converts item to a string
# int(item)        # Converts the provided item to an integer 
# float(item)      # Converts the item to a floating-point number
# hex(int)         # Converts an integer to a hexadecimal STRING
# oct(int)         # Converts an integer to an octal STRING
# tuple(item)      # Converts item to a tuple
# list(item)       # Converts item to a list
# dict(item)       # Converts item to a dictionary

# string methods
splitWords = 'ace of spades'.split(' ')
# print(splitWords)
# ['ace', 'of', 'spades'] splits at the spaces

# print(list('abcd')) # this will return each character as a list ['a', 'b', 'c', 'd']

# substring
# print('qqxzzz'.index('c')) # this will return an error
# print('qqxzzz'.index('x')) # returns index of 2

# toUpperCase()
"boo".upper() # => BOO

# toLowerCase()
"WHY???".lower() # => why???

# toUpperCase() for the first index
"what".capitalize() # => What

# .replace(old_string, new_string)
py_var = 'Monty Python'
py_code = py_var.replace('Monty', 'Coding') # Coding Python
# print(py_code)

# in_method
# print('Python' in py_var) # should return a boolean (True)
    # this is caps sensitive!!
# print('python' in py_var) # (False)

# .length()
word_len = len('tacos') # 5
# print(word_len)

# Flow Control
x = 0

# if x < 0:
#     print('Negative')
# elif x == 0:
#     print('Zero')
# else:
#     print('Positive')

# python ternary expression
age = 12
beverage = 'Beer' if age >= 21 else 'Milk'
    # this is great for algo, but it is cluttered

# this is exactly like above, but this is better to read in a professional environment
if age >= 21:
    beverage = 'Beer'
else:
    beverage = 'Milk'

# loops
# count = 0
# while count < 5:
#     print(count, 'is less than 5')
#     count = count + 1 # count += 1 works as well
# else:
#     print(count, 'is not less than 5')
# # 0 is less than 5
# # 1 is less than 5
# # 2 is less than 5
# # 3 is less than 5
# # 4 is less than 5
# # 5 is not less than 5

# count = 15
# for i in range(1,count):
#     print(i)
# else:
#     print("done")
    # prints until 15 and logs done

count = 15
# range(start, end)
# for i in range(1,count):
#     print(i)
# else:
#     print("done")

def add_nums(a,b): # def instead of function; means to declare function
    c = a + b
    return c

#print(add_nums(1,2))

#! 15 min activity: make a fizzbuzz function

# def fizz_buzz(num):
#     for i in range(1,num):
#         if i % 3 == 0 : 
#            i == "fizz"
#         elif i % 5 == 0 : 
#             i == "buzz"
#         elif i % 3 == 0 and i % 5 == 0 : 
#             i == "fizzbuzz"
#     print(i)
        

# print(fizz_buzz(16))

# def fizz_buzz():
#     for i in range(1, 21):
#         if i % 3 == 0 and i % 5 == 0:
#             return 'fizzbizz'
#         elif i % 3 == 0:
#             return 'fizz'
#         elif i % 5 == 0:
#             return 'buzz'
#         else:
#             return i

# def fizz_buzz(num):
#     for i in range(1, num +1):
#         if i % 3 == 0 and i % 5 == 0:
#             print('fizzbizz')
#         elif i % 3 == 0:
#             print('fizz')
#         elif i % 5 == 0:
#             print('buzz')
#         else:
#             print(i)
# return stops the function

# you need to loop outside of the function if you want to return something?

# range()
    # this is a (start, stop, step) 
# for i in range(0, 10, 2):
#     print(i)

# def print_even_nums(num):

#     for i in range(0, num+2, 2):
#         print(i)


# collections
# arrays are now lists in python
first_nums = [1,2,3,4,5]
second_nums = [6,7,8,9,10]

set_of_nums = first_nums + second_nums
#print(set_of_nums) 
# you can just concat two lists together with +

# list methods
# append is exactly push
set_of_nums.append(11)
#print(set_of_nums) # adds to the end of the list

# pop - deletes from a list
    # defaults pop() on the last element
    # you can add a position of index
set_of_nums.pop(4) # this will remove 5 from the list

# remove() - removes specific element from list
set_of_nums.remove(9) # removes 9 from the list
    # this will only remove the first instance of 9, not all 9s

# clear() - removes the whole list
set_of_nums.clear()

# to clear a specific instance, use a while loop
while 9 in set_of_nums:
    set_of_nums.remove(9)

# print(set_of_nums)

# enumerate
    # passing in index into loops, separated by a comma.
    # for idx, value in enumerate(values)
# instructors = ['troy', 'eric', 'josh']

# for i, instructor in enumerate(instructors):
    #print(i, instructor)
# 0 troy
# 1 eric
# 2 josh

# dictionaries
    # set of key value pairs (key: value)

# student = {
#     'name': "Heather",
#     'course': 'SEI',
#     'current_week': 10
# }

# name = student['name'] = "Heather" # name = Heather
# name = student['name'] = 'Phil' # name = Phil
# # student = {'name': 'Phil', 'course': 'SEI', 'current_week': 10}
# current_week = student['current_week'] = 11

# # get() => dict_name.get(key) = value
# course = student.get('course') # SEI
# # print(course)

# instructor = student.get('instuctor') # return none
# instructor = student.get('instructor', 'Default Instructor')
# # you can pass in a default value as the second parameter in get() method
#     # get(lookup, default if lookup doesn't exist)
# print(instructor)

# check_in = {
#     {'name': "Tim", "student": True, "is_present": True},
#     {'name': "Kingsley", "student": True, "is_present": True},
#     {'name': "Mona", "student": False}
# }

# for i, person in enumerate(check_in):
#     name = person.get('name')
#     #print(name)
#     student = person.get('student')
#     #print(student)
#     is_present = person.get('is_present', False) # setting a default value for a key that doesn't exist
#     #print(is_present)


# "in" operator - return a boolean

student = {
    'name': "Heather",
    'course': 'SEI',
    'current_week': 10
}

#print('name' in student) # True
#print('instructor' in student) # False

# in list
#print(10 in [1,2,3,4,5]) # False

import datetime
    # pulling in a library called datetime

today = datetime.datetime.today()
#print(today) #2022-09-26 12:02:23.546441

month = today.month
#print(month) # 9

day = today.day
#print(day) # 26

#print(type(today)) # <class 'datetime.datetime'>

# import is a built-in object, so we can use dot-notation

# dir(library_name)
#print(dir(datetime))
#['MAXYEAR', 'MINYEAR', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']

# adding items
things = {
    'book': 'harry potter',
    'interface': 'apollo twin',
    'color': 'blue'
}

things['rubber_ducky'] = 'Quacky'
#{'book': 'harry potter', 'interface': 'apollo twin', 'color': 'blue', 'rubber_ducky': True}

# deleting items
del things['color']
# {'book': 'harry potter', 'interface': 'apollo twin', 'rubber_ducky': True}

# number of items in dict
print( student )
#> {'name': 'Tina', 'course': 'SEI'}
len(student)
#> 2
len({})
#> 0

# items() - iterates through a dictionary
# for key, value in things.items():
#     print(f'{key}: {value}')

where_are_my_things = {
    "computer": "desk",
    "keyboard": "table",
    "water_bottle": "kitchen",
    "headphones": "desk"
}

for key, val in where_are_my_things.items():
    print(f"{key} is kept in {val}") 