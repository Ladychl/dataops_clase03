# script etl.py
import pandas as pd

df = pd.read_csv('input.csv')
df['processed'] = df['value'] * 100
df['processed_inv'] = df['processed'] / 10
df.to_csv('output1.csv', index=False)
print("ETL completado en la tercera clase.")