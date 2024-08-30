import pandas as pd
#
#
# products = ['Apple','Strawberries','Orange','Pear']
# sales = [150,45,50,65]
#
# sales_series = pd.Series(sales,index=products) # this just displays for
# # every element in the products list
# # the element of sales list of the same index
# # for example
# # index 0 of the products array
# # with the index 0 of the sales array
# print(sales_series)
#
# #DATA FRAMES
#
# datat = {
#     'Names':['Dren','Dior','Ylli','Atik'],
#     'Age':[17,18,19,23],
#     'City':['Prishtine','Tirane','Gjakove','Prizren']
# }
#
# df_people = pd.DataFrame(datat)
# print(df_people)
#
#
# # manipulating data with files
#
df = pd.read_csv('avgIQpercountry.csv')
# print(df.info())
# print(df.head())
#
#
# #select only the two columns that are needed
# subset = df[['Country','Average IQ']]
#
# print(subset)
#
# ## see countries and info for those who's iq is above 100
#
# filtering = subset[subset['Average IQ'] > 100]
# print(filtering)
#
# # handle an example where the data is missing or has duplicates
#
# null_mask = df.isnull()
# null_count = null_mask.sum()
#  # nese ka null domethane printo numrin sa jan null
#
# # removing the unwanted data
#
# df.dropna(inplace=True) # if any column is empty or something went wrong remove that
# print(df.info())
#
# duplicated_data = df.duplicated()# count if there is any duplicate there
#
# if duplicated_data.sum():
#     print(duplicated_data.sum())
# else:
#     print('No Duplicate Data')
#
#
# df.drop_duplicates(keep='first',inplace=True) # with this we have an option
# # to tell if we find an duplicate which one to keep
# # aggregation functions-mi grumbullu te dhenat
# print(subset)
# subset2 = df[['Rank','Country']]
# subset3 = df[['Average IQ','Continent']]
# print(subset2)
# print(subset3)
# print(df_people)

# find average IQ for each continent
averag_iq_continent = df.groupby('Continent')['Average IQ'].mean()
print(averag_iq_continent)

averag_iq_continent_sorted = averag_iq_continent.sort_values(ascending=False)
print(averag_iq_continent_sorted)
by_nobel = df.groupby('Country')['Nobel Prices'].sum()
sorting_them = by_nobel.sort_values(ascending=False)
print(sorting_them)

for_reading = df.groupby('Continent')['Literacy Rate'].mean()
sorting_them_by = for_reading.sort_values(ascending=False)
print(sorting_them_by)
