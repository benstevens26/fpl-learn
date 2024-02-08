# importing all required statistics/data

import pandas as pd

num_gws = 23
csv_urls = []

for i in range(num_gws):
    csv_urls.append(f'https://raw.githubusercontent.com/vaastav/Fantasy-Premier-League/master/data/2023-24/gws/gw{i+1}')

print(csv_urls)


dataframes = {}

for url in csv_urls:
    # Extracting filename or identifier from URL for use as a key
    filename = url.split('/')[-1].replace('.csv', '')

    # pd read csv into df
    dataframes[filename] = pd.read_csv(url)



gw1 = dataframes['gw1']

xg_argmax = gw1['expected_goals'].argmax()

print(gw1.iloc[xg_argmax])


