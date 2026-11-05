import pandas as pd

#Take number of students

n = int(input("Enter the number of students: "))

names = []
ages = []
departments = []
dates = []

#Take input from user

for i in range(n):
    print("\n Enter details of students", i+1)
    
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    department = input("Enter Department: ")
    date = input("Enter Admission date (DD-MM-YYYY): ")
    
    names.append(name)
    ages.append(age)
    departments.append(department)
    dates.append(date)
    
    #Create DataFrame
    
    data = {
        'Name': names,
        'Age': ages,
        'Department': departments,
        'Admission_Date': dates
    }
    
    df = pd.DataFrame(data)
    
    print("\n Original data :")
    print(df)
    
    print("\nOriginal Data Types :")
    print(df.dtypes)
    
    # 1. DATA TYPE CONVERSION
    
    # Convert Age from string to integer
    
    df["Age"] = df["Age"].astype(int)
    
    # STRING MANIPULATION
    
    # Removes extra space from names
    
    df["Name"] = df["Name"].str.strip()
    
    # Convert Name into Tittle Case
    
    df["Name"] = df["Name"].str.title()
    
    # Converts Department into Title Case
    
    df['Department']=df['Department'].str.title()
    
    # 3 DATA TYPE TRANSFORMATION
    
    # Converts Admission_Date into DateTime 
    
    df["Admission_Date"] = pd.to_datetime(df["Admission_Date"], format="%d-%m-%Y")
    
    # Extra Year
    
    df['Year'] = df['Admission_Date'].dt.year
    
    # Extra month
    
    df['Month'] = df['Admission_Date'].dt.month
    
    # Extra Day
    
    df['Day'] = df['Admission_Date'].dt.day
    
    # DISPLAY TRANSFORMED DATA
    
    print("\nTransformed Data :")
    print(df)
    
    print("\nTransformed Data types :")
    print(df.dtypes)
