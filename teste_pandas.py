import pandas as pd
df = pd.read_csv('supermarket_sales.csv', sep=None, engine='python')
df['Total'] = df['Total'].str.replace(',','.').astype(float)
df_agrupado = df.groupby("City")["Total"].sum().round(2)
print(df_agrupado)