import pandas as pd

# Lê o CSV compactado
df = pd.read_csv("caso_full.csv.gz", compression="gzip", low_memory=False)

# Mostra as 5 primeiras linhas
print(df.head())
