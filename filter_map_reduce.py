'''
@author: Shivam Mishra
@date: 23-12-21 05:58 PM
@dsec: practice problems for filter, map and reduce
'''

# filter numbers that are greater than 0
numbers = [-2, -1, 0, 1, 2]
greater_numbers = filter(lambda num: num > 0, numbers)
print(list(greater_numbers))


# Using a user-defined function
def is_positive(n):
    return n > 0


positive_numbers = list(filter(is_positive, numbers))
print(positive_numbers)


# check number is palindrome
def is_palindrome(word):
    reversed_word = "".join(reversed(word))
    return word.lower() == reversed_word.lower()


words = ("filter", "Ana", "hello", "world", "madam", "racecar")


palindrome_words = list(filter(is_palindrome, words))
print(palindrome_words)

#############################################################################
# find length of words in list
lst = ["Greenland", "Japan", "Taiwan", "Botswana", "Bhutan", "Tuvalu"]
lst2 = map(len, lst)
print(list(lst2))

# convert float to int
lst = [87.9983729183943, 88.27381223193, 88.01283119001, 90.3166247903554, 89.94283229101, 100.00000000001]

new_lst = map(int, lst)
print(list(new_lst))

# reverse the string
lst = ["Greenland", "Japan", "Taiwan", "Botswana", "Bhutan", "Tuvalu"]
new_lst = map("".join, map(reversed, lst))
for i in new_lst:
    print(i)

# find percentage of each value
lst = [2.54, 4.0, 3.0, 9.95, 5.4]
new_lst = map(lambda x: x/100, lst)

print(list(new_lst))

# format the string
lst = [2.54, 4.0, 3.0, 9.95, 5.4]
new_lst1 = map("{:,.2f}".format, map(lambda x: x/100, lst))
for i in new_lst1:
    print(i)


# using filter and map to store only numbers less than 100 after squaring them
lst = [1, 4, 9, 11, 400]
a = filter(lambda x: x < 100, map(lambda x: x**2, lst))

print(list(a))

########################################################################################
from functools import reduce


# add all elements of list
def my_add(x, y):
    return x+y


numbers = [0, 1, 2, 3, 4]
num_sum = reduce(my_add, numbers)
print(num_sum)

# applying lambda function
numbers = [1, 2, 3, 4]
num = reduce(lambda a, b: a * b, numbers, 50)
print(num)


# find minimum and maximum
numbers = [3, 5, 2, 4, 7, 1]

# Minimum
min_num = reduce(lambda a, b: a if a < b else b, numbers)
# Maximum
max_num = reduce(lambda a, b: a if a > b else b, numbers)
print(min_num,max_num)
