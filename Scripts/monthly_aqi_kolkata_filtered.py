import pandas as pd

# Load Kolkata daily AQI data
file_path = "data/daily aqi (2015-2024)-Kolkata.csv"
data = pd.read_csv(file_path)

# Convert Date column to datetime
data["Date"] = pd.to_datetime(data["Date"])

# Remove AQI values below 20
filtered_data = data[data["AQI"] >= 20]

# Calculate monthly average AQI
monthly_aqi = (
    filtered_data
    .groupby(filtered_data["Date"].dt.to_period("M"))["AQI"]
    .mean()
)

# Convert to DataFrame
monthly_aqi = monthly_aqi.reset_index()
monthly_aqi.columns = ["Month", "Average_AQI"]

# Save cleaned monthly data
output_path = "data/kolkata_monthly_aqi_filtered.csv"
monthly_aqi.to_csv(output_path, index=False)

print("Filtered Monthly AQI (Kolkata):")
print(monthly_aqi)
