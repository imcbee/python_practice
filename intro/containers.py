
#! lists (like js arrays)
#colors = ['red', 'green', 'blue'] # ordered list
#print(colors[0]) # it will give red
#print(len(colors)) # print the total: 3

# dict are unordered lists

colors = ['red', 'green', 'blue', 'purple'] 
print(colors[-1]) # this will give us purple
print(colors[-2]) # this will give us blue
    # it already knows to grab the last 
    # easier than colors[colors.length-1]

colors[-1] = 'orange' # it can be chnaged to any data type
print(colors) # ['red', 'green', 'blue', 'orange']

#! push()
colors.append('yellow') # pushes to the end
print(colors) # ['red', 'green', 'blue', 'orange', 'yellow']

#! extend() - pass in a list
colors.extend(['black', 'white', 'red'])
print(colors) # appends at the end of the list

new_color = ['brown', 'mac & cheese'] + colors
print(new_color) # 
# ['brown', 'mac & cheese', 'red', 'green', 'blue', 'orange', 'yellow', 'black', 'white', 'red']

#! inserting elements
# insert( index, value )
print(colors)
colors.insert(4, 'hot pink')
print(colors)
# ['red', 'green', 'blue', 'orange', 'hot pink', 'yellow', 'black', 'white', 'red']

#! deleting elements - pop()
# pop() removes item at index passed, or last as default if empty
hot_pink = colors.pop(4)
print(hot_pink) # 
print(hot_pink) # hot pink
print(colors) # hot pink will not be there anymore
# ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'white', 'red']

#! del
del colors[0]
print(colors) # first red is gone
# ['green', 'blue', 'orange', 'yellow', 'black', 'white', 'red']

#! remove()
colors.remove('orange')
print(colors) # it ill remove ornage
# ['green', 'blue', 'orange', 'yellow', 'black', 'white', 'red']

#! clear() - this will clear the whole list


#! iteration
for color in colors: # use singular of the plural in loops
    print(color)

# for dict
for i, color in enumerate(colors):
    print(i, color)

# dict = objects
menu = {
	'hamburger': 4.99,  # double click and hit single-quote to make in quote
	'french_fries': 1.99,
	'taco': 2.99
}

colors.remove(colors[0])
print(colors) # ['blue', 'yellow', 'black', 'white', 'red']

# also remove() works too

#! list comprehension
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = []

for n in nums:
    squares.append(n * n)
print(squares) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# [<exp> for <item> in <list>]
squares_list_comp = [n * n for n in nums]
print(squares_list_comp) #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

    # list comprehensions can simplify making this happen

squares_list_comp2 = [n * n for n in nums if (n * n) % 2 == 0]
# make sure to have the []
print(squares_list_comp2) # [4, 16, 36, 64, 100]

#! write out regularly
even_squares = []

for n in nums:
    square = n * n
    if square % 2 ==0:
        even_squares.append(square)

print(even_squares)

#! for dict, it can work the same way.  See below
squares_list_comp3 = {n: n * n for n in nums if (n * n) % 2 == 0}
print(squares_list_comp3) # {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}

#! Tuples
# only difference is that tuples are immutable, can't be changed
# tuples are faster than lists because they are memory effcient
person = ('person', 'troy')

# defaults to a tuple if type isn't declared (comma-separated)
colors = 'red', 'green', 'blue'
print(type(colors)) # <class 'tuple'>
print(colors[0]) # red
    # you don't need to use a tuple, but they are great to use.

#! index() - accessing elements
blue_id = colors.index('blue') # 2

for idx, color in enumerate(colors):
	print(idx, color)
    #> 0 red
    #> 1 green
    #> 2 blue

#! unpacking
red, green, blue = colors
print(red, green, blue) #> red green blue

#! ranges
# range(stop) => range(0, stop)
# range(start, stop)
# range(start, stop, step)
for num in range(5):
    print(num)

# range(num =0, while num < stop, increment step)
num = 0
while num < 5:
    print(num)
    num += 1

    #! use whatever is easiest for you and readability

#! list()
nums = list(range(10)) # you can stack methods
    # 10 is like the stop, it stops at 9
print(nums) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

odds = tuple(range(1, 10, 2))
print(odds) # (1, 3, 5, 7, 9)

#! Moving backwards with range
for num in range(5, 0, -1):
    print(num)
# 5
# 4
# 3
# 2
# 1

#! Sliced
# slice [start:stop]
short_name = 'Alexandria'[0:4]
print(short_name) # Alex

video_games = ['tetris', 'Valorant', 'super mario bros 2', 'zelda', 'ffvii']
# slice [start:] => return list from starting index to end
new_vg_list = video_games[2:]# ['super mario bros 2', 'zelda', 'ffvii']
# slice [:end] => return list from 0 to ending index passed in
other_vg_list = video_games[:2] # ['tetris', 'Valorant']
last_vg_list = video_games[:] # ['tetris', 'Valorant', 'super mario bros 2', 'zelda', 'ffvii']
print(new_vg_list) 
print(other_vg_list)
print(last_vg_list)

