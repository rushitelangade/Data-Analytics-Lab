# ============================================================
# Practical 01: Data Operations using Pandas
# Subject: Data Analytics
# Topic: DataFrame, Subsetting, Sorting, Grouping and
#        Statistical Operations
# ============================================================

# Import the pandas library
import pandas as pd


# ------------------------------------------------------------
# Create a DataFrame
# ------------------------------------------------------------
df = pd.DataFrame({
    "Name": ["Arjun", "Kavya", "Sahil", "Meera"],
    "Dept": ["HR", "Sales", "Finance", "IT"],
    "Age": [24, 29, 26, 31],
    "Weight": [68, 55, 72, 60],
    "Salary": [35000, 42000, 38000, 50000]
})


# Display the original DataFrame
print("Original Data:\n", df)


# ------------------------------------------------------------
# Data Subsetting
# Select employees whose salary is greater than 40000
# ------------------------------------------------------------
print("\nSubset (Salary > 40000):\n",
      df[df["Salary"] > 40000])


# ------------------------------------------------------------
# Sorting in Ascending Order
# Sort the data based on Salary from lowest to highest
# ------------------------------------------------------------
print("\nSorted by Salary (Ascending):\n",
      df.sort_values("Salary"))


# ------------------------------------------------------------
# Sorting in Descending Order
# Sort the data based on Salary from highest to lowest
# ------------------------------------------------------------
print("\nSorted by Salary (Descending):\n",
      df.sort_values("Salary", ascending=False))


# ------------------------------------------------------------
# Grouping
# Calculate the average salary for each department
# ------------------------------------------------------------
print("\nGrouped (Average Salary by Department):\n",
      df.groupby("Dept")["Salary"].mean())


# ------------------------------------------------------------
# Statistical Operations
# Calculate Mean, Median and Mode of Salary
# ------------------------------------------------------------

print("\nMean Salary =", df["Salary"].mean())

print("Median Salary =", df["Salary"].median())

print("Mode Salary =")
print(df["Salary"].mode())
