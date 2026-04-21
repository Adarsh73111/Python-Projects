import pandas as pd
import plotly.express as px

df = pd.read_csv("mission_launches.csv")

df = df.dropna(subset=['Organisation', 'Location', 'Date', 'Detail', 'Rocket_Status', 'Price', 'Mission_Status'])

df['Price'] = df['Price'].astype(str).str.replace(',', '').astype(float)
df['Date'] = pd.to_datetime(df['Date'], format='mixed', utc=True)
df['Year'] = df['Date'].dt.year

launches_per_year = df['Year'].value_counts().reset_index()
launches_per_year.columns = ['Year', 'Launches']
launches_per_year = launches_per_year.sort_values('Year')

fig_timeline = px.line(
    launches_per_year,
    x='Year',
    y='Launches',
    title='Space Missions per Year'
)
fig_timeline.show()

org_launches = df['Organisation'].value_counts().reset_index()
org_launches.columns = ['Organisation', 'Total_Launches']

fig_orgs = px.bar(
    org_launches,
    x='Organisation',
    y='Total_Launches',
    title='Total Launches by Organisation',
    color='Total_Launches',
    color_continuous_scale='Viridis'
)
fig_orgs.update_layout(xaxis={'categoryorder':'total descending'})
fig_orgs.show()

status_counts = df['Mission_Status'].value_counts().reset_index()
status_counts.columns = ['Status', 'Count']

fig_status = px.pie(
    status_counts,
    values='Count',
    names='Status',
    title='Mission Status Distribution',
    hole=0.4
)
fig_status.show()

df_cost = df.groupby('Organisation')['Price'].sum().reset_index()
df_cost = df_cost.sort_values('Price', ascending=False).head(10)

fig_cost = px.bar(
    df_cost,
    x='Organisation',
    y='Price',
    title='Top 10 Organisations by Total Money Spent (in Millions)',
    text='Price'
)
fig_cost.show()