string = input()
substring = input()
count = 0
for i in range(0, len(string)):
    if string[i:].startswith(substring):
        count += 1
print(count)
