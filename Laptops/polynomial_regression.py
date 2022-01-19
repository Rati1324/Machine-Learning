import pandas as pd
import numpy as np
from sklearn.metrics import r2_score
data = pd.read_excel('data.xls')

x = data['ram']
y = data['price']

model = np.poly1d(np.polyfit(x, y, 3))
line = np.linspace(2, 95, 100)
print(r2_score(y, model(x)))