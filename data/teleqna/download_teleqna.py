from datasets import load_dataset
import pandas as pd

dataset = load_dataset("netop/TeleQnA")

df = pd.DataFrame(dataset["test"])

df.to_csv("teleqna.csv", index=False)

print("Saved teleqna.csv")
print(df.head())