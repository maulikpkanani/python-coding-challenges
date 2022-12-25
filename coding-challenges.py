https://edabit.com/challenges/python3

1.Flip the Boolean
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
2.Write a function that finds the sum of the first n natural numbers. Make your function recursive.
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

