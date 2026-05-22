import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(
    "/Users/priya/Documents/Projects/Accident/accident.csv",
    sep=";",             # comma-separated
    engine="python",     # handle irregular lines
    on_bad_lines="skip"  # skip bad/malformed lines
)

# Clean up column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

#df = pd.read_csv('/Users/priya/Documents/Projects/Accident/accident.csv',sep=";")
#print(df.head())

#df.columns = df.columns.str.lower().str.replace(' ', '_')

#df.to_csv('cleaned_file.csv', index=False)

#print(df.columns)
print(df.info())
print("*************************************************************************")

total_injuries =df['total_injuries']
df['total_injuries'] = (df['number_of_pedestrians_injured'] + 
                        df['number_of_cyclist_injured'] + 
                        df['number_of_motorist_injured'])
print(total_injuries)
# Optional: create total deaths column as well
total_deaths = df['total_deaths']
df['total_deaths'] = (df['number_of_pedestrians_killed'] + 
                      df['number_of_cyclist_killed'] + 
                      df['number_of_motorist_killed'])

print(total_deaths)
print("*************************************************************************")

features = ['borough', 'zip_code', 'vehicle_type_code_1', 'vehicle_type_code_2', 
            'contributing_factor_vehicle_1', 'contributing_factor_vehicle_2']

X = df[features]
y = df['total_injuries']

#1
print(df['borough'].value_counts())

sns.set_style("dark")

df['borough'].value_counts().plot(kind='bar', figsize=(8,5))
plt.show()

print("*****************************@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
#2a
injured_cols = [
    'number_of_pedestrians_injured',
    'number_of_cyclist_injured',
    'number_of_motorist_injured'
]
for column in injured_cols:
    df[column]=df[column].astype(int)


injured_sums = df[injured_cols].sum()
print("Total injuries by category:")
print(injured_sums)

max_injured_category = injured_sums.idxmax()
max_injured_count=injured_sums[max_injured_category]
print("Category with most injuried persons is ", max_injured_category, "with count:", max_injured_count)

plt.figure(figsize=(8,5))
plt.bar(injured_sums.index, injured_sums.values, color=['pink', 'violet', 'lightblue'])
plt.title("Total injured by Category")
plt.xlabel("Category")
plt.ylabel("Number of injured persons")
plt.xticks(rotation=15)
plt.show()

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*******************************************")
#2b
killed_cols = [
    'number_of_pedestrians_killed',
    'number_of_cyclist_killed',
    'number_of_motorist_killed'
]

for column in killed_cols:
    df[column]=df[column].astype(int)


max_dead = df[killed_cols].sum()
print("Total Deaths by category:")
print(max_dead)
max_dead_category = max_dead.idxmax()

max_dead_count = max_dead[max_dead_category]
print("Category with most dead persons is", max_dead_category,"with count:",max_dead_count)

killed_df = max_dead.reset_index()
killed_df.columns = ['Category', 'Deaths']


plt.figure(figsize=(8,5))
sns.barplot(x='Category', y='Deaths', data=killed_df, palette='Reds_r')
plt.title("Total Deaths by Category")
plt.xlabel("Category")
plt.ylabel("Number of Deaths")
plt.xticks(rotation=15)
plt.show()
print("*****************@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@************************")


#3
vehicle_cols = ['vehicle_type_code_1', 'vehicle_type_code_2','vehicle_type_code_3', 'vehicle_type_code_4', 'vehicle_type_code_5']
all_vehicles = df[vehicle_cols].stack()
vehicle_counts = all_vehicles.value_counts().head(10)
print(vehicle_counts)

plt.figure(figsize=(12,6))
sns.barplot(x=vehicle_counts.index, y=vehicle_counts.values, palette='viridis')
plt.title("Number of Accidents by Vehicle Type")
plt.xlabel("Vehicle Type")
plt.ylabel("Number of Accidents")
plt.xticks(rotation=90)
plt.show()

