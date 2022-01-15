x = []
res = []
def check(num):
    d = []
    for i in range(2, num//2 + 1):
        if len(d) > 2:
            return 0
        if num % i == 0:
            d.append(i)
    if len(d) == 2 and 7 in d:
        return 1
    return 0

for i in range(10, 3000):
    if check(i):
        res.append(i)
    
