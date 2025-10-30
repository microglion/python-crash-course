from pathlib import Path
import csv

# Check Sitka temperature range
path = Path('weather_data/sitka_weather_2021_simple.csv')
lines = path.read_text(encoding='utf-8').splitlines()
reader = csv.reader(lines)
header_row = next(reader)

sitka_highs, sitka_lows = [], []
for row in reader:
    try:
        sitka_highs.append(int(row[4]))
        sitka_lows.append(int(row[5]))
    except ValueError:
        pass

print("SITKA TEMPERATURE RANGE:")
print(f"  High: {min(sitka_highs)}°F - {max(sitka_highs)}°F")
print(f"  Low:  {min(sitka_lows)}°F - {max(sitka_lows)}°F")
print(f"  Overall range: {min(sitka_lows)}°F - {max(sitka_highs)}°F")

# Check Death Valley temperature range
path = Path('weather_data/death_valley_2021_simple.csv')
lines = path.read_text(encoding='utf-8').splitlines()
reader = csv.reader(lines)
header_row = next(reader)

dv_highs, dv_lows = [], []
for row in reader:
    try:
        dv_highs.append(int(row[3]))
        dv_lows.append(int(row[4]))
    except ValueError:
        pass

print("\nDEATH VALLEY TEMPERATURE RANGE:")
print(f"  High: {min(dv_highs)}°F - {max(dv_highs)}°F")
print(f"  Low:  {min(dv_lows)}°F - {max(dv_lows)}°F")
print(f"  Overall range: {min(dv_lows)}°F - {max(dv_highs)}°F")

# Combined range
overall_min = min(min(sitka_lows), min(dv_lows))
overall_max = max(max(sitka_highs), max(dv_highs))
print(f"\nCOMBINED RANGE FOR COMPARISON:")
print(f"  {overall_min}°F - {overall_max}°F")
print(f"\nSuggested y-axis limits: ax.set_ylim({overall_min - 5}, {overall_max + 5})")
