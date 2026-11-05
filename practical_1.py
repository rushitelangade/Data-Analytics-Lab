import pandas as pd 

df = pd.DataFrame({
    "name": ["Amit", "Priya", "Rahul", "sneha"],
    "dept": ["CSE", "IT", "CSE", "IT"],
    "marks": [85, 92, 78, 88]
})

print(df)
   
print("Original Data : \n",df)

#Data Subsetting

print("\nSubset (Marks>50):\n",df[df["marks"]>50])

#Sorting in Ascending Orders

print("\nSorted by marks (Ascending):\n",df.sort_values("marks"))

#Grouping

print("\nGrouped (Average Marks bt Department):\n",df.groupby("dept")["marks"].mean())

#Statistical Operations

print("\nMean =",df["marks"].mean())
print("Median =",df["marks"].median())
print("Mode =")
print(df["marks"].mode())