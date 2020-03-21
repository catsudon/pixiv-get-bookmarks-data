import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

my_data = pd.read_csv('data.csv')
print(my_data.head(10))
print(my_data.describe())

# print(sns.scatterplot(my_data['Num'],my_data['Bookmarks']))


plt.scatter(my_data['Num'], my_data['Bookmarks'])
plt.title("Sam's Bookmarks")
plt.xlabel('')
plt.ylabel('popularity of bookmark')
plt.show()

