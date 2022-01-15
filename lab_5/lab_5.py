import numpy as np

#1
# x = np.array(np.random.randint(100, size=(36)))
# x2 = np.array(np.random.randint(100, size=(3,36)))
# x3 = np.array(np.random.randint(100, size=(3,3,3)))

#2
# 2D
# for i in range(1, 36):
#     j = 36 / i
#     if (j.is_integer()):
#         xn = x.reshape(i, int(j))
#         print(xn)

# 3d
x = np.array([2, 5, 6, 6])
for i in range(1, len(x) + 1):
    j = len(x) / i
    if j.is_integer():
        for k in range(1, len(x) + 1):
            j2 = len(x) / k
            if j2.is_integer: 
                if j * j2 * i == len(x):
                    xn = x.reshape(i, int(j), int(j2))
                    print(xn)
                    print("====")

#4
# x = np.random.randint(0, 100, size=36)
# x2 = np.divide(x, 2)
# x3 = [i for i in x2 if not (i%1)]

#5
# x = np.random.randint(0, 100, size=(5, 3))
# x2 = np.random.randint(0, 100, size=(3, 5))
# print(np.dot(x, x2))

#6
# x = np.random.randint(0, 100, size=(6))
# x2 = np.random.randint(0, 100, size=(3))
# print(np.concatenate((x, x2)))

#7
# x = np.random.randint(0, 100, size=(6))
# x2 = np.random.randint(0, 100, size=(6))
# print(np.outer(x, x2))
# print(np.inner(x, x2))

#8
# x = np.array([])
# for i in range(3):
#     n = int(input())
#     x = np.append(x, n)
# print(np.sqrt(x))