import numpy as np
import matplotlib.pyplot as mplot
import scipy.stats as stats
age = [23, 24, 26, 27, 35]
salary = [200, 210, 220, 235, 240]
# mplot.scatter(age, salary)
# mplot.show()
slope, intercept, r, d, std_err = stats.linregress(age, salary)
print(slope, intercept, r, std_err)
print(f"Guy who's 25 makes: {slope * 25 + intercept}")