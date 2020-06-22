import numpy as nump
import pandas as pd
import matplotlib.pyplot as plt
 
# Reading df
df = pd.read_csv('usworld.csv')
print(df.shape)
#df.head()
 
 
# Collecting X and Y
X = df['United States'].values
Y = df['World'].values

# Mean X and Y
x_mean = nump.mean(X)
y_mean = nump.mean(Y)
 
# Total number of values
n = len(X)
 
# Using the formula to calculate m and c
numerator = 0
denominator = 0
for i in range(n):
    numerator += (X[i] - x_mean) * (Y[i] - y_mean)
    denominator += (X[i] - x_mean) ** 2
    m = numerator / denominator
    c = y_mean - (m * x_mean)
 
# Print coefficients

print ("m = ", m)
print("c = ", c)

# Plotting Values and Regression Line
max_x = nump.max(X) + 100
min_x = nump.min(X) - 100
# Calculating line values x and y
x = nump.linspace(min_x, max_x, 1000)
y = c + m * x 

 
# Ploting Line
plt.plot(x, y, color='red', label='Regression Line')
# Ploting Scatter Points
plt.scatter(X, Y, c='blue', label='Scatter Plot')
 
plt.title('Linear Regression betweeen US and the World Total')
plt.xlabel('United States')
plt.ylabel('World')
plt.legend()
plt.show()