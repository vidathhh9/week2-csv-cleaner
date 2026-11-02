import pandas as pd

df = pd.read_csv("urls.csv")
print(df.head())
print(df.info())
print(df.describe(include="all"))
print(df["label"].value_counts(dropna=False))