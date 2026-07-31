import pandas as pd 

df = pd.read_csv("baza.txt", header=None)

df.to_excel("baza.xlsx", index=False)
