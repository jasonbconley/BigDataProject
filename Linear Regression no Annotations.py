# Import the packages and classes needed in this example:
import numpy as np
from sklearn.linear_model import LinearRegression
from scipy import stats
import matplotlib.pyplot as plt
import queryTree

x1,y1,z1 = queryTree.queryTheTree()

# Create a numpy array of data:
x = np.array(x1).reshape((-1, 1))
y = np.array(y1)
z = an= z1
pX = np.array(x1) # just to be used for the Pearson's coefficient calculation

# Create an instance of a linear regression model and fit it to the data with the fit() function:
model = LinearRegression().fit(x,y) 

# The following section will get results by interpreting the created instance: 

# Print the Intercept:
print('Intercept:', model.intercept_)

# Print the Slope:
print('Slope:', model.coef_) 
model = LinearRegression()
model.fit(x,y)

# Print the Pearson's coefficient
pcoeff = stats.pearsonr(pX, y)
print('Pearsons r:', pcoeff)

# Obtain the coefficient of determination by calling the model with the score() function, then print the coefficient:
r_sq = model.score(x, y)
print('R^2/Coefficient of Determination:', r_sq)

# Plot the estimated linear regression line with matplotlib:
x_test = np.linspace(35000,100000, endpoint=True)
y_pred = model.predict(x_test[:,None])

#plots the x and y then adds the annotations for y 'states'
plt.scatter(x, y, color = 'black')
plt.title("COVID-19 Case Counts vs. Average Income by Counties (unlabeled)", fontsize=15)

#plots the prediciton and labels
plt.xlabel("Average Income")
plt.ylabel("Case Count")

plt.plot(x_test,y_pred, color = 'red');
plt.legend(['Counties','Line of Regression'])
plt.show()
