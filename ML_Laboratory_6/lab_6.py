import pandas as pd
import string, random
from openpyxl import load_workbook
import xlsxwriter

writer = pd.ExcelWriter('ML/ML_Laboratory_6/data.xlsx', engine='xlsxwriter')

#1
x = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
x2 = random.sample(range(0, 10), 1)[0]
x3 = random.sample(range(1, 7), 1)[0]
x4 = random.sample(range(1, 100), 1)[0]

df1 = pd.DataFrame([[x, x2, x3, x4]], 
                    columns=['col 1', 'col 2', 'col 3', 'col 4'])
df1.to_excel(writer, index=True, sheet_name="Sheet_1")

#2
f_name = ['mari', 'ana', 'dato', 'gio']
l_name = ['maridze', 'anadze', 'datodze', 'giodze']

data = []
nums = random.sample(range(1, 100), 50)

for i in range(50):
    data.append([])
    data[i].append(nums[i])
    data[i].append(f_name[random.randint(0, len(f_name) - 1)])
    data[i].append(l_name[random.randint(0, len(l_name) - 1)])
    data[i].append(random.sample(range(2000, 5000), 1)[0])

df2 = pd.DataFrame(data,
                    columns=['col 1', 'col 2', 'col 3', 'col 4'])

df2.to_excel(writer, index=True, sheet_name="Sheet_2")
writer.save()