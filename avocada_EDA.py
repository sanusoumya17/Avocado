import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

#Read the dataset and make the first column as the default index column
data_csv = pd.read_csv('avocado.csv',index_col=0)

#Checking for any missing values
data_csv.isnull().sum()

data_csv.info()

#DATA SHAPE:
row, columns = data_csv.shape
print("Data Row:", row)
print("Data Columns:", columns)

# Count of each type in the data set to find which is more in demand
count_of_type=pd.crosstab(index=data_csv['type'],columns='count',dropna=True)
print(count_of_type)

# Count of each region in the data set
count_of_region=pd.crosstab(index=data_csv['region'],columns='count',dropna=True)
print(count_of_region)

#To study coorelation between all the varibles
num_data=data_csv.select_dtypes(exclude=[object])
corr_matrix= num_data.corr()

#Exploratory Data Analysis

#FREQUENCY OF AVERAGE PRICE
plt.figure(figsize=(16,8))
plt.title("Distribution of the Average Price")
sns.distplot(data_csv["AveragePrice"])
plt.show()

#AVOCADOS SOLD IN 2015-2018
quantity_per_year= data_csv.groupby('year')['Total Volume'].sum().reset_index()
sns.catplot(x='year', y='Total Volume', kind='bar', data=quantity_per_year, height=10)
plt.xlabel('Year')
plt.ylabel('Number of avocados sold (billion avocados)')
plt.subplots_adjust(top=0.9)
plt.suptitle('Total avocados sold in the US between 2015-2018',  size=14)
plt.show()

#AVERAGE PRICE OF AVOCADO ACCORDING TO REGION
region_list=list(data_csv.region.unique())
average_price=[]

for i in region_list:
    x=data_csv[data_csv.region==i]
    region_average=sum(x.AveragePrice)/len(x)
    average_price.append(region_average)

df1=pd.DataFrame({'region_list':region_list,'average_price':average_price})
new_index=df1.average_price.sort_values(ascending=False).index.values
sorted_data=df1.reindex(new_index)

plt.figure(figsize=(15,10))
ax=sns.barplot(x=sorted_data.region_list,y=sorted_data.average_price,palette='rocket')

plt.xticks(rotation=90)
plt.xlabel('Region')
plt.ylabel('Average Price')
plt.title('Average Price of Avocado According to Region')

#AVERAGE PRICE OF AVOCADO ACCORDING TO TYPES(CONVENTIONAL/ORGANIC)
type_list=list(data_csv.type.unique())
average_price2=[]

for i in type_list:
    x=data_csv[data_csv.type==i]
    average_price2.append(sum(x.AveragePrice)/len(x))
df2=pd.DataFrame({'type_list':type_list,'average_price':average_price2})

plt.figure(figsize=(15,10))
ax=sns.barplot(x=df2.type_list,y=df2.average_price,palette='vlag')
plt.xlabel('Type of Avocado')
plt.ylabel('Average Price')
plt.title('Average Price of Avocado According to Types')

#AVERAGE PRICE ACCORDING TO YEARS
year_list=list(data_csv.year.unique())
average_price3=[]

for i in year_list:
    x=data_csv[data_csv.year==i]
    average_price3.append(sum(x.AveragePrice)/len(x))
df3=pd.DataFrame({'year_list':year_list,'average_price':average_price3})

plt.figure()
ax=sns.barplot(x=df3.year_list,y=df3.average_price)
plt.xlabel('Year')
plt.ylabel('Average Price')
plt.title('Average Price of Avocado According to Years')

#AVERAGE OF TOTAL VOLUME ACCORDING TO REGION
filter1=data_csv.region!='TotalUS'
data1=data_csv[filter1]


region_list=list(data1.region.unique())
average_total_volume=[]

for i in region_list:
    x=data1[data1.region==i]
    average_total_volume.append(sum(x['Total Volume'])/len(x))
df4=pd.DataFrame({'region_list':region_list,'average_total_volume':average_total_volume})

new_index=df4.average_total_volume.sort_values(ascending=False).index.values
sorted_data1=df4.reindex(new_index)

plt.figure(figsize=(15,10))
ax=sns.barplot(x=sorted_data1.region_list,y=sorted_data1.average_total_volume,palette='deep')

plt.xticks(rotation=90)
plt.xlabel('Region')
plt.ylabel('Average of Total Volume')
plt.title('Average of Total Volume According to Region')

#AVERAGE OF TOTAL VOLUME ACCORDİNG TO TYPE(CONVENTIONAL/ORGANIC)
type_list1=list(data_csv.region.unique())
average_total_volume1=[]

for i in type_list:
    x=data_csv[data_csv.type==i]
    average_total_volume1.append(sum(x['Total Volume']/len(x)))
df5=pd.DataFrame({'type_list':type_list,'average_total_volume1':average_total_volume1})

plt.figure(figsize=(15,10))
ax=sns.barplot(x=df5.type_list,y=df5.average_total_volume1)
plt.xlabel('Type of Avocado')
plt.ylabel('Average of Total Volume')
plt.title('Average of Total Volume According to Types')

#COMPARISION B/W TOTAL VOLUME & SMALL BAGS
data_csv.plot(kind = 'scatter', x = 'Small Bags', y = 'Total Volume', color = 'magenta')
plt.xlabel('Small Bags')
plt.ylabel('Total Volume')
plt.title("Comparison Between Total Volume and Small Bags")
plt.show()

#COMPARISION B/W TOTAL VOLUME & LARGE BAGS
data_csv.plot(kind = 'scatter', x = 'Large Bags', y = 'Total Volume', color = 'pink')
plt.xlabel('Large Bags')
plt.ylabel('Total Volume')
plt.title("Comparison Between Total Volume and Small Bags")
plt.show()

#COMPARISION B/W TOTAL VOLUME & XLARGE BAGS
data_csv.plot(kind = 'scatter', x = 'XLarge Bags', y = 'Total Volume', color = 'purple')
plt.xlabel('XLarge Bags')
plt.ylabel('Total Volume')
plt.title("Comparison Between Total Volume and Small Bags")
plt.show()