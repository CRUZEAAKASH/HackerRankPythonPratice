# Need to work on thiss



string = input()
print(len(string))

for item in range(0, len(string)):
    if string[item].islower() == True:
        string[item] = string[item].upper()
    else:
        string[item] = string[item].lower()

print(string)
