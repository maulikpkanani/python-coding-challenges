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
2.
