import pandas as pd
import openpyxl
import random as rn

writer = pd.ExcelWriter("data.xlsx", engine="openpyxl")

ids = rn.sample(range(1000, 9999), 100)
indexes_id = rn.sample(range(0, len(ids)), 5)
for i in indexes_id:
    ids[i] = ""

dates = []
for i in range(100):
    month = rn.randint(1, 30)
    dates.append(f"{month}-1-2019")
indexes_date = rn.sample(range(0, len(dates)), 5)
for i in indexes_date:
    dates[i] = "NaN"

times = [rn.randint(1, 8) for i in range(100)]
indexes_time = rn.sample(range(0, len(times)), 30)
for i in indexes_time:
    times[i] = ""

hourly = rn.sample(range(10, 110), 100)
indexes_hourly = rn.sample(range(0, len(hourly)), 25)
for i in indexes_hourly:
    hourly[i] = "NaN"

data = []
for i in range(0, 100):
    data.append([])
    data[i].append(ids[i])
    data[i].append(dates[i])
    data[i].append(times[i])
    data[i].append(hourly[i])

df = pd.DataFrame(data,
                    columns = ['col 1', 'col 2', 'col 3', 'col 4'])
df.to_excel(writer, index=True, sheet_name="sheetOne") 
writer.save()