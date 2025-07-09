from statsmodels.tsa.statespace.sarimax import SARIMAX

def run_sarimax_forecast(series, order=(1,1,1), steps=12):
    """Fit a SARIMAX model and forecast future values."""
    model = SARIMAX(series, order=order)
    results = model.fit(disp=False)
    forecast = results.get_forecast(steps=steps)
    return forecast.predicted_mean