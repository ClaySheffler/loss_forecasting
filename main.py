import os
from src.data_loading import load_input_data, save_output_data
from src.forecasting import run_sarimax_forecast
from src.visualization import plot_forecast

# Load data
input_path = "data/inputs/your_data.xlsx"
df = load_input_data(input_path)

# Assume your time series is in a column named 'value'
series = df['value']

# Run forecast
forecast = run_sarimax_forecast(series, order=(1,1,1), steps=12)

# Save results
output_df = df.copy()
output_df['forecast'] = forecast
save_output_data(output_df, "data/outputs/forecast_results.xlsx")

# Plot results
plot_forecast(series, forecast)