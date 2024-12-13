# import pandas as pd
# import matplotlib.pyplot as plt

# df = pd.read_csv('c:/Users/admin/Downloads/Mall_Customers.csv')
# data = df.groupby('Genre')['Spending Score (1-100)'].idxmax()
# df1 = df.loc[df['Genre'] == 'Female']
# df2 = df.loc[df['Genre'] == 'Male']
# print(df)
# print(df1['Annual Income (k$)'].mean())
# print(df.loc[data, ['Genre', 'CustomerID', 'Spending Score (1-100)']])

# df2 = df2.sort_values('Age')
# df2.plot(x = 'Age', y = 'Annual Income (k$)', kind= 'bar')
# plt.title('Male')
# plt.show()

# df1.plot(x = 'Annual Income (k$)', y = 'Spending Score (1-100)', kind = 'bar')
# plt.title('Female')
# df2.plot(x = 'Annual Income (k$)', y = 'Spending Score (1-100)', kind = 'bar')
# plt.title('Male')
# plt.legend()
# plt.show()
