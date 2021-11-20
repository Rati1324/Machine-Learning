import random as rn

x = [rn.randint(2, 15) for i in range(20)]
print(x)
counts = [x.count(i) for i in x]
print(f"yvelaze xshirad ganmeorebadi: {x[counts.index(max(counts))]}")

xd = []
[xd.append(i) for i in x if i not in xd]
print(x)
print(xd)
