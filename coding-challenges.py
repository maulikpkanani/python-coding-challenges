https://edabit.com/challenges/python3
Easy-->Language fundamentals

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
==========================
Create a function that takes in a current mood and return a sentence in the following format: "Today, I am feeling {mood}". However, if no argument is passed, return "Today, I am feeling neutral".
Examples
mood_today("happy") ➞ "Today, I am feeling happy"
mood_today("sad") ➞ "Today, I am feeling sad"
mood_today() ➞ "Today, I am feeling neutral"

def mood_today(mood='neutral'):
    if not mood:
        return 'Today, I am feeling mood'
    else:
        return 'Today, I am feeling {}'.format(mood)
==========================
Given an unsorted list, create a function that returns the nth smallest integer (the smallest integer is the first smallest, the second smallest integer is the second smallest, etc).
Examples
nth_smallest([1, 3, 5, 7], 1) ➞ 1
nth_smallest([1, 3, 5, 7], 3) ➞ 5
nth_smallest([1, 3, 5, 7], 5) ➞ None
nth_smallest([7, 3, 5, 1], 2) ➞ 3

def nth_smallest(lst, n):
    sorted_list = sorted(lst)
    if len(lst) >= n:
        return sorted_list[n-1]
    else:
        return None
==========================
Create a function that returns the frequency distribution of a list. This function should return an object, where the keys are the unique elements and the values are the frequency in which those elements occur.
Examples
get_frequencies(["A", "B", "A", "A", "A"]) ➞ { "A" : 4, "B" : 1 }
get_frequencies([1, 2, 3, 3, 2]) ➞ { 1: 1, 2: 2, 3: 2 }
get_frequencies([True, False, True, False, False]) ➞ { True: 2, False: 3 }
get_frequencies([]) ➞ {}

def get_frequencies(lst):
        d = {}
        for i in lst:
            d[i] = lst.count(i)
        return d
=============================
Create a function that returns a list of strings sorted by length in ascending order.
Examples
sort_by_length(["a", "ccc", "dddd", "bb"]) ➞ ["a", "bb", "ccc", "dddd"]
sort_by_length(["apple", "pie", "shortcake"]) ➞ ["pie", "apple", "shortcake"]
sort_by_length(["may", "april", "september", "august"]) ➞ ["may", "april", "august", "september"]
sort_by_length([]) ➞ []

def sort_by_length(lst):
	return sorted(lst, key=len)
===================
Remove enemies from the list of people, even if the enemy shows up twice.
Examples
remove_enemies(["Fred"], []) ➞ ["Fred"]
remove_enemies(["Adam", "Emmy", "Tanya", "Emmy"], ["Emmy"]) ➞ ["Adam", "Tanya"]

def remove_enemies(names, enemies):
	#return [i for i in names if i not in enemies]
	return filter(lambda i:i not in enemies,names)
============================
Write a function that creates a dictionary with each (key, value) pair being the (lower case, upper case) versions of a letter, respectively.
Examples
mapping(["p", "s"]) ➞ { "p": "P", "s": "S" }
mapping(["a", "b", "c"]) ➞ { "a": "A", "b": "B", "c": "C" }
mapping(["a", "v", "y", "z"]) ➞ { "a": "A", "v": "V", "y": "Y", "z": "Z" }

def mapping(letters):
    return {i:i.upper() for i in letters}
===========================
Create a function which validates whether a 3 character string is a vowel sandwich. In order to have a valid sandwich, the string must satisfy the following rules:
The first and last characters must be a consonant.
The character in the middle must be a vowel.
Examples
is_vowel_sandwich("cat") ➞ True
is_vowel_sandwich("ear") ➞ False
is_vowel_sandwich("bake") ➞ False
is_vowel_sandwich("try") ➞ False

def is_vowel_sandwich(s):
    v = 'aeiou'
    return len(s) == 3 and s[1] in v and s[0] not in v and s[-1] not in v
import re
def is_vowel_sandwich(s):
	return bool(re.match(r'[^aeiou][aeiou][^aeiou]\Z', s))
=============================
Create a function that returns the number of arguments it was called with.
Examples
num_args() ➞ 0
num_args("foo") ➞ 1
num_args("foo", "bar") ➞ 2
num_args(True, False) ➞ 2
num_args({}) ➞ 1

