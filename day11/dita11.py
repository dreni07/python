import pandas as pd
import matplotlib.pyplot as plt
the_df = pd.read_csv('weather_tokyo_data.csv')

average = the_df['temperature'].mean()
rounding = round(average,2)
only_day = the_df['day']

grouping = the_df.groupby('day')['temperature'].sum()
sorting_them = grouping.sort_values(ascending=False)


changes_over_time = the_df.groupby('year')['temperature'].sum()
print(changes_over_time)


sorting_them_2 = changes_over_time.sort_values(ascending=False)

plt.figure(figsize=(10,6))
bars = plt.bar(changes_over_time.index,changes_over_time.values,color='black')
plt.xlabel('Year')
plt.ylabel('Temperature')
plt.bar_label(bars,color='skyblue')
plt.tight_layout()
plt.show()













