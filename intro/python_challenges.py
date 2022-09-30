'''
27Sep22
*******************************************************************************
Write a function even_range(start, end) that returns an list containing all even
numbers between 'start' and 'end' in sequential order.
Examples:
even_range(13, 20) => [ 14, 16, 18, 20 ]
even_range(4, 11) => [ 4, 6, 8, 10 ]
even_range(8, 5) => []
*******************************************************************************/
'''

def even_range(start, end):
    arr = []

    if start > end:
        return []
    if start % 2 != 0:
        start += 1
    if end % 2 != 0:
        end += 1
    for num in range(start, end, 2):
        arr.append(num)

    return arr

# print(even_range(13, 20))
# print(even_range(4, 11))
# print(even_range(8, 5))

'''
*******************************************************************************
Write a function phrase_finder(words, phrase), that takes in an list of words and a
string representing a phrase. The function should return True if the phrase can be
formed by a pair of words from the list. The function should return false if the
phrase cannot be formed by any pair of words.

Examples:

phrase_finder(['world', 'prep', 'hello', 'bootcamp'], 'bootcamp prep') => True
phrase_finder(['world', 'bootcamp', 'hello', 'prep'], 'bootcamp prep') => True
phrase_finder(['world', 'bootcamp', 'hello', 'prep'], 'hello world') => True
phrase_finder(['world', 'bootcamp', 'hello', 'prep'], 'hello prep') => True
phrase_finder(['world', 'bootcamp', 'hello', 'prep'], 'hello goodbye') => False
*******************************************************************************/
'''
def phrase_finder(words, phrase):
    arr = phrase.split()
    match = []
    not_match = []
    for word in words:
        for letter in arr:
            if word == letter:
                if word == arr[0]:
                    match.append(word)
                    match.append(letter)

                else:
                    not_match.append(word)
                    not_match.append(letter)
                if word ==arr[1]:
                    match.append(word)
                    match.append(letter)

                else:
                    not_match.append(word)
                    not_match.append(letter)

    if match[0] == match[1] and match[2] == match[3]:
        return True
    else:
        return False

#phrase_finder(['world', 'bootcamp', 'hello', 'prep'], 'hello goodbye')
# print(phrase_finder(['world', 'prep', 'hello', 'bootcamp'],'bootcamp prep'))
# print(phrase_finder(['world', 'bootcamp', 'hello', 'prep'], 'bootcamp prep'))
# print(phrase_finder(['world', 'bootcamp', 'hello', 'prep'], 'hello world'))
# print(phrase_finder(['world', 'bootcamp', 'hello', 'prep'], 'hello prep'))
# print(phrase_finder(['world', 'bootcamp', 'hello', 'prep'], 'hello goodbye'))

'''
-----------------------------------------------------------------
Prompt:

In information theory, the hamming distance refers to the count of the differences between two strings of equal length.  It is used in computer science for such things as implementing 'fuzzy search'  capability.

- Write a function named hamming_distance that accepts two arguments which are both strings of equal length.
- The function should return the count of the symbols (characters, numbers, etc.) at the same position within each string that are different.
- If the strings are not of the same length, the function should return float('nan'). Note: There is no native not a number type, but it can be cast through float() or imported from the python math library.

Examples:

hamming_distance('abc', 'abc'); //=> 0
hamming_distance('a1c', 'a2c'); //=> 1
hamming_distance('!!!!', '****'); //=> 4
hamming_distance('abc', 'ab'); //=> nan

-----------------------------------------------------------------*/

'''

#! did not attempt

'''
28Sep22
******************************************************************************
Write a function reverse_string(string) that takes in a hyphenated string and
returns a the hyphenated string reversed.

Examples:
reverseString('Go-to-the-store') => 'store-the-to-Go'
reverseString('Jump-jump-for-joy') => 'joy-for-jump-Jump,'
******************************************************************************
'''

def reverse_string(string):
    arr = string.split("-")
    arr.reverse()
    return '-'.join(str(e) for e in arr)




# print(reverse_string('Go-to-the-store'))
# print(reverse_string('Jump-jump-for-joy'))


