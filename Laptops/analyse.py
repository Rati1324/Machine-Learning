import pandas as pd
from sklearn import linear_model
import numpy as np
import matplotlib.pyplot as plt

#multiple regression
data = pd.read_excel("data.xls")
X = data[['storage', 'ram']]
y = data['price']
model = linear_model.LinearRegression()
model.fit(X, y)

# predicted = model.predict([[500, 8]])
# print(np.round(predicted))
print(model.coef_)

# model = np.poly1d(np.polyfit(data.ram, data.price, 3))
# line = np.linspace(4, 32, 10000)
# plt.scatter(data.ram, data.price)
# plt.plot(line, model(line))
# plt.show()
