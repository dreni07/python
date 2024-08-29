import pandas as pd


products = ['Apple','Strawberries','Orange','Pear']
sales = [150,45,50,65]

sales_series = pd.Series(sales,index=products) # this just displays for
# every element in the products list
# the element of sales list of the same index
# for example
# index 0 of the products array
# with the index 0 of the sales array
print(sales_series)

#DATA FRAMES

datat = {
    'Names':['Dren','Dior','Ylli','Atik'],
    'Age':[17,18,19,23],
    'City':['Prishtine','Tirane','Gjakove','Prizren']
}

df_people = pd.DataFrame(datat)
print(df_people)


# manipulating data with files

df = pd.read_csv('avgIQpercountry.csv')
print(df.info())
print(df.head())


#select only the two columns that are needed
subset = df[['Country','Average IQ']]
print(subset)

## see countries and info for those who's iq is above 100

filtering = subset[subset['Average IQ'] > 100 and subset['Average IQ'] < 200]
print(filtering)

# handle an example where the data is missing or has duplicates

null_mask = df.isnull()
null_count = null_mask.sum()
if null_count:print(null_count) # nese ka null domethane printo numrin sa jan null

# removing the unwanted data

df.dropna(inplace=True) # if any column is empty or something went wrong remove that
print(df.info())

# count if there is any duplicate there
duplicated_data = df.duplicated()
if duplicated_data.sum():
    print(duplicated_data.sum())
else:
    print('No Duplicate Data')


df.drop_duplicates(keep='first',inplace=True) # with this we have an option
# to tell if we find an duplicate which one to keep
# aggregation functions-mi grumbullu te dhenat 