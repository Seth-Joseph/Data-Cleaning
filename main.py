import pandas as pd

df = pd.read_csv('main.csv')
print(list(df))

del df['planet_orbital_inclination']
del df['planet_density']

df.to_csv('data_cleaned.csv')