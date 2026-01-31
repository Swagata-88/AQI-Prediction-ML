import pandas as pd

# Load daily AQI data for Bangalore
file_path = "data/daily aqi (2015-2024)-Bangalore.csv"
daily_aqi_data = pd.read_csv(file_path)

# Convert Date column to datetime
daily_aqi_data["Date"] = pd.to_datetime(daily_aqi_data["Date"])

# Calculate monthly average AQI
monthly_aqi = (
    daily_aqi_data
    .groupby(daily_aqi_data["Date"].dt.to_period("M"))["AQI"]
    .mean()
)

# Convert to DataFrame
monthly_aqi = monthly_aqi.reset_index()
monthly_aqi.columns = ["Month", "Average_AQI"]

# Save output
output_path = "data/bangalore_monthly_aqi.csv"
monthly_aqi.to_csv(output_path, index=False)

# Print result
print("Monthly AQI data for Bangalore:")
print(monthly_aqi)
