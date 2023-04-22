import pandas as pd
import csv
from matplotlib import pyplot as plt


with open('DataSet.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader) # Skip the header row
    data = [row for row in reader]


# Extract the relevant data from the loaded data

total_area = [float(row[1]) for row in data]
lowest_point = [row[6] for row in data]
max_elevation = [float(row[5]) for row in data]
lowest_point_num,uniques=pd.factorize(lowest_point)


#define a sinle regression function for total area vs max elevation
x = lowest_point_num
y = max_elevation

'''fig, ax = plt.subplots()
box = ax.boxplot(y)
#plt.savefig("LM_boxplot.png")

# Get the whiskers and caps
# Get the whiskers' data
whiskers_data = [whiskers.get_ydata() for whiskers in box['whiskers']]

# Extract the whiskers' upper and lower values
upper_whiskers = [whiskers[1] for whiskers in whiskers_data]
lower_whiskers = [whiskers[0] for whiskers in whiskers_data]

print("Upper whiskers values:", upper_whiskers)
print("Lower whiskers values:", lower_whiskers)'''

from scipy import stats
import numpy as np
# Calculate the Z-score of each data point 
x_z_scores = stats.zscore(x)
 
# Remove data points with Z-score greater than 3 
threshold = 3
Y_data = [y for y, z in zip(y, x_z_scores) if abs(z) < threshold]
X_data = [x for x, z in zip(x, x_z_scores) if abs(z) < threshold]

print ("removed ", len(y) - len(Y_data), " outliers")
# Calculate the mean of x and y
mean_x = sum(X_data) / len(X_data)
mean_y = sum(Y_data) / len(Y_data)

# Calculate the β1 (coefficient) and β0
numerator = 0
denominator = 0
for i in range(len(X_data)):
    numerator += (X_data[i] - mean_x) * (Y_data[i] - mean_y)
    denominator += (X_data[i] - mean_x) ** 2
β1 = numerator / denominator
β0 = mean_y - β1 * mean_x

# Make a Y for a new value of x
new_x = 6
Y = β1 * new_x + β0

# Print the results
print("β1 (coefficient):", β1)
print("β0:", β0)
print("Y for x=6:", Y)


# Plot the data
plt.scatter(X_data, Y_data)
# Plot the regression line
x1 = [min(X_data), max(X_data)]
y1 = [β0 + β1 * x_data for x_data in x1]

plt.xlabel("Lowest Point")
plt.ylabel("Max Elevation")
plt.title("Lowest Point vs Max Elevation")
plt.savefig("low_point_vs_max_elevation1.png")
plt.show()

