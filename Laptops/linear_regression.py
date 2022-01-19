import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

data = pd.read_excel("data.xls")
X = np.array(data.ram).reshape(-1, 1)
y = np.array(data.price).reshape(-1, 1)

model = LinearRegression()
model.fit(X, y)

print(model.score(X, y))