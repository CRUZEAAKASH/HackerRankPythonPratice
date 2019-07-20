# Need to work on this

string = input()

if string.isalnum():
    print(True)
if any(c.isalpha() for c in string):
    print(True)
if string.isdigit():
    print(True)
if string.islower():
    print(True)
if string.isupper():
    print(True)
