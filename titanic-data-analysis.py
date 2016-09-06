import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re

training_df = pd.read_csv("train.csv")

"""
The main types stored in pandas objects are 
float, int, bool, datetime64[ns], datetime64[ns, tz] (in >= 0.17.0), timedelta[ns], category (in >= 0.15.0), and object
"""

# exctract some data from the "Name" column and add to the data frame
training_df["First_Name"] = training_df["Name"].apply(lambda _: _.split()[2])
training_df["Surname"] = training_df["Name"].apply(lambda _: _.split(",")[0])
training_df["Title"] = training_df["Name"].apply(lambda _: re.findall(",\s+(\w+)\.",_)[0] if len(re.findall(",\s+(\w+)\.",_)) > 0 else None)

print(training_df.head())