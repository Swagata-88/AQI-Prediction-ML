import pandas as pd
import matplotlib.pyplot as plt

aqi = pd.read_csv("data/kolkata_monthly_aqi.csv")

# Convert Month to datetime
aqi["Month"] = pd.to_datetime(aqi["Month"])

plt.figure(figsize=(12,5))
plt.plot(aqi["Month"], aqi["Average_AQI"], marker="o", color="blue")

plt.title("Monthly AQI Trend - Kolkata (2015–2024)")
plt.xlabel("Year")
plt.ylabel("Average AQI")

# Show only yearly labels (January of each year)
year_ticks = aqi[aqi["Month"].dt.month == 1]["Month"]
year_labels = year_ticks.dt.year.astype(str)

plt.xticks(year_ticks, year_labels, fontsize=9)

plt.grid(True)
plt.tight_layout()
plt.show()
