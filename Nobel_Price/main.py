import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

df_data = pd.read_csv('nobel_prize_data.csv')

gender_counts = df_data.sex.value_counts()
fig1 = px.pie(labels=gender_counts.index, values=gender_counts.values, title="Nobel Prize by Gender", names=gender_counts.index, hole=0.4)
fig1.update_traces(textinfo='percent+label')
fig1.show()

cat_counts = df_data.category.value_counts()
fig2 = px.bar(x=cat_counts.index, y=cat_counts.values, title="Prizes by Category", color=cat_counts.values)
fig2.show()

prize_per_year = df_data.groupby('year').count()['prize']
moving_average = prize_per_year.rolling(window=5).mean()

plt.figure(figsize=(12, 6), dpi=150)
plt.title('Number of Nobel Prizes Awarded per Year', fontsize=18)
plt.yticks(fontsize=14)
plt.xticks(fontsize=14, rotation=45)
ax = plt.gca()
ax.set_xlim(1900, 2020)
ax.scatter(x=prize_per_year.index, y=prize_per_year.values, c="dodgerblue", alpha=0.7, s=100)
ax.plot(prize_per_year.index, moving_average.values, c="crimson", linewidth=3)
plt.show()

top_countries = df_data.groupby(['birth_country_current'], as_index=False).agg({'prize': pd.Series.count})
top_countries.sort_values('prize', inplace=True, ascending=False)
fig3 = px.choropleth(top_countries, locations='birth_country_current', locationmode='country names', color='prize', hover_name='birth_country_current', color_continuous_scale=px.colors.sequential.matter)
fig3.show()

country_city_org = df_data.groupby(['organization_country', 'organization_city', 'organization_name'], as_index=False).agg({'prize': pd.Series.count})
country_city_org = country_city_org[country_city_org.prize > 0]
fig4 = px.sunburst(country_city_org, path=['organization_country', 'organization_city', 'organization_name'], values='prize', title='Where do Discoveries Take Place?')
fig4.show()

df_data['birth_date'] = pd.to_datetime(df_data['birth_date'], errors='coerce')
df_data['winning_age'] = df_data['year'] - df_data['birth_date'].dt.year

plt.figure(figsize=(8, 4), dpi=200)
sns.regplot(data=df_data, x='year', y='winning_age', lowess=True, scatter_kws={'alpha': 0.4}, line_kws={'color': 'black'})
plt.title('Age of Nobel Laureates Over Time')
plt.show()

plt.figure(figsize=(8, 4), dpi=200)
sns.boxplot(data=df_data, x='category', y='winning_age')
plt.title('Age of Laureates by Category')
plt.show()