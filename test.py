from scipy import stats
import numpy as np
# Generate some data with outliers
x = [-5, 6, 3, 4, 56]
y = [10, 20, 30, 40, 50]

# Convert the lists to numpy arrays
x = np.array(x)
y = np.array(y)

# Calculate the Z-score of each data point for y only
y_z_scores = stats.zscore(y)

# Remove data points with Z-score greater than 3 (or any other threshold) for y only
threshold = 1
y_filtered = y[abs(y_z_scores) < threshold]

# Filter x data based on which y values were removed
x_filtered = x[abs(y_z_scores) < threshold]

print("Original x data:", x)
print("Original y data:", y)
print("Filtered x data:", x_filtered)
print("Filtered y data:", y_filtered)

# Plot the data
import matplotlib.pyplot as plt
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
ax1.plot(x)
ax1.plot(x_filtered)
ax1.set_title('X data')
ax2.plot(y)
ax2.plot(y_filtered)
ax2.set_title('Y data')
plt.show()
