# Need to work on thiss


string = input()
print(len(string))
string1 = ""

for item in range(0, len(string)):
    if string[item].islower() == True:
        string1 += string[item].upper()
    else:
        string1 += string[item].lower()

print(string1)