'''
-----------------------------------------------------------------

Prompt:
- Write a function named is_prime that returns true when the integer argument passed to it is a prime number and false when the argument passed to it is not prime.
- A prime number is a whole number (integer) greater than 1 that is evenly divisible by only itself.

Examples:

is_prime(2) //=> true
is_prime(3) //=> true
is_prime(4) //=> false
is_prime(29) //=> true
is_prime(200) //=> false

-----------------------------------------------------------------*/
'''
import math
import string

def is_prime(num):
    if num == 2 or num == 3:
        return True
    if num % 2 == 0:
        return False
    if num <= 0:
        return False
    
    half_num = math.floor(num /2) + 1

    for i in range(3, half_num):
        if num % i == 0:
            return False
        else:
            return True
    

# print(is_prime(2))
# print(is_prime(29))
# print(is_prime(3))
# print(is_prime(4))
# print(is_prime(200))

'''
-----------------------------------------------------------------

Prompt:
You are given an list (which will have a length of at least 3, but could be very large) containing integers. The list is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the list as an argument and returns this 'outlier' N.

Examples
find_the_parity_outlier([2, 4, 0, 100, 4, 11, 2602, 36])
Should return: 11 (the only odd number)

find_the_parity_outlier([160, 3, 1719, 19, 11, 13, -21])
Should return: 160 (the only even number)

-----------------------------------------------------------------*/

'''

def find_the_parity_outlier(list):
    even_arr = []
    odd_number = 0
    negative_numbers = []

    for num in list:
        if num < 0:
            negative_numbers.append(num)
        if num % 2 == 0:
            even_arr.append(num)
        else:
            odd_number = num
    
    return odd_number

# print(find_the_parity_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))
# print(find_the_parity_outlier([160, 3, 1719, 19, 11, 13, -21]))

''' 29Sep22
******************************************************************************
Write a function intersect(list1, list2) that takes in two lists and returns a
new list containing the elements common to both list1 and list2.

Hint: use index()

Examples:

intersect(['a', 'b', 'c', 'd'], ['b', 'd', 'e']) => [ 'b', 'd' ]
intersect(['a', 'b', 'c'], ['x', 'y', 'z']) => []
*******************************************************************************/
'''
def intersect(list1, list2):
    matching_arr = []

    for item in list1:
        for letter in list2:
            if item == letter:
                matching_arr.append(item)
    
    return matching_arr

# print(intersect(['a', 'b', 'c', 'd'], ['b', 'd', 'e']))

'''
-----------------------------------------------------------------

Prompt:

- Write a function named merge_dictionaries that accepts at least two dictionaries as arguments, merges the properties of the second through n dictionaries into the first object, then finally returns the first dictionary.
- If any dictionaries have the same property key, values from the object(s) later in the arguments list should overwrite earlier values.

Examples:

merge_dictionaries({}, {'a': 1});  //=> {'a': 1} (same object as first arg)
merge_dictionaries({'a': 1, 'b': 2, 'c': 3}, {'d': 4});  //=> {'a': 1, 'b': 2, 'c': 3, 'd': 4}
merge_dictionaries({'a': 1, 'b': 2, 'c': 3}, {'d': 4}, {'b': 22, 'd': 44});  //=> {'a': 1, 'b': 22, 'c': 3, 'd': 44}
-----------------------------------------------------------------
'''

def merge_dictionaries(dict1, dict2):
    
    dict1.update(dict2)
    return dict1

# print(merge_dictionaries({'a': 1, 'b': 2, 'c': 3}, {'d': 4}))
# print(merge_dictionaries({'a': 1, 'b': 2, 'c': 3}, {'d': 4}, {'b': 22, 'd': 44}))

#! Jared's answer to learn from
def merge_dictionaries1(*args):
    new_dict = {}
    
    for dict in args:
        for key in dict.keys():
            new_dict[key] = dict[key]
    
    return new_dict

# print(merge_dictionaries1({'a': 1, 'b': 2, 'c': 3}, {'d': 4}))
# print(merge_dictionaries1({'a': 1, 'b': 2, 'c': 3}, {'d': 4}, {'b': 22, 'd': 44}))

#! Jordan's answer to what I wanted to do
def merge_dictionaries(dict1, *other_dicts):
    for dict in other_dicts:
        dict1.update(dict)
    return dict1
