import random as rn
nums = ""
results = {}
len = rn.randint(1, 10)

for i in range(0, len):
    nums += str(round(rn.uniform(0, 5), 2)) + "-"
nums = nums[:-1]

for x in [float(i) for i in nums.split("-")]:
    results[x] = 2 * x - 1

with open("2.txt", "w") as f:
    for i in results:
        f.write(str(i))
        f.write(" - ")
        f.write(str(results[i]))
        f.write("\n")