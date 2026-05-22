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


8.
total = len(df)
print(total)

print('--------------------------------------------------------------')

tota = df.shape[0]
print(tota)

print('--------------------------------------------------------------')

print(df[['ON STREET NAME']].count())

print('--------------------------------------------------------------')

print(df['NUMBER OF PEDESTRIANS INJURED'].unique())

print(df['BOROUGH'].unique())

print('--------------------------------------------------------------')

print(df[['BOROUGH']].nunique())

print('--------------------------------------------------------------')

print(df[['BOROUGH']].value_counts())

print('--------------------------------------------------------------')

print(df[['CONTRIBUTING FACTOR VEHICLE 1',
       'CONTRIBUTING FACTOR VEHICLE 2']].drop_duplicates())


9.
ped_inj = df.loc[df['NUMBER OF PEDESTRIANS INJURED']>=1 ,'BOROUGH'] #.shape[0]
print(ped_inj)

print('--------------------------------------------------------------')

print(len(ped_inj))

print('--------------------------------------------------------------')

print(ped_inj.shape[0])

print('--------------------------------------------------------------')

10.
print(df[['NUMBER OF MOTORIST INJURED']].mean())

print('--------------------------------------------------------------')

11.
print(df.groupby('BOROUGH').count())


12.
print(df.groupby('BOROUGH')['COLLISION_ID'].count())

print('--------------------------------------------------------------')

14.
vehicle_cols = ['CONTRIBUTING FACTOR VEHICLE 1',
       'CONTRIBUTING FACTOR VEHICLE 2', 'CONTRIBUTING FACTOR VEHICLE 3',
       'CONTRIBUTING FACTOR VEHICLE 4', 'CONTRIBUTING FACTOR VEHICLE 5']

df[vehicle_cols] = df[vehicle_cols].apply(lambda x: x.str.strip().str.upper())

print(df.loc[df[vehicle_cols].isin(['Sedan']).any(axis=1),'BOROUGH'])


#print(df[vehicle_cols].apply(lambda x: x.str.upper().str.strip().isin(['Bus'])).any(axis=1).sum())

print('--------------------------------------------------------------')


15.
print(df.loc[df['NUMBER OF PEDESTRIANS INJURED']>=1,['ON STREET NAME','NUMBER OF PEDESTRIANS INJURED']])

print('--------------------------------------------------------------')

16.
avg = df.groupby('BOROUGH').size()
avg_acc = avg.mean()

acc = avg[avg >= avg_acc]
print(acc)

print('--------------------------------------------------------------')

17.
factor_cols = ['CONTRIBUTING FACTOR VEHICLE 1',
               'CONTRIBUTING FACTOR VEHICLE 2',
               'CONTRIBUTING FACTOR VEHICLE 3',
               'CONTRIBUTING FACTOR VEHICLE 4',
               'CONTRIBUTING FACTOR VEHICLE 5']


all_factors = pd.concat([df[col] for col in factor_cols])


most_common = all_factors.value_counts().idxmax()
count = all_factors.value_counts().max()

print(f"Most common contributing factor: {most_common} ({count} times)")

print('--------------------------------------------------------------')

factors = df[factor_cols].stack()
print(factors.value_counts())

print('--------------------------------------------------------------') 

18.
injuries = ['NUMBER OF PEDESTRIANS INJURED','NUMBER OF CYCLIST INJURED','NUMBER OF MOTORIST INJURED']

total_injuries_by_date = (
    df.groupby('DATE')[injuries]
      .sum()
      .sum(axis=1)
)
print(total_injuries_by_date)


21.
df['DATE'] = pd.to_datetime(df['DATE'])

df['YEAR'] = df['DATE'].dt.year
pedestrians = (df.groupby('YEAR')['NUMBER OF PEDESTRIANS INJURED'].sum())
print(pedestrians)



22.
df['TIME'] = pd.to_datetime(df['TIME'])
df['HOUR'] = df['TIME'].dt.hour

accidents_per_hour = df.groupby('HOUR').size()
print(accidents_per_hour)


