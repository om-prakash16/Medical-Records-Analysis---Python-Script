import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the medical data from the CSV file
data = pd.read_csv("medical_records.csv")

# Get a quick glimpse at the first few rows of the data
print("First few rows:")
print(data.head())

# Show the column names (features) present in the data
print("\nColumn names:")
print(data.columns)

# Get some summary statistics of the data, including numerical and categorical data
print("\nSummary statistics:")
print(data.describe(include='all'))

# Filter data for patients with Stroke diagnosis
stroke_data = data[data['Disease_Category'] == 'Stroke']

# Print a summary of the Stroke data
print("\nStroke data summary:")
print(stroke_data.describe(include='all'))

# Group data by disease category and calculate statistics
disease_stats = data.groupby('Disease_Category').describe(include='all')
print("Statistics by Disease Category:")
print(disease_stats)


sns.boxplot(
    x = "Disease_Category",
    y = "Age",
    data=data
)
plt.title('Distribution of Age by Disease Category')
plt.xlabel('Disease Category')
plt.ylabel('Age')
plt.xticks(rotation=45)
plt.show()


sns.violinplot(
    x = "Disease_Category",
    y = "Age",

    data=data
)
plt.title('Distribution of Age by Disease Category (Violin Plot)')
plt.xlabel('Disease Category')
plt.ylabel('Age')
plt.xticks(rotation=45)
plt.show()

