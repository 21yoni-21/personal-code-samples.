# Simple Linear Regression Example using scikit-learn
# This script predicts house prices based on size

from sklearn.linear_model import LinearRegression
import numpy as np

# Training data: sizes (in square feet) and prices (in $1000s)
sizes = np.array([[650], [800], [1200], [1500], [1800]])
prices = np.array([200, 250, 350, 400, 450])

# Create the model and fit the data
model = LinearRegression()
model.fit(sizes, prices)

# Predict price for a new house size
new_house_size = np.array([[1000]])
predicted_price = model.predict(new_house_size)

print(f"Predicted price for 1000 sq ft: ${predicted_price[0]*1000:.2f}")
