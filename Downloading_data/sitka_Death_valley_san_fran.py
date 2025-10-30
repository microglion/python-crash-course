from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt

def get_weather_data(filepath, year=2021, station_filter=None):
    """Reads any weather CSV and returns station name, dates, high and low temps.
    Can filter by year and specific station."""
    path = Path(filepath)
    lines = path.read_text(encoding='utf-8').splitlines()
    reader = csv.reader(lines)
    header = next(reader)

    #get indexes for any station
    name_index = header.index('NAME')
    date_index = header.index('DATE')
    tmax_index = header.index('TMAX')
    tmin_index = header.index('TMIN')
    station_index = header.index('STATION')

    station_name = None
    dates, highs, lows = [], [], []

    for row in reader:
        # Filter by station if specified
        if station_filter and row[station_index] != station_filter:
            continue

        current_date = datetime.strptime(row[date_index],'%Y-%m-%d')

        # Filter by year
        if current_date.year != year:
            continue

        if station_name is None:
            station_name = row[name_index]

        try:
            high = int(row[tmax_index])
            low = int(row[tmin_index])
        except ValueError:
            continue

        dates.append(current_date)
        highs.append(high)
        lows.append(low)

    return dates, highs, lows, station_name
    
dates_sitka, highs_sitka, lows_sitka, name_sitka = get_weather_data('weather_data/sitka_weather_2021_simple.csv')
dates_dv, highs_dv, lows_dv, name_dv = get_weather_data('weather_data/death_valley_2021_simple.csv')
dates_sf, highs_sf, lows_sf, name_sf = get_weather_data('weather_data/san_francisco_weather_2021.csv', year=2021, station_filter='USW00023234')

#Plot all values
plt.style.use('seaborn-v0_8')
fig,ax = plt.subplots()
ax.plot(dates_sitka, highs_sitka, color='blue',alpha=0.5, label='Sitka Highs')
ax.plot(dates_sitka,lows_sitka,color='lightblue',alpha=0.5, label='Sitka Lows')
ax.fill_between(dates_sitka,highs_sitka,lows_sitka,facecolor='blue',alpha=0.1)
ax.plot(dates_dv, highs_dv, color='red', alpha=0.5, label='Death Valley Highs')
ax.plot(dates_dv, lows_dv, color='orange', alpha=0.5, label='Death Valley Lows')
ax.fill_between(dates_dv, highs_dv, lows_dv, facecolor='red', alpha=0.1)
ax.plot(dates_sf, highs_sf, color='purple', alpha=0.5, label='San Francisco Highs')
ax.plot(dates_sf, lows_sf, color='green', alpha=0.5, label='San Francisco Lows')
ax.fill_between(dates_sf, highs_sf, lows_sf, facecolor='purple', alpha=0.1)
#Format plot.
ax.set_title(f"Daily High and Low Temperatures - 2021\n{name_sitka}, {name_dv}\n, {name_sf}", fontsize=12)
ax.set_xlabel('', fontsize=10)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=10)
ax.tick_params(labelsize=10)

ax.legend(fontsize=8)
plt.show()