'''
-----------------------------------------------------------------


Prompt:

- Write a function named prime_factors that accepts a whole number greater than one (1) as an argument and returns an list of that argument's prime factors.
- The prime factors of a whole number are the prime numbers that, when multiplied together, equals the whole number.
- If the argument provided is not greater than 1, or not a whole number, then primeFactors should return an empty list.

Examples:

prime_factors(2) //=> [2]
prime_factors(3) //=> [3]
prime_factors(4) //=> [2, 2]
prime_factors(18) //=> [2, 3, 3]
prime_factors(29) //=> [29]
prime_factors(105) //=> [3, 5, 7]
prime_factors(200) //=> [2, 2, 2, 5, 5]

-----------------------------------------------------------------
'''

def prime_factors(num):
    arr =[]
    
    if num <= 0:
        return None
    
    for i in range(0, num):
        if i == 0 or i == 1:
            continue
        if i == 2:
            arr.append(i)
        
        if num % i == 0:
            arr.append(i)

    return arr


#! googled answer refactored to return a list
import math


def primeFactors(n):
    list1 = []
    while n % 2 == 0:
        list1.append(2)
        n = n / 2
    # n reduces to become odd
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        # while i divides n
        while n % i == 0:
            list1.append(i)
            n = n / i
    # if n is a prime
    if n > 2:
        list1.append(n)

    return list1

# print(primeFactors(2))
# print(primeFactors(3))
# print(primeFactors(4))
# print(primeFactors(18))
# print(primeFactors(29))
# print(primeFactors(105))
# print(primeFactors(200))


## 30Sep22 --- 1. **Create Phone Number**
# Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) // => returns "(123) 456-7890"

def create_phone_number(arr):
    if len(arr) != 10:
        return "Not a valid phone number"
    
    arr.insert(0, "(")
    arr.insert(4, ")")
    arr.insert(5, " ")
    arr.insert(9, '-')
    
    new_list =[]
    for num in arr:
        new_list.append(str(num))
    
    return "".join(new_list)

print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))

#! Troy's Answer
import re
def create_phone_number2(nums):
    if len(nums) != 10:
        return "Not a valid phone number"
    stringify_nums = ''
    for num in nums:
        stringify_nums += str(num)
    
    return re.sub(r'(\d{3})(\d{3})(\d{4})', r'(\1) \2-\3', stringify_nums)

print(create_phone_number2([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))

#! Python Method
from colormap import rgb2hex
from colormap import hex2rgb

print(rgb2hex(255, 255, 255))
print(hex2rgb('#FFFFFF'))


## 2. **RGB To Hex Conversion**
# The RGB function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

# **Note**: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

# rgb(255, 255, 255) // returns FFFFFF
# rgb(255, 255, 300) // returns FFFFFF
# rgb(0,0,0) // returns 000000
# rgb(148, 0, 211) // returns 9400D3

def rgb(*args):
    hex = []
    
    for num in args:
        first = num // 16
        second = num % 16
        if first == 10: first = "A"
        elif first == 11: first = "B"
        elif first == 12: first = "C"
        elif first == 13: first = "D"
        elif first == 14: first = "E"
        elif first == 15: first = "F"
        else: first = str(first)
        if second == 10: second = "A"
        elif second == 11: second = "B"
        elif second == 12: second = "C"
        elif second == 13: second = "D"
        elif second == 14: second = "E"
        elif second == 15: second = "F"
        else: second = str(second)
        hex.append(first)
        hex.append(second)
    
    return "".join(str(x) for x in hex)

print(rgb(255, 255, 255))

#! Eric's Answer
def rgb2(r, g, b):
    double_digits = {
        10: "A",
        11: "B",
        12: "C",
        13: "D",
        14: "E",
        15: "F"
    }
    hex_conversion= ''
    arr = [r,g,b]
    for num in arr:
        if num > 255:
            num = 255
        elif num < 0:
            num =0
        whole_number = num //16
        remainder = num % 16
        if whole_number < 10:
            hex_conversion += str(whole_number)
        else:
            hex_conversion += double_digits[whole_number]
        if remainder < 10:
            hex_conversion += str(remainder)
        else:
            hex_conversion += double_digits[remainder]
    return hex_conversion

print(rgb2(255, 255, 255))