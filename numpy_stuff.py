import numpy as np
#1
# x = np.random.randint(100, size=(5))
# x2 = np.array([2, 4, 5, 6, 7])
# print(np.add(x, x2))

#2
# x = np.array([[2, 3, 4], [2, 4, 6], [5, 6, 7]])
# x2 = np.random.randint(10, size=(3, 3))
# np.add(x, x2)

#17
# x = np.random.randint(10, size=(2,2))
# x1 = np.random.randint(10, size=(2,2))
# print(np.multiply(x, x1))

#20
# x = np.random.randint(10, size=(2, 2))
# x2 = np.delete(x, 1, 0)

#21 replace all the 2s
# x = np.array([2, 4, 5, 2, 6])
# x2 = np.where(x==2)
# for i in x2:
#     x[i] = 0

# 23
# x = np.random.randint(10, size=(5, 5))
# x = x.reshape(-1)
# x = x.flatten()

# fill with zereos
# x = np.zeros((6), dtype=int)

# filtering
# x = np.random.randint(3, size=5)
# filter = []

# for i in x:
#     if (i == 2):
#         filter.append(True)
#     else:
#         filter.append(False)
# newarr = x[filter]