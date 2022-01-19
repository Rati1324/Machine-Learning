import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

data = pd.read_excel('data.xls')

X = data[['ram', 'storage', 'cores', 'thread', 'cpu_speed', 'max_cpu_speed']]
y = data['price']

model = linear_model.LinearRegression()
model.fit(X, y)

print(f"Mean of rams: {round(np.mean(X['ram']))}")
print(f"Standard deviation of rams: {round(np.std(X['ram']))}")
print(f"50th percentile of rams: {round(np.percentile(X['ram'], 50))}")
print(f"Standard deviation of rams: {round(np.std(X['ram']))}")

print(model.score(X, y))
print(model.predict([[8, 256, 2, 4, 2100, 4100]]))