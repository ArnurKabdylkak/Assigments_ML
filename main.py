import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
import json
import os
import matplotlib

# Set Matplotlib backend
matplotlib.use('TkAgg')

# Load and combine all JSON files into a single DataFrame
json_folder_path = 'D:/ShoppingAppReviews Dataset/ShoppingAppReviews/json'
json_files = os.listdir(json_folder_path)

combined_data = []
for json_file in json_files:
    file_path = os.path.join(json_folder_path, json_file)
    with open(file_path, 'r') as f:
        data = json.load(f)
        combined_data.extend(data)  # Assuming each JSON file contains a list of records

# Convert to a DataFrame
df = pd.DataFrame(combined_data, columns=['Platform'])

# Step 1: Add Dummy Data (Simulated for Assignment)
np.random.seed(42)
df['Reviews'] = np.random.randint(1000, 5000, size=len(df))
df['Ratings'] = np.random.uniform(1, 5, size=len(df)).round(1)
df['Category'] = np.random.choice(['Electronics', 'Fashion', 'Groceries'], size=len(df))

# Step 2: Exploratory Analysis and Visualization
# Visualizing Ratings Distribution
sns.histplot(df['Ratings'], bins=10, kde=True)
plt.title('Distribution of Ratings')
plt.xlabel('Ratings')
plt.ylabel('Frequency')
plt.savefig("ratings_distribution.png")  # Save instead of show

# Visualizing Reviews by Platform
sns.barplot(x='Platform', y='Reviews', data=df)
plt.title('Number of Reviews by Platform')
plt.xticks(rotation=45)
plt.savefig("reviews_by_platform.png")  # Save instead of show

# Visualizing Ratings by Category
sns.boxplot(x='Category', y='Ratings', data=df)
plt.title('Ratings by Category')
plt.savefig("ratings_by_category.png")  # Save instead of show

# Step 3: Handling Missing Values
# Checking for Missing Values
missing_values_count = df.isnull().sum()
print("Missing values count:")
print(missing_values_count)

# Step 4: Identify Numeric and Categorical Columns
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
categorical_cols = df.select_dtypes(include=['object']).columns.tolist()

# Step 5: Encode Categorical Data
# One-Hot Encoding
one_hot_encoder = OneHotEncoder()
one_hot_encoded = one_hot_encoder.fit_transform(df[categorical_cols]).toarray()

# Label Encoding
label_encoder = LabelEncoder()
for col in categorical_cols:
    df[col] = label_encoder.fit_transform(df[col])

# Step 6: Correlation Analysis
correlation_matrix = df[numeric_cols].corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.savefig("correlation_matrix.png")  # Save instead of show

# Save the processed data to a new CSV file
df.to_csv('processed_shopping_data.csv', index=False)

# Summary for Report
print("\nData processing and analysis complete. Check the generated visualizations and processed_shopping_data.csv file.")
