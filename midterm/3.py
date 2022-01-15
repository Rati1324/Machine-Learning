x = input()
valid = 1

for i in x:
    if (not i.isalnum()) and (not i.isspace()):
        valid = 0
        print("invalid input")
        break
    
if valid:
    english = "".join([i for i in x if i.isalpha()])
    num = "".join([i for i in x if i.isnumeric()])
    print(f"{english} - {len(english)}")
    print(f"{num} - {len(num)}")