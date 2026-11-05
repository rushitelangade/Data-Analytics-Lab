import pandas as pd

# HELPER FUNCTION : Build a DataFrame from user input

def get_dataframe(df_name,columns):
    
    print(f"\n--Enter data for {df_name} (columns: {columns})--")
    num_rows = int(input(f"How many rows for {df_name}? "))
    
    data = {col:[] for col in columns}
    for r in range(num_rows):
        print(f"\nRow {r+1}:")
        for col in columns:
            value = input(f "{col}: ").strip()
            if value.isdigit():
                value = int(value)
                
            else:
                try:
                    value = float(value)
                except ValueError:
                    pass# keep as string
                data[col].append(value)
                
                df = pd.DataFrame(data)
                print(f"\n {df_name}:\n{df}\n")
                return df
            
            #1. CREATE DATASETS FROM USER INPUT
            
            PRINT("="*60)
            PRINT("step 1: Build Dataset 1- Student Basic info")
            print("="*60)
            student_df1=get_dataframe("Dataset 1(Students)",["StudentsID","Name","Branch"])
            
            print("="*60)
            print("step 2: Build Dataset 2- Student Marks")
            print("="*60)
            marks_df2=get_dataframe("Dataset 2(Marks)",["StudentsID","Subject","Marks"])
            
            print("="*60)
            print("step 3: Build Dataset 3- New batch of students ( same columns as Dataset 1)")
            print("="*60)
            students_df3=get_dataframe("Dataset 3(New Students)",["StudentsID","Name","Branch"])
            
            #2 CONCATENATION
            
            # VERTICAL CONCATENATION (STACKING-ROW)-COMBINING TWO BATCHES
            
            
            combined_students=pd.concat([student_df1,students_df3], axis=0, ignore_index=True)
            print("Vertical Concatenation (axis=0):\n",combined_students,"\n")
            
            
            #horizontal concatenation (Stacking columns side-by-side)
            
            print("--")