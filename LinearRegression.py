from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Read Six Flags Stock History CSV into DataFrame
six = pd.read_csv("Six Flags Stock.csv")
print("Dimensions of Six Flags DataFrame:", six.shape, end="\n\n")
print(six.head(), end="\n\n")

# Plot relationship between date and closing cost
six.plot("Date", "Close", color="Green", legend=None)
title = "$\\bf{Date}$" + " " + "$\\bf{vs}$" + " " + "$\\bf{Close}$"
plt.title(title)
plt.xlabel("$\\bf{Date}$")
plt.ylabel("$\\bf{Close}$")
plt.xticks(rotation=15)
plt.subplots_adjust(top=0.9, bottom=0.17)

# Plot relationship between opening cost and closing cost
six.plot.scatter("Open", "Close", color="Red", legend=None)
title = "$\\bf{Open}$" + " " + "$\\bf{vs}$" + " " + "$\\bf{Close}$"
plt.title(title)
plt.xlabel("$\\bf{Open}$")
plt.ylabel("$\\bf{Close}$")
plt.subplots_adjust(top=0.9, bottom=0.12)

# Uncomment to show plots
# plt.show()

# Split data with opening cost as input and closing cost as output
x_train, x_test, y_train, y_test = train_test_split(six[["Open"]], six.Close, test_size=0.2)

# Create linear regression model
model = LinearRegression()
model.fit(np.array(x_train), y_train)
prediction = model.predict(np.array(x_test))

# Check model accuracy with r2 score
print("Y_True:", ["{:0.8f}".format(n) for n in np.array(y_test.head())])
print("Y_Pred:", ["{:0.8f}".format(n) for n in np.array(prediction[0:5])])
print("R2 Score:", "%.2f" % r2_score(y_test, prediction))
