import random as rn
x = {}
sum = 0

for i in range(10):
    for j in range(10):
        sum += rn.randint(1, 100)
    # pythonshi key ver iqneba listi amitom ubralod ricxvebi gamoviyene
    x[i] = sum
    sum = 0
print(max(x))

print(x)
    