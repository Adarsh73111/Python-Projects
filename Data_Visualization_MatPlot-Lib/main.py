import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('QueryResults.csv', names=['DATE', 'TAG', 'POSTS'], header=0)

print(df.head())
print(df.tail())
print(df.shape)
print(df.count())

print(df.groupby('TAG').sum(numeric_only=True))

df.DATE = pd.to_datetime(df.DATE)

reshaped_df = df.pivot(index='DATE', columns='TAG', values='POSTS')

reshaped_df.fillna(0, inplace=True)

print(reshaped_df.head())
print(reshaped_df.shape)

roll_df = reshaped_df.rolling(window=6).mean()

plt.figure(figsize=(16, 10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)

for column in roll_df.columns:
    plt.plot(roll_df.index, roll_df[column], linewidth=3, label=roll_df[column].name)

plt.legend(fontsize=16)
plt.show()