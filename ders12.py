import pandas as pd 

df = pd.read_csv("test.txt", header=None)

df.to_excel("test.xlsx", index=False)