def num_args(*args):
    return len(args)
=========================
Write a function that searches a list of names (unsorted) for the name "Bob" and returns the location in the list. If Bob is not in the list, return -1.
Examples
find_bob(["Jimmy", "Layla", "Bob"]) ➞ 2
find_bob(["Bob", "Layla", "Kaitlyn", "Patricia"]) ➞ 0
find_bob(["Jimmy", "Layla", "James"]) ➞ -1

def find_bob(names):
    try:
        return names.index("Bob")
    except:
        return -1
=======================
Create a function that returns True if the given string has any of the following:
Only letters and no numbers.
Only numbers and no letters.
If a string has both numbers and letters, or contains characters which don't fit into any category, return False
Examples
alphanumeric_restriction("Bold") ➞ True
alphanumeric_restriction("123454321") ➞ True
alphanumeric_restriction("H3LL0") ➞ False
alphanumeric_restriction("ed@bit") ➞ False

def alphanumeric_restriction(s): 
    return s.isalpha() or s.isnumeric()
=======================
Create a function that squares every digit of a number.
Examplessquare_digits(9119) ➞ 811181
square_digits(2483) ➞ 416649
square_digits(3212) ➞ 9414

def square_digits(n):
    strn = str(n)
    strs = ''
    for i in strn:
        strs += str((int(i)**2))
    return int(strs)
======================
Write a function that finds the sum of the first n natural numbers. Make your function recursive.
Examples
sum_numbers(5) ➞ 15
# 1 + 2 + 3 + 4 + 5 = 15
sum_numbers(1) ➞ 1
sum_numbers(12) ➞ 78

def sum_numbers(n):
    if n == 1:
        return n
    else:
        return (n + sum_numbers(n-1))
==========================
Create a function to calculate how many characters in total are needed to make up the shape. You will be given a list of strings which make up a shape in the compiler (i.e. a square, a rectangle or a line).
Examples
count_characters([
  "###",
  "###",
  "###"
]) ➞ 9
count_characters([
  "22222222",
  "22222222",
]) ➞ 16
count_characters([
  "------------------"
]) ➞ 18
count_characters([]) ➞ 0
count_characters(["", ""]) ➞ 0

def count_characters(lst):
    return len(''.join(lst))
==============================
Given a string of numbers separated by a comma and space, return the product of the numbers.
Examples
multiply_nums("2, 3") ➞ 6
multiply_nums("1, 2, 3, 4") ➞ 24
multiply_nums("54, 75, 453, 0") ➞ 0
multiply_nums("10, -2") ➞ -20

def multiply_nums(nums):
    return eval(nums.replace(',', '*'))
================================
Given an unsorted list, create a function that returns the nth smallest integer (the smallest integer is the first smallest, the second smallest integer is the second smallest, etc).
Examples
nth_smallest([1, 3, 5, 7], 1) ➞ 1
nth_smallest([1, 3, 5, 7], 3) ➞ 5
nth_smallest([1, 3, 5, 7], 5) ➞ None
nth_smallest([7, 3, 5, 1], 2) ➞ 3

def nth_smallest(lst, n):
    if n > len(lst):
        return None
    else:
        lst.sort()
        return lst[n-1]
================================
Imagine a school that kids attend for 6 years. In each year, there are five groups started, marked with the letters a, b, c, d, e. For the first year, the groups are 1a, 1b, 1c, 1d, 1e and for the last year, the groups are 6a, 6b, 6c, 6d, 6e.
Write a function that returns the groups in the school by year (as a string), separated with a comma and a space in the form of "1a, 1b, 1c, 1d, 1e, 2a, 2b (....) 5d, 5e, 6a, 6b, 6c, 6d, 6e".
Examples
print_all_groups() ➞ "1a, 1b, 1c, 1d, 1e, 2a, 2b, 2c, 2d, 2e, 3a, 3b, 3c, 3d, 3e, 4a, 4b, 4c, 4d, 4e, 5a, 5b, 5c, 5d, 5e, 6a, 6b, 6c, 6d, 6e "
Notes:Use nested "for" loops to achieve this, as well as the array of ["a", "b", "c", "d", "e"] groups

