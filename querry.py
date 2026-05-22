import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_csv('/Users/priya/Documents/Projects/Accident/accident.csv',sep=";")

1.
print(df.columns)

2.
df_selected = df[['DATE','BOROUGH','NUMBER OF PEDESTRIANS INJURED']]
print(df_selected)

3.
queens_df = df[df['BOROUGH'] == 'QUEENS']
print(queens_df)

4.
pedestrian_df = df.loc[df['NUMBER OF PEDESTRIANS INJURED'] >= 1,'BOROUGH']
print(pedestrian_df)

5.
street_df = df[df['ON STREET NAME'].notnull()]
print(street_df)

6.
date_df = df[['DATE','TIME']].sort_values('DATE', ascending=False)
print(date_df)

7.
cyclist_df = df[['NUMBER OF CYCLIST INJURED']].sort_values('NUMBER OF CYCLIST INJURED', ascending=False).head(10)
print(cyclist_df)

print('***************************')
8.
total = len(df)
print(total)
print('***************************')

tota = df.shape[0]
print(tota)
print('***************************')

print(df[['ON STREET NAME']].count())

print('***************************')
print(df['NUMBER OF PEDESTRIANS INJURED'].unique())

print(df['BOROUGH'].unique())
print('***************************')

print(df[['BOROUGH']].nunique())

print('***************************')
print(df[['BOROUGH']].value_counts())

print('***************************')
print(df[['CONTRIBUTING FACTOR VEHICLE 1',
       'CONTRIBUTING FACTOR VEHICLE 2']].drop_duplicates())

9.
ped_inj = df.loc[df['NUMBER OF PEDESTRIANS INJURED']>=1 ,'BOROUGH']
print(ped_inj)

print('***************************')

print(len(ped_inj))

print('***************************')
print(ped_inj.shape[0])

print('***************************')
10.
print(df[['NUMBER OF MOTORIST INJURED']].mean())

