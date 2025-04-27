import pandas as pd

df = pd.read_csv("data.csv")

x = round(df["Calories"].mode()[0], 2)

df["Date"] = pd.to_datetime(df["Date"])

print(df.to_string())
print(x)
