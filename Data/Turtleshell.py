import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

df =pd.read_csv('totalcost.csv')
print(df)
#china graph 
df_china = df[df['Country'] == 'China']
df_china = df_china.sort_values(by='Total_Cost', ascending=True)
x_vaules = df_china['City']
y_values = df_china['Total_Cost']
#Now we are going to plot the graph.
plt.plot(x_vaules, y_values)
plt.title('Total Cost of Living in China')
plt.xlabel('City')
plt.ylabel('Total Cost')
plt.grid(True)
plt.show()


 
#Graph for Russia 

df_russia = df[df['Country'] == 'Russia']
df_russia = df_russia.sort_values(by= 'Total_Cost', ascending=True)
x_vaules = df_russia['City']
y_values = df_russia['Total_Cost']

# WE are graphing russia 

plt.plot (x_vaules, y_values)
plt.title ('Total Cost of Living in Russia')
plt.xlabel ('City')
plt.ylabel ('Total Cost')
plt.grid (True)
plt.show()







