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




print(reverse_string('Go-to-the-store'))
print(reverse_string('Jump-jump-for-joy'))


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
    

print(is_prime(2))
print(is_prime(29))
print(is_prime(3))
print(is_prime(4))
print(is_prime(200))

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

print(find_the_parity_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))
print(find_the_parity_outlier([160, 3, 1719, 19, 11, 13, -21]))