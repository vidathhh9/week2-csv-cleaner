import pandas as pd

df = pd.read_csv("urls.csv")
print("Rows before:", len(df))

df = df.drop_duplicates()
df = df.dropna(subset=["url"])
df["label"] = df["label"].fillna("unknown")
df["url"] = df["url"].str.strip().str.lower()

print("Rows after:", len(df))

df["url_length"] = df["url"].str.len()
df["uses_https"] = df["url"].str.startswith("https")
df["dot_count"] = df["url"].str.count(r"\.")

print(df)
print(df["label"].value_counts())
print(df.groupby("label")["url_length"].mean())

df.to_csv("urls_clean.csv", index=False)
print("Saved urls_clean.csv")