def print_all_groups():
    resultstr = ""
    groups = ["a", "b", "c", "d", "e"]
    for i in range(1,7):
        for j in groups:
            resultstr += "{}{}, ".format(i,j)
    return resultstr[:-2]
==================================
Given a list of directions to spin, "left" or "right", return an integer of how many full 360° rotations were made. Note that each word in the list counts as a 90° rotation in that direction.
Worked Example
spin_around(["right", "right", "right", "right", "left", "right"]) ➞ 1
# You spun right 4 times (90 * 4 = 360)
# You spun left once (360 - 90 = 270)
# But you spun right once more to make a full rotation (270 + 90 = 360)
Examples
spin_around(["left", "right", "left", "right"]) ➞ 0
spin_around(["right", "right", "right", "right", "right", "right", "right", "right"]) ➞ 2
spin_around(["left", "left", "left", "left"]) ➞ 1

def spin_around(lst):
    return abs(lst.count('right')-lst.count('left'))//4
==================================
Write a function that searches a list of names (unsorted) for the name "Bob" and returns the location in the list. If Bob is not in the list, return -1.
Examples
find_bob(["Jimmy", "Layla", "Bob"]) ➞ 2
find_bob(["Bob", "Layla", "Kaitlyn", "Patricia"]) ➞ 0
find_bob(["Jimmy", "Layla", "James"]) ➞ -1

def find_bob(names):
    return names.index('Bob') if 'Bob' in names else -1
===================================
Write a function that returns the boolean True if the given two lists do not share any numbers, and False otherwise.

def not_share(lst1, lst2):
    return not  set(lst1) & set(lst2)
==================================
Write a function that takes a string, breaks it up and returns it with vowels first, consonants second. For any character that's not a vowel (like special characters or spaces), treat them like consonants.
Examples
split("abcde") ➞ "aebcd"
split("Hello!") ➞ "eoHll!"
split("What's the time?") ➞ "aeieWht's th tm?"
Notes
Vowels are a, e, i, o, u.
Define a separate is_vowel() function for easier to read code (recommendation).

def split(txt):
	return ''.join(sorted(txt, key=lambda x: x.lower() not in 'aeiou'))
================================
Create a function that returns the frequency distribution of a list. This function should return an object, where the keys are the unique elements and the values are the frequency in which those elements occur.
Examples
get_frequencies(["A", "B", "A", "A", "A"]) ➞ { "A" : 4, "B" : 1 }
get_frequencies([1, 2, 3, 3, 2]) ➞ { 1: 1, 2: 2, 3: 2 }
get_frequencies([True, False, True, False, False]) ➞ { True: 2, False: 3 }
get_frequencies([]) ➞ {}

def get_frequencies(lst):
    counter = {}
    for i in lst:
        if i not in counter:
            counter[i] = 1
        else:
            counter [i] += 1
    return counter
