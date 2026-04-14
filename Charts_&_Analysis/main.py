import pandas as pd
import plotly.express as px

df_apps = pd.read_csv('apps.csv')

df_apps.dropna(inplace=True)
df_apps.drop_duplicates(subset=['App', 'Type', 'Price'], inplace=True)

print(df_apps.sort_values('Rating', ascending=False).head())
print(df_apps.sort_values('Size_MBs', ascending=False).head())
print(df_apps.sort_values('Reviews', ascending=False).head())

df_apps['Installs'] = df_apps['Installs'].astype(str).str.replace(',', '')
df_apps['Installs'] = pd.to_numeric(df_apps['Installs'].str.replace('+', ''))

df_apps['Price'] = pd.to_numeric(df_apps['Price'].astype(str).str.replace('$', ''))

# THE FIX IS HERE: Changed 'Content Rating' to 'Content_Rating'
ratings = df_apps['Content_Rating'].value_counts()
fig = px.pie(labels=ratings.index, values=ratings.values, title="Content Rating", names=ratings.index)
fig.update_traces(textposition='outside', textinfo='percent+label')
fig.show()

category_installs = df_apps.groupby('Category').agg({'Installs': pd.Series.sum})
category_installs.sort_values('Installs', ascending=True, inplace=True)
fig2 = px.pie(labels=category_installs.index, values=category_installs.Installs, title="Category vs Installs", names=category_installs.index, hole=0.6)
fig2.update_traces(textposition='inside', textinfo='percent')
fig2.show()

top10_category = df_apps['Category'].value_counts()[:10]
bar = px.bar(x=top10_category.index, y=top10_category.values)
bar.show()

category_merged_df = df_apps.groupby('Category').agg({'App': pd.Series.count, 'Installs': pd.Series.sum})
category_merged_df.sort_values('Installs', ascending=False, inplace=True)
scatter = px.scatter(category_merged_df, x='App', y='Installs', title='Category Concentration', size='App', hover_name=category_merged_df.index, color='Installs')
scatter.show()

stack = df_apps['Genres'].str.split(';', expand=True).stack()
num_genres = stack.value_counts()
genres_bar = px.bar(x=num_genres.index[:15], y=num_genres.values[:15], title='Top Genres', hover_name=num_genres.index[:15], color=num_genres.values[:15], color_continuous_scale='Agsunset')
genres_bar.show()

df_free_vs_paid = df_apps.groupby(["Category", "Type"], as_index=False).agg({'App': pd.Series.count})
fig_grouped_bar = px.bar(df_free_vs_paid, x='Category', y='App', title='Free vs Paid Apps by Category', color='Type', barmode='group')
fig_grouped_bar.update_layout(xaxis_title='Category', yaxis_title='Number of Apps', xaxis={'categoryorder':'total descending'}, yaxis=dict(type='log'))
fig_grouped_bar.show()

fig_box = px.box(df_apps, x='Type', y='Installs', color='Type', notched=True, points='all', title='How Many Downloads are Paid Apps Giving Up?')
fig_box.update_layout(yaxis=dict(type='log'))
fig_box.show()

df_paid_apps = df_apps[df_apps['Type'] == 'Paid']
fig_box_revenue = px.box(df_paid_apps, x='Category', y='Price', title='Price per Category')
fig_box_revenue.update_layout(xaxis_title='Category', yaxis_title='Paid App Price', xaxis={'categoryorder':'max descending'}, yaxis=dict(type='log'))
fig_box_revenue.show()