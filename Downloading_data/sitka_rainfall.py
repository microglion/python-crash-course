from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt


path = Path('weather_data/sitka_weather_2021_full.csv')
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)

#Extract dates and high and low temperatures.
precipitation = []
dates = []
for row in reader:
    current_date = datetime.strptime(row[2],'%Y-%m-%d')
    try:
        current_prec = float(row[5])
    except ValueError:
        print(f"Data missing for {current_date}")
    else:
        dates.append(current_date)
        precipitation.append(current_prec)
        

#Plot the high and low temperatures.
plt.style.use('seaborn-v0_8')
fig,ax = plt.subplots()
ax.plot(dates, precipitation, color='blue',alpha=0.5)


#Format plot.
ax.set_title("Daily precipitation, Sitka, AK, 2021, fontsize=24")
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Precipitation (\")", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