================================
Create a function that changes specific words into emoticons. Given a sentence as a string, replace the words smile, grin, sad and mad with their corresponding emoticons.
word	emoticon
smile	:D
grin	:)
sad	:(
mad	:P
Examples
emotify("Make me smile") ➞ "Make me :D"
emotify("Make me grin") ➞ "Make me :)"
emotify("Make me sad") ➞ "Make me :("

def emotify(txt):
    d = {
        'smile': ':D',
        'grin':':)',
        'sad':':(',
        'mad':':P'
    }
    for k, v in d.items():
        txt = txt.replace(k,v)
    return txt
================================
Create a function that takes a string as the first argument, and a (string) specification as a second argument. If the specification is "word", return a string with each word reversed while maintaining their original order. If the specification is "sentence", reverse the order of the words in the string, while keeping the words intact.
Examples
txt = "There's never enough time to do all the nothing you want"
flip("Hello", "word") ➞ "olleH"
flip("Hello", "sentence") ➞ "Hello"
flip(txt, "word") ➞ "s'erehT reven hguone emit ot od lla eht gnihton uoy tnaw"
flip(txt, "sentence") ➞ "want you nothing the all do to time enough never There's"

def flip(txt, spec):
    if spec == 'sentence':
        finaltxt = ' '.join(txt.split()[::-1])
    else:
        finaltxt = ' '.join([i[::-1] for i in txt.split()])
    return finaltxt
===================================
Given a square matrix (i.e. same number of rows as columns), its trace is the sum of the entries in the main diagonal (i.e. the diagonal line from the top left to the bottom right).
As an example, for:
[
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
... the trace is 1 + 5 + 9 = 15.
Write a function that takes a square matrix and computes its trace.

def trace(lst):
    trace = 0
    for i in range(len(lst)):
        trace += (lst[i][i])
    return trace

def trace(lst):
    return sum(lst[i][i] for i in range(len(lst)))
================================
Given a string indicating a range of letters, return a string which includes all the letters in that range, including the last letter. Note that if the range is given in capital letters, return the string in capitals also!
Examples
gimme_the_letters("a-z") ➞ "abcdefghijklmnopqrstuvwxyz"
gimme_the_letters("h-o") ➞ "hijklmno"
gimme_the_letters("Q-Z") ➞ "QRSTUVWXYZ"
gimme_the_letters("J-J") ➞ J"

def gimme_the_letters(spectrum):
    lowerstr = 'abcdefghijklmnopqrstuvwxyz'
    capstr = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    speclst = spectrum.split('-')
    if speclst[0] in capstr:
        index1 = capstr.index(speclst[0])
        index2 = capstr.index(speclst[1]) + 1
        return (capstr[index1:index2])
    else:
        index1 = lowerstr.index(speclst[0])
        index2 = lowerstr.index(speclst[1]) + 1
        return (lowerstr[index1:index2])
=================================
Given a number between 1-26, return what letter is at that position in the alphabet. Return "invalid" if the number given is not within that range, or isn't an integer.
Examples
letter_at_position(1) ➞ "a"
letter_at_position(26.0) ➞ "z"
letter_at_position(0) ➞ "invalid"
letter_at_position(4.5) ➞ "invalid"

def letter_at_position(n):
    chars = 'abcdefghijklmnopqrstuvwxyz'
    if n not in range(1, len(chars)+1):
        return 'invalid'  
    else:
        return (chars[int(n)-1])
==================================
Create two functions: a left-shift function and a right-shift function. Each function will take in a list and a single parameter: the number of shifts.
[1, 2, 3, 4, 5]
[2, 3, 4, 5, 1]  # left shift of 1
[5, 1, 2, 3, 4]  # left shift of 4
[5, 1, 2, 3, 4]  # right shift of 1
[3, 4, 5, 1, 2]  # right shift of 3
Examples
left_shift([1, 2, 3, 4], 1) ➞ [2, 3, 4, 1]
right_shift([1, 2, 3, 4], 1) ➞ [4, 1, 2, 3]
left_shift([1, 2, 3, 4, 5], 3) ➞ [4, 5, 1, 2, 3]
left_shift([1, 2, 3, 4, 5], 5) ➞ [1, 2, 3, 4, 5]
# You have fully shifted the list, you end up back where you began.
left_shift([1, 2, 3, 4, 5], 6) ➞ [2, 3, 4, 5, 1]
# You should be able to take in numbers greater than the length.
# Think of the length of the list as a modulo.

def left_shift(lst, n):
	n = n % len(lst) 
	return lst[n:] + lst[:n]

def right_shift(lst, n):
	n = n % len(lst) 
	return lst[-n:] + lst[:-n]
=======================================
Is Prime 
def is_prime(n):
    if n < 2:
        return False:
    for i in range(2, n):
        if n%i == 0:
            return False
        return True
========================================
Create a function that finds the highest integer in the list using recursion.
Examples
find_highest([-1, 3, 5, 6, 99, 12, 2]) ➞ 99
find_highest([0, 12, 4, 87]) ➞ 87
def find_highest(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        r = find_highest(lst[1:])
        if r >= lst[0]:
            return r
        else lst[0]
======================================
Write a function that returns the longest sequence of consecutive zeroes in a binary string.
Examples
longest_zero("01100001011000") ➞ "0000"
longest_zero("100100100") ➞ "00"
longest_zero("11111") ➞ ""
def longest_zero(s):
    return sorted( s.split('1'))[-1] if '0'  in s else ''  
=====================================