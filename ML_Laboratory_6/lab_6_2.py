import pandas as pd
import xlsxwriter, openpyxl, numpy

writer = pd.ExcelWriter('Machine-Learning/ML_Laboratory_6/datanew.xlsx', engine='openpyxl')
writer2 = pd.ExcelWriter('Machine-Learning/ML_Laboratory_6/staff_age.xlsx', engine='openpyxl')
df = pd.read_excel('Machine-Learning/ML_Laboratory_6/data.xlsx', sheet_name="Sheet_1")

#3
# df.to_excel(writer, index=True, sheet_name="Sheet_1")
# writer.save()

#4
# s = [i for i in df.loc[0] if 'a' in str(i)][0]
# df2 = pd.DataFrame([[s]], columns=["String with 'a'"])
# df2.to_excel(writer, index=True, sheet_name="Sheet_3")
# writer.save()

#5
# df3 = pd.read_excel('Machine-Learning/ML_Laboratory_6/data.xlsx', sheet_name="Sheet_2")
# nums = max([i for i in df3.loc[3][1:] if type(i) == numpy.int64])

#6
# df4 = pd.read_excel('Machine-Learning/ML_Laboratory_6/file_example_XLSX_1000.xlsx')
# df4 = df4.sort_values("Id").head(55)

#7
df5 = pd.read_excel('Machine-Learning/ML_Laboratory_6/staff_1000.xlsx')
df5 = df5[(df5.Age > 30) & (df5.Age < 40)].head(10)
df5.to_excel(writer2, index=True)
writer2.save()