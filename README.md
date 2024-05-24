Medical Records Analysis - Python Script
This Python script analyzes a dataset of medical records (stored in "medical_records.csv"). It provides insights into the data, including:

General overview: Displays the first few rows and column names to familiarize you with the data structure.
Summary statistics: Generates summary statistics for all data types (numerical and categorical) to understand the central tendencies and spread of the data.
Stroke data analysis: Filters and summarizes data for patients diagnosed with Stroke.
Disease-wise statistics: Groups data by disease category and calculates various descriptive statistics for each category.
Data visualizations: Creates box plots and violin plots to visualize the distribution of age across different disease categories.
Requirements:

Python 3.x
pandas library
matplotlib.pyplot library
seaborn library
Instructions:

Ensure you have the required libraries installed (pandas, matplotlib.pyplot, seaborn). You can install them using pip install pandas matplotlib seaborn.
Place this script (along with the "medical_records.csv" file) in the same directory.
Run the script from your terminal using python your_script_name.py.
Output:

The script will print the following:

First few rows of the data.
List of column names.
Summary statistics of the entire dataset.
Summary statistics of the Stroke data.
Summary statistics grouped by disease category.
Two visualizations depicting the distribution of age by disease category (box plot and violin plot).
