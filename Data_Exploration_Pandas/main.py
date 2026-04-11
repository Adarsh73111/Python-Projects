import pandas as pd

df = pd.read_csv('salaries_by_college_major.csv')

print(df.head())

print(df.shape)

clean_df = df.dropna()
print(clean_df.tail())

print(clean_df['Starting Median Salary'].max())

print(clean_df['Starting Median Salary'].idxmax())

print(clean_df.loc[43])

spread_col = clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary']

clean_df.insert(1, 'Spread', spread_col)

low_risk = clean_df.sort_values('Spread')
print(low_risk[['Undergraduate Major', 'Spread']].head())

pd.options.display.float_format = '{:,.2f}'.format
print(clean_df.groupby('Group').mean(numeric_only=True))