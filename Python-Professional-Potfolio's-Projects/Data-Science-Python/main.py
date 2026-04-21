import pandas as pd
import plotly.express as px

# Updated the filename to match your project folder!
df = pd.read_csv("Deaths_by_Police_US.csv", encoding="windows-1252")

df = df.dropna(subset=['date', 'race', 'state', 'signs_of_mental_illness', 'age'])

df['date'] = pd.to_datetime(df['date'], format='mixed')
df['year'] = df['date'].dt.year

deaths_per_year = df['year'].value_counts().reset_index()
deaths_per_year.columns = ['Year', 'Deaths']
deaths_per_year = deaths_per_year.sort_values('Year')

fig_timeline = px.line(
    deaths_per_year,
    x='Year',
    y='Deaths',
    title='Police-Involved Deaths per Year',
    markers=True
)
fig_timeline.show()

race_counts = df['race'].value_counts().reset_index()
race_counts.columns = ['Race', 'Deaths']

fig_race = px.bar(
    race_counts,
    x='Race',
    y='Deaths',
    title='Total Deaths by Race',
    color='Deaths',
    color_continuous_scale='Reds'
)
fig_race.show()

mental_illness = df['signs_of_mental_illness'].value_counts().reset_index()
mental_illness.columns = ['Signs_of_Mental_Illness', 'Count']

fig_mental = px.pie(
    mental_illness,
    values='Count',
    names='Signs_of_Mental_Illness',
    title='Proportion of Incidents Involving Mental Illness',
    hole=0.4
)
fig_mental.show()

state_counts = df['state'].value_counts().reset_index()
state_counts.columns = ['State', 'Deaths']

fig_map = px.choropleth(
    state_counts,
    locations='State',
    locationmode="USA-states",
    color='Deaths',
    scope="usa",
    title='Total Deaths by State',
    color_continuous_scale='Reds'
)
fig_map.show()