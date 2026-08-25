import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("olympics_medals_country_wise.csv")
df.columns = df.columns.str.strip()
columns_to_clean = [
    "summer_gold",
    "summer_total",
    "total_gold",
    "total_total"
]

for column in columns_to_clean:
    df[column] = df[column].str.replace(",", "")
    df[column] = pd.to_numeric(df[column])
df[df["total_gold"] == df["total_gold"].max()]
top_10 = df.sort_values("total_gold", ascending=False).head(10)
top_10 = df.sort_values("total_total", ascending=False).head(10)

plt.bar(top_10["countries"], top_10["total_total"])

plt.title("Top 10 Countries by Total Olympic Medals")
plt.xlabel("Country")
plt.ylabel("Total Medals")

plt.xticks(rotation=45)

plt.savefig("top_10_gold.png")