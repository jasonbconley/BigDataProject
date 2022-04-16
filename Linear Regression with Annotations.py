# Import the packages and classes needed in this example:
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import queryTree

x1,y1,z1 = queryTree.queryTheTree()

# Create a numpy array of data:
x = np.array(x1).reshape((-1, 1))
y = np.array(y1)
z = an= z1

# Create an instance of a linear regression model and fit it to the data with the fit() function:
model = LinearRegression().fit(x,y) 

# The following section will get results by interpreting the created instance: 

# Obtain the coefficient of determination by calling the model with the score() function, then print the coefficient:
r_sq = model.score(x, y)
print('coefficient of determination:', r_sq)

# Print the Intercept:
print('intercept:', model.intercept_)

# Print the Slope:
print('slope:', model.coef_) 
model = LinearRegression()
model.fit(x,y)

# Plot the estimated linear regression line with matplotlib:
x_test = np.linspace(35000,100000, endpoint=True)
y_pred = model.predict(x_test[:,None])

#plots the x and y then adds the annotations for y 'states'
plt.scatter(x, y, color = 'darkgreen')
plt.title("Covid Infection Rates",fontsize=15)
for i, label in enumerate(z):
    plt.annotate(label, (x[i], y[i]))

#plots the prediciton and labels
plt.xlabel("Average Income")
plt.ylabel("Case Count")

plt.plot(x_test,y_pred, color = 'red');
plt.legend(['Counties','Line of Regression'])
plt.show()

