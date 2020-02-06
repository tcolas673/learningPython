# import pandas as pd 
# from matplotlib import pyplot as plt 

# x = [1,2,3]
# y = [1,4,9]
# z = [10,5,0]

# plt.plot(x,y)
# plt.plot(x,z)
# plt.title('test plot')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.legend(['this is y', 'this is z']) 
# plt.show()

# read csv files using pandas
# sample_data = pd.read_csv('filename')
#print(df.head)
#print(df.columns) reads headers
#df[name of Column]
#read each row df.head(numberofrows) or df.iloc[0:4] gets first 4 rows
#print(df.iloc[2,1]) gets 2nd row 1st column

# for index, row in df.iterrows
#     print(index, row)

# for index, row in df.iterrows
#     print(index, row['Name'])
# df.loc[df['Type 1'] == 'Fire']

# ascending sort
# df.sort_values('Name')

# ascending sort
# df.sort_values('Name', ascending = false)

# make new column
# df['Total'] = 
# delete column
# df = df.drop(columns=['Total'])

# df['Total'] = df.iloc[:,4:9]