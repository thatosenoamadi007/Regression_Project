import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# Load the data from a CSV file
data = pd.read_csv("DataSet.csv")
data["Lowest.point"] = pd.factorize(data["Lowest.point"])[0]

#uncomment to remove outliers

"""threshold = 5
z_scores = stats.zscore(data[["TotalArea", "LandArea", "WaterArea", "Lowest.point", "Pop2023"]])
abs_z_scores = np.abs(z_scores)
filtered_entries = (abs_z_scores < threshold).all(axis=1)
data = data[filtered_entries"""

# Select the independent variables
X = data[["TotalArea", "LandArea", "WaterArea", "Lowest.point", "Pop2023"]]

# Select the dependent variable
y = data["Maximum.elevation"]

# Fit the multiple variable regression model
model = LinearRegression().fit(X, y)

# Create the subplots
fig, axes = plt.subplots(nrows=1, ncols=6, figsize=(12, 4))

dt={"TotalArea":"TA", "LandArea":"LA", "Lowest.point":"LP", "Pop2023":"P23", "WaterArea":"WA"}

# Plot scatter plots and regression lines for each variable
axes[0].set_ylabel('ME')
for i, var in enumerate(["TotalArea", "LandArea", "WaterArea", "Lowest.point", "Pop2023"]):
    axes[i].scatter(X[var], y, color='r', alpha=0.5)
    axes[i].scatter(X[var], model.predict(X), color='b', alpha=0.5)
    axes[i].set_xlabel(f"{dt[var]}")
    
    axes[i].set_title(f"{dt[var]} vs ME")

# Show the plots
import matplotlib.pyplot as plt

#plot predicted vs actual

plt.scatter(y, model.predict(X), color='r', alpha=0.5)
plt.xlabel("Actual ME")
plt.ylabel("Predicted ME")
plt.title("Actual vs Predicted ME")
 

plt.tight_layout()
plt.savefig("MultipleRegression_withOutliers.png")
plt.show()
