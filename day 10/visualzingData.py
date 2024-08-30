import matplotlib.pyplot as plt
import pandas as pd
import numPY
# df = pd.read_csv('../numPY/avgIQpercountry.csv')
# # just_grouping = df[['Country','Average IQ']]
# # print(just_grouping)
# # sub_seting = just_grouping[just_grouping['Average IQ'] > 100]
# meKusht = df[df['Average IQ'] >= 100].sort_values(by='Average IQ',ascending=False)
#
# print(meKusht)
# plt.figure(figsize=(14,8))
# bars = plt.bar(meKusht['Country'],meKusht['Average IQ'],color='skyblue') # first argument will be in the X axis and the second one in the Y axis
# plt.xlabel('Country')
# plt.ylabel('Average IQ')
# plt.xticks(rotation=90,fontsize=14)
# plt.yticks(rotation=90,fontsize=14)
# plt.grid(axis='y',linestyle='--',alpha=0.5)
# plt.bar_label(bars,color='black')
# plt.tight_layout()


## visualizing again
# data_frames = pd.read_csv('../numPY/avgIQpercountry.csv')
# by_country_iq = data_frames.groupby('Continent')['Average IQ'].mean()
#
# plt.figure(figsize=(10,6))
# by_country_iq.plot(kind='line')
# plt.title('Average IQ per country')
# plt.xlabel('Country')
# plt.ylabel('IQ')
# plt.yticks(rotation=90)
#
# plt.grid(axis='both',linestyle='--',alpha=0.5)
# plt.show()
# SCATTER PLOT
# df = pd.read_csv('../numPY/avgIQpercountry.csv')
# plt.figure(figsize=(10,6))
#
# plt.scatter(df['Mean years of schooling - 2021'],df['Average IQ'])
#
# plt.show()

#PY CHARTING
# df = pd.read_csv('../numPY/avgIQpercountry.csv')
#
# nobel_prizes_by_continent = df.groupby('Continent')['Nobel Prices'].sum()
# num_of_continents = nobel_prizes_by_continent.count()
# print(num_of_continents)
#
# colors = ['gold','lightcoral','yellow','green','orange']
#
#
# plt.figure(figsize=(10,10))
#
# nobel_prizes_by_continent.plot(kind='pie',autopct='%1.1f%%',color=colors)
# plt.show()

# SEABORN
# import seaborn as sns
#
#
# df = pd.read_csv('../numPY/avgIQpercountry.csv')
# plt.figure(figsize=(10,6))
# sns.histplot(df['Average IQ'])
# plt.xlabel('Average IQ')
# plt.ylabel('Average IQ')
# plt.tight_layout()
# plt.show()

#HEAT MAP
# import seaborn as sns
# df = pd.read_csv('../numPY/avgIQpercountry.csv')
# df['Population - 2023'] = df['Population - 2023'].str.replace(',','').astype(float)
# numerical_iq_data = df.select_dtypes(include='number')
# sns.heatmap(numerical_iq_data.corr(),annot=True,cmap='coolwarm',fmt='.2f')
# plt.show()

#plotpy visualization
import seaborn as sns
import plotly.express as px

df = pd.read_csv('../numPY/avgIQpercountry.csv')

df['Population - 2023'] = df['Population - 2023'].str.replace(',','').astype(float)

fig=px.scatter_geo(df,locations='Country',locationmode='country names',hover_name='Country',size='Average IQ',color='Continent',projection='natural earth',title='Average IQ per country',size_max=20,template='plotly_dark')
fig.show()