import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="whitegrid")
import re
import pylab

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

# have a look at the age of passengers by sex
g = sns.FacetGrid(training_df, col="Sex")
g.map(plt.hist, "Age");

# see the fares they paid depending on sex and where they got on the ship
g = sns.FacetGrid(training_df, col="Sex", hue="Embarked")
g.map(plt.scatter, "Fare", "Age", alpha=.7)
g.add_legend();

g = sns.FacetGrid(training_df, col="Sex", hue="Survived")
g.map(plt.scatter, "Fare", "Pclass", alpha=.7)
g.add_legend();


pylab.show()