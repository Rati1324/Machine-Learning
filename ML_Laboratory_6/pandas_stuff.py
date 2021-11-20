import pandas as pd

# mydataset = {
#   'cars': ["BMW", "Volvo", "Ford"],
#   'passings': [3, 7, 2]
# }
# myvar = pd.DataFrame(mydataset)

# print(myvar.loc[0])
# a = mydataset['passings']
# s = pd.Series(a)

excel_data = pd.read_excel('ML/ML_Laboratory_6/staff_1000.xlsx')
# excel_data.dropna(inplace=True)
# excel_data.dropna(subset=["Age"], inplace=True)

# excel_data.loc[2, "Age"] = 2
# print(excel_data.corr())
# print(excel_data.head().to_string())


# excel_data.fillna(25, inplace = True)
# x = excel_data["Age"].mode()[0]
# excel_data["Age"].fillna(x, inplace=True)
