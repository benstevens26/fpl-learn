# importing all required statistics/data

import pandas as pd

num_gws = 23
csv_urls = []

for i in range(num_gws):
    # data from github user vaastav
    csv_urls.append(f'https://raw.githubusercontent.com/vaastav/Fantasy-Premier-League/master/data/2023-24/gws/gw{i+1}.csv')

dataframes = {}

for url in csv_urls:
    # use gw as key
    filename = url.split('/')[-1].replace('.csv', '')
    # read csv to df
    dataframes[filename] = pd.read_csv(url)
    print(filename+" data loaded")


# creating individual player dfs with features for model (number of entries = number of gws used)
player_dfs = {}
names = []
gw_num = 1


# creating df for each player that has played at least 1 gw
for gw in dataframes.values():
    for index, row in gw.iterrows():
        name = row['name']
        if name not in names: # if name df isn't yet created
            names.append(name)
            new_df = pd.DataFrame(columns=['GW', 'xG', 'G', 'xA', 'A', 'Points'], index=range(num_gws))
            player_dfs[name] = new_df

for gw in dataframes.values():
    for index, row in gw.iterrows():
        xg = row['expected_goals']
        xa = row['expected_assists']
        points = row['total_points']
        g = row['goals_scored']
        a = row['assists']
        player_dfs[row['name']].iloc[gw_num-1] = (gw_num, xg, g, xa, a, points)

    gw_num += 1





