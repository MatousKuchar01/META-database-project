# Load the 'Orders' sheet to examine its structure and content
orders_data = pd.read_excel(xls, 'Orders')

# Display the first few rows of the dataset to understand its structure
orders_data.head()



import matplotlib.pyplot as plt

# 1. Bar chart of total sales by cuisine type
sales_by_cuisine = orders_data.groupby('Cuisine Name')['Sales'].sum().sort_values(ascending=False)

# Create the bar chart
plt.figure(figsize=(10,6))
sales_by_cuisine.plot(kind='bar', color='c')
plt.title('Total Sales by Cuisine')
plt.ylabel('Total Sales')
plt.xlabel('Cuisine Name')
plt.xticks(rotation=45)
plt.tight_layout()

# Show the plot
plt.show()

