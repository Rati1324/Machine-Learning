import pandas as pd
import string, random
from openpyxl import load_workbook
import xlsxwriter

writer = pd.ExcelWriter('ML/ML_Laboratory_6/data.xlsx', engine='xlsxwriter')

df = pd.DataFrame([[1, 2, 3]], columns=['col1', 'col2', 'col3'])
df.to_excel(writer, sheet_name="sheet_1", index=True)

df2 = pd.DataFrame([[4, 5, 6]], columns=['col4', 'col5', 'col6'])
df2.to_excel(writer, sheet_name="sheet_2", index=True)
writer.save()