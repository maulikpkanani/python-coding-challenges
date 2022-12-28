https://edabit.com/challenges/python3

Flip the Boolean
Create a function that reverses a boolean value and returns the string "boolean expected" if another variable type is given.
Examples
reverse(True) ➞ False
reverse(False) ➞ True
reverse(0) ➞ "boolean expected"
reverse(None) ➞ "boolean expected"

def reverse(arg):
    if type(arg) != bool:
        return "boolean expected"
    elif arg == False:
        return True
    else:
        return False
=====================
Write a function that finds the sum of the first n natural numbers. Make your function recursive.
Examples
sum_numbers(5) ➞ 15
# 1 + 2 + 3 + 4 + 5 = 15
sum_numbers(1) ➞ 1
sum_numbers(12) ➞ 78

def sum_numbers(n):
    if n == 1:
        return 1
    else:
        return n + sum_numbers(n-1)
=====================
Write a function that converts hours into seconds.
def how_many_seconds(hours):
    return hours*60*60
=====================
Given a list of numbers, create a function which returns the list but with each element's index in the list added to itself. This means you add 0 to the number at index 0, add 1 to the number at index 1, etc...
Examples
add_indexes([0, 0, 0, 0, 0]) ➞ [0, 1, 2, 3, 4]
add_indexes([1, 2, 3, 4, 5]) ➞ [1, 3, 5, 7, 9]
add_indexes([5, 4, 3, 2, 1]) ➞ [5, 5, 5, 5, 5]

def add_indexes(lst):
    return [i+val for i, val in enumerate(lst)]
========================
Write a function that takes a list of elements and returns only the integers.
Examples
return_only_integer([9, 2, "space", "car", "lion", 16]) ➞ [9, 2, 16]
return_only_integer(["hello", 81, "basketball", 123, "fox"]) ➞ [81, 123]
return_only_integer([10, "121", 56, 20, "car", 3, "lion"]) ➞ [10, 56, 20, 3]
return_only_integer(["String",  True,  3.3,  1]) ➞ [1]

def return_only_integer(lst):
    my_set = set([i for i in lst if type(i) == int])
    return list(my_set)
=======================
Create a function that squares every digit of a number.
Examples
square_digits(9119) ➞ 811181
square_digits(2483) ➞ 416649
square_digits(3212) ➞ 9414

def square_digits(n):
    lst =(str(n))
    estr = ''
    for i in lst:
        estr += str(int(i)**2)
    return int(estr)

def square_digits(n):
    return int(''.join(str(int(i)**2) for i in str(n)))
======================
Write a function that stutters a word as if someone is struggling to read it. The first two letters are repeated twice with an ellipsis ... and space after each, and then the word is pronounced with a question mark ?.
Examples
stutter("incredible") ➞ "in... in... incredible?"
stutter("enthusiastic") ➞ "en... en... enthusiastic?"

def stutter(word):
    return f"{word[:2]}.. {word[:2]}.. {word}?"
    #return word[:2]+"... "+word[:2]+"... "+word+"?"
======================
Create a function that takes a number as input and returns True if the sum of its digits has the same parity as the entire number. Otherwise, return False.
Examples
parity_analysis(243) ➞ True
# 243 is odd and so is 9 (2 + 4 + 3)
parity_analysis(12) ➞ False
# 12 is even but 3 is odd (1 + 2)
parity_analysis(3) ➞ True
# 3 is odd and 3 is odd and 3 is odd (3)

def parity_analysis(num):
    digit_sum = sum(map(int, str(num)))
    return num %2 == digit_sum %2
========================
Create a function which concatenates the number 7 to the end of every chord in a list. Ignore all chords which already end with 7.
Examples
jazzify(["G", "F", "C"]) ➞ ["G7", "F7", "C7"]
jazzify(["Dm", "G", "E", "A"]) ➞ ["Dm7", "G7", "E7", "A7"]
jazzify(["F7", "E7", "A7", "Ab7", "Gm7", "C7"]) ➞ ["F7", "E7", "A7", "Ab7", "Gm7", "C7"]
jazzify([]) ➞ []

def jazzify(lst):
    final_lst = []
    if len(lst) != 0:
        for i in lst:
            if i.endswith('7'):
                final_lst.append(i)
            else:
                final_lst.append(i+'7')
        return final_lst
    else:
        return []
def jazzify(lst):
    if len(lst) != 0:
        return [i if i.endswith('7') else i+'7' for i in lst]
    else:
        return []
==============================
Create a function that ends the first word of a phrase with "ed", essentially verbifying a noun.
Examples
verbify("cheese burger") ➞ "cheesed burger"
verbify("salt water") ➞ "salted water"
verbify("orange juice") ➞ "oranged juice"
verbify("shredded cheese") ➞ "shredded cheese"

def verbify(txt):
    strlst = txt.split( )
    if strlst[0].endswith('ed'):
        #return f"{strlst[0]} {strlst[1]}"
        return "{} {}".format(strlst[0],strlst[1])
    elif strlst[0].endswith('e'):
        #return f"{strlst[0]+'d'} {strlst[1]}"
        return "{} {}".format(strlst[0]+'d',strlst[1])
    else:
        #return f"{strlst[0]+'ed'} {strlst[1]}"
         return "{} {}".format(strlst[0]+'ed',strlst[1])
========================
Given a list of numbers, return a list which contains all the even numbers in the original list, which also have even indices.
Examples
get_only_evens([1, 3, 2, 6, 4, 8]) ➞ [2, 4]
get_only_evens([0, 1, 2, 3, 4]) ➞ [0, 2, 4]
get_only_evens([1, 2, 3, 4, 5]) ➞ []

def get_only_evens(nums):
    lst = []
    for i, num in enumerate(nums):
        if num%2 == i%2 == 0:
            lst.append(num)
        else:
            lst
    return lst
def get_only_evens(nums):
	return [i for i in nums[::2] if i%2==0]

