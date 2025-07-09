# script etl.py
import pandas as pd

df = pd.read_csv('input.csv')
df['processed'] = df['value'] * 100000
df['processed_inv'] = df['processed'] / 1000
df.to_csv('output1.csv', index=False)
print("ETL completado.")