import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

data = pd.read_csv('cost_revenue_dirty.csv')

chars_to_remove = [',', '$']
columns_to_clean = ['USD_Production_Budget', 'USD_Worldwide_Gross', 'USD_Domestic_Gross']

for col in columns_to_clean:
    for char in chars_to_remove:
        data[col] = data[col].astype(str).str.replace(char, "")
    data[col] = pd.to_numeric(data[col])

data.Release_Date = pd.to_datetime(data.Release_Date)

data = data[data.USD_Worldwide_Gross != 0]

data['Decade'] = (data.Release_Date.dt.year // 10) * 10

plt.figure(figsize=(8,4), dpi=200)
with sns.axes_style("darkgrid"):
    ax = sns.scatterplot(data=data,
                         x='USD_Production_Budget',
                         y='USD_Worldwide_Gross',
                         hue='USD_Worldwide_Gross',
                         size='USD_Worldwide_Gross')
    ax.set(ylim=(0, 3000000000),
           xlim=(0, 450000000),
           ylabel='Revenue in $ Billions',
           xlabel='Budget in $100 Millions')
plt.show()

plt.figure(figsize=(8,4), dpi=200)
with sns.axes_style("whitegrid"):
    sns.regplot(data=data,
                x='USD_Production_Budget',
                y='USD_Worldwide_Gross',
                scatter_kws={'alpha': 0.4},
                line_kws={'color': '#ff7c43'})
plt.show()

regression = LinearRegression()
X = pd.DataFrame(data, columns=['USD_Production_Budget'])
y = pd.DataFrame(data, columns=['USD_Worldwide_Gross'])

regression.fit(X, y)

print(regression.intercept_)
print(regression.coef_)
print(regression.score(X, y))