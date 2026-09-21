import pandas as pd

# DataFrame = A tabular data structure with rows AND columns. (2 Dimensional)
#             Similar to an Excel spreadsheet


data = {"Name" : ["java kahn", "python bhuiyan", "cpp khan"],
        "Age": [23, 34, 12]
        }

df = pd.DataFrame(data) # DataFrame() - constructor

print(df)              # Name  Age
         # 0       java kahn   23
         # 1  python bhuiyan   34
         # 2        cpp khan   12

df=pd.DataFrame(data, index=["Employee 1","Employee 2","Employee 3"])  # custom indexing
print(df)                      #  Name  Age
          # Employee 1       java kahn   23
          # Employee 2  python bhuiyan   34
          # Employee 3        cpp khan   12
        

print(df.loc["Employee 2"]) # Name    python bhuiyan
                            # Age                 34
                            # Name: Employee 2, dtype: object
        

print(df.iloc[2]) # Name    cpp khan
                  # Age           12
                  # Name: Employee 3, dtype: object


# ----- Add a new column -----

df["Job"] = ["Cook","N/A","Cashier"]

print(df)                     #    Name  Age      Job
           # Employee 1       java kahn   23     Cook
           # Employee 2  python bhuiyan   34      N/A
           # Employee 3        cpp khan   12  Cashier


# ----- Add a new row -----

new_row = pd.DataFrame([{"Name": "Someone", "Age": 45, "Job": "Nothing"}],
                       index=["Employee 4"])

df = pd.concat([df, new_row])

print(df)                 #      Name  Age      Job
         # Employee 1       java kahn   23     Cook
         # Employee 2  python bhuiyan   34      N/A
         # Employee 3        cpp khan   12  Cashier
         # Employee 4         Someone   45  Nothing

# ----- Add new rows -----

new_rows = pd.DataFrame([{"Name": "No one", "Age": 15, "Job": "something"},
                         {"Name": "unknown", "Age": 22, "Job": "anything"}],
                       index=["Employee 5", "Employee 6"])

df = pd.concat([df, new_rows])

print(df)                 #          Name  Age        Job
            #  Employee 1       java kahn   23       Cook
            #  Employee 2  python bhuiyan   34        N/A
            #  Employee 3        cpp khan   12    Cashier
            #  Employee 4         Someone   45    Nothing
            #  Employee 5          No one   15  something
            #  Employee 6         unknown   22   anything