import pandas as pd
import matplotlib.pyplot as plt
print("changes from Github remotely")
# Load the dataset
data = pd.read_csv("Mall_customers.csv")

# Plot a scatter plot for 'Annual Income (k$)' vs 'Spending Score (1-100)'
data.plot(x='Annual Income (k$)', y='Spending Score (1-100)', kind='scatter', title='Annual Income vs Spending Score')
plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score (1-100)")
plt.show()
