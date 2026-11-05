import pandas as pd

# Function to calculate average 

def calculate_average(marks):
    return sum(marks) / len(marks)

#User Input
n = int(input("Enter the number of students: "))

names = []
marks = []

for i in range(n):
    name = input("Enter student name: ")
    mark =float(input("Enter student marks: "))
    
    names.append(name)
    marks.append(mark)
    
    #create dataset
    
    df = pd.DataFrame({
        "name": names,
        "marks": marks
    })
    
    # Conditional Statement using function
    
    def result(marks):
        if marks >= 75:
            return "Distinction"
        elif marks >= 50:
            return "Pass"
        else:
            return "Fail"
        
        df["Result"]= df["marks"].apply(result)
        
        #Display dataset 
        print("\nDataset:")
        print(df)
        
        #Loop for processinf values
        
        print("\nStudent Analysis:")
        for mark in marks:
            if mark >= 75:
                print(mark, "Distinction")
            elif mark >= 50:
                print(mark, "Pass")
            else:
                print(mark, "Fail")
            
            
    # Analysis 
    print("\nAverage Marks:", calculate_average(marks))
    print("Highest Marks:", max(marks))
    print("Lowest Marks:", min(marks))