import pandas as pd
import matplotlib.pyplot as plt

colors = pd.read_csv('data/colors.csv')
print(colors['name'].nunique())
print(colors.groupby('is_trans').count())

sets = pd.read_csv('data/sets.csv')
print(sets.sort_values('year').head())
print(sets[sets['year'] == 1949])
print(sets.sort_values('num_parts', ascending=False).head())

sets_by_year = sets.groupby('year').count()
sets_by_year = sets_by_year[:-2]

plt.plot(sets_by_year.index, sets_by_year.set_num)
plt.show()

themes_by_year = sets.groupby('year').agg({'theme_id': pd.Series.nunique})
themes_by_year.rename(columns={'theme_id': 'nr_themes'}, inplace=True)
themes_by_year = themes_by_year[:-2]

ax1 = plt.gca()
ax2 = ax1.twinx()
ax1.plot(sets_by_year.index, sets_by_year.set_num, color='g')
ax2.plot(themes_by_year.index, themes_by_year.nr_themes, color='b')
ax1.set_xlabel('Year')
ax1.set_ylabel('Number of Sets', color='g')
ax2.set_ylabel('Number of Themes', color='b')
plt.show()

parts_per_set = sets.groupby('year').agg({'num_parts': pd.Series.mean})
plt.scatter(parts_per_set.index, parts_per_set.num_parts)
plt.show()

themes = pd.read_csv('data/themes.csv')
set_theme_count = sets['theme_id'].value_counts()
set_theme_count = pd.DataFrame({'id': set_theme_count.index, 'set_count': set_theme_count.values})
merged_df = pd.merge(set_theme_count, themes, on='id')

plt.figure(figsize=(14,8))
plt.xticks(fontsize=14, rotation=45)
plt.yticks(fontsize=14)
plt.ylabel('Nr of Sets', fontsize=14)
plt.xlabel('Theme Name', fontsize=14)
plt.bar(merged_df.name[:10], merged_df.set_count[:10])
plt.show()