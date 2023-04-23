from sklearn.linear_model import LinearRegression
import pandas as pd

# Load the data into a Pandas dataframe
data = pd.read_csv('DataSet.csv')

# Define the independent variables and the dependent variable 
#add th total area land area and water area to the independent variables
X = 
y = data['Maximum.elevation'].values.astype(float)

# Create the model and fit it to the data
model = LinearRegression().fit(X, y)

# Print the coefficients for each independent variable
# plot the data
import matplotlib.pyplot as plt
plt.scatter(X[:,0], y, color='red')
plt.scatter(X[:,1], y, color='blue')
plt.scatter(X[:,2], y, color='green')
plt.title('Total Area vs Max Elevation', fontsize=14)
plt.xlabel('Total Area', fontsize=14)
plt.ylabel('Max Elevation', fontsize=14)
plt.grid(True)
plt.show()