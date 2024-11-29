"""
Retrieve the most recent FPL data

"""

import aiohttp
import asyncio
import csv
from fpl import FPL


async def main():
    async with aiohttp.ClientSession() as session:
        fpl = FPL(session)
        players = await fpl.get_players()

        # Prepare the data for the CSV
        player_data = []
        for player in players:
            player_name = f"{player.first_name} {player.second_name}"
            element_type = player.element_type
            now_cost = player.now_cost
            player_data.append({'Player': player_name, 'Position': element_type, 'Cost': now_cost})

        # Write the data to a CSV
        with open('player_data.csv', mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['Player', 'Position', 'Cost'])
            writer.writeheader()  # Write column headers
            writer.writerows(player_data)  # Write player data


asyncio.run(main())