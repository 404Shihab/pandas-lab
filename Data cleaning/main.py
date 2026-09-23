import pandas as pd

# Data cleaning = the process of fixing/removing:
#                 incomplete, incorrect, or irrelevant data.
#                 ~75% of work done with Pandas is data cleaning

df = pd.read_csv("Data cleaning/data.csv")

# print(df)

# ------remove irrelevant columns-------

# df = df.drop(columns=["CGPA", "Phone"])

# print(df.to_string())

# -------Handle missing data--------
# df = df.dropna(subset=["CGPA"])         # dropna - drop not available

# df = df.fillna({"CGPA": "NONE"})  #fillna = fill not available


#---- fix inconsistent values -------

# df["City"] = df["City"].replace({"Dhaka":"DHAKA",
#                                 "Chittagong":"ctg"}
#                                 )


# --- Standardize text -----

# df["Name"] = df["Name"].str.lower()


# -------- fix data types -----

# df["Is_Active"] = df["Is_Active"].astype(bool)


#------------- Remove duplicate values --------

df =df.drop_duplicates()


print(df.to_string())
