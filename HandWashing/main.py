import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import scipy.stats as stats

df_yearly = pd.read_csv('annual_deaths_by_clinic.csv')
df_monthly = pd.read_csv('monthly_deaths.csv')

print(df_yearly.shape)
print(df_monthly.shape)

df_yearly['pct_deaths'] = df_yearly.deaths / df_yearly.births * 100

fig = px.line(df_yearly, x='year', y='pct_deaths', color='clinic', title='Proportion of Yearly Deaths by Clinic')
fig.show()

df_monthly.date = pd.to_datetime(df_monthly.date)
df_monthly['pct_deaths'] = df_monthly.deaths / df_monthly.births

handwashing_start = pd.to_datetime('1847-06-01')
before_washing = df_monthly[df_monthly.date < handwashing_start]
after_washing = df_monthly[df_monthly.date >= handwashing_start]

bw_rate = before_washing.pct_deaths.mean() * 100
aw_rate = after_washing.pct_deaths.mean() * 100
print(f"Average death rate before 1847: {bw_rate:.2f}%")
print(f"Average death rate AFTER 1847: {aw_rate:.2f}%")

roll_df = before_washing.set_index('date')
roll_df = roll_df.rolling(window=6).mean()

plt.figure(figsize=(14, 8), dpi=200)
plt.title('Percentage of Monthly Deaths over Time', fontsize=18)
plt.yticks(fontsize=14)
plt.xticks(fontsize=14, rotation=45)
plt.ylabel('Percentage of Deaths', color='crimson', fontsize=18)
ax = plt.gca()
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
ax.set_xlim([df_monthly.date.min(), df_monthly.date.max()])

plt.plot(before_washing.date, before_washing.pct_deaths, color='black', linewidth=1, linestyle='--', label='Before Handwashing')
plt.plot(roll_df.index, roll_df.pct_deaths, color='crimson', linewidth=3, linestyle='--', label='6m Moving Average')
plt.plot(after_washing.date, after_washing.pct_deaths, color='skyblue', linewidth=3, marker='o', label='After Handwashing')
plt.legend(fontsize=18)
plt.show()

plt.figure(figsize=(8, 4), dpi=200)
sns.kdeplot(before_washing.pct_deaths, fill=True, clip=(0,1), label='Before Handwashing')
sns.kdeplot(after_washing.pct_deaths, fill=True, clip=(0,1), label='After Handwashing')
plt.title('Est. Distribution of Monthly Death Rate Before and After Handwashing')
plt.xlim(0, 0.40)
plt.legend()
plt.show()

t_stat, p_value = stats.ttest_ind(a=before_washing.pct_deaths, b=after_washing.pct_deaths)
print(f"t-statistic: {t_stat:.4f}")
print(f"p-value: {p_value:.10f}")