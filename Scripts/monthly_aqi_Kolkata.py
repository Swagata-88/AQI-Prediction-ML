import pandas as pd

# 1. Load daily AQI data for Kolkata
file_path = "data/daily aqi (2015-2024)-Kolkata.csv"
daily_aqi_data = pd.read_csv(file_path)

# 2. Convert the Date column to datetime format
daily_aqi_data["Date"] = pd.to_datetime(daily_aqi_data["Date"])

# 3. Group by month and calculate average AQI
monthly_aqi = (
    daily_aqi_data
    .groupby(daily_aqi_data["Date"].dt.to_period("M"))["AQI"]
    .mean()
)

# 4. Convert result to DataFrame
monthly_aqi = monthly_aqi.reset_index()
monthly_aqi.columns = ["Month", "Average_AQI"]

# 5. Save the monthly AQI data to CSV
output_path = "data/kolkata_monthly_aqi.csv"
monthly_aqi.to_csv(output_path, index=False)

# 6. Print result
print("Monthly AQI data for Kolkata:")
print(monthly_aqi)
