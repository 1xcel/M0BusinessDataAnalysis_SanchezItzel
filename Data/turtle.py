import pandas as pd

# Read the CSV file
df = pd.read_csv('data/DATA.csv')
print(df)
print(df.columns)#This information looks insane.
#List the right columns we want to keep.
Coulmns_to_print=['Country', 'City','Tuition_USD', 'Rent_USD', 'Visa_Fee_USD',]
#Printing the columns selected
print(df[Coulmns_to_print])
# We need China and Russia,ONLY.
target_countries = ['China', 'Russia']
filtered_df = df[df['Country'].isin(target_countries)]
print(filtered_df[Coulmns_to_print]) #Have to add the filtered colums as well.
#Clumpy data. Finding the Total Cost for all cities.
filtered_df['Total_Cost'] = filtered_df['Tuition_USD'] + filtered_df['Rent_USD'] + filtered_df['Visa_Fee_USD']
city_total_cost = filtered_df.groupby(['Country','City'])['Total_Cost'].sum()
print(city_total_cost)#FILTERED_DF
#FINITOOO
























    




    